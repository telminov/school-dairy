var gulp = require('gulp');
var gutil = require('gulp-util');
var concat = require('gulp-concat');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var coffee = require('gulp-coffee');
var angularTemplates = require('gulp-angular-templates');

var paths = {
  scripts: ['./src/app/**/*.coffee'],
  html: './src/app/controllers/**/*.html'
};

gulp.task('html', function () {
    return gulp.src(paths.html)
        .pipe(angularTemplates({basePath: 'src/app/controllers/', module: 'schoolDairy'}))
        .pipe(concat('templates.js'))
        .pipe(gulp.dest('./dist/'));
});

gulp.task('js', function() {
  gulp.src(paths.scripts)
      .pipe(sourcemaps.init())
      .pipe(coffee().on('error', gutil.log))
      .pipe(concat('app.js'))
      .pipe(sourcemaps.write())
      .pipe(gulp.dest('./dist/'));
});

gulp.task('compress', function() {
    gulp.src('./dist/app.js')
        .pipe(uglify({
            mangle: false
        }))
        .pipe(rename('app.min.js'))
        .pipe(gulp.dest('./dist/'));
});

gulp.task('watch', function() {
    gulp.watch(paths.scripts, ['js', 'compress']);
    gulp.watch(paths.html, ['html']);
});