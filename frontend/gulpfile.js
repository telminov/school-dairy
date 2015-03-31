var gulp = require('gulp');
var gutil = require('gulp-util');
var concat = require('gulp-concat');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var coffee = require('gulp-coffee');
var angularTemplates = require('gulp-angular-templates');

gulp.task('html', function () {
    return gulp.src('./src/app/controllers/**/*.html')
        .pipe(angularTemplates({basePath: 'src/app/controllers/', module: 'schoolDairy'}))
        .pipe(concat('templates.js'))
        .pipe(gulp.dest('./dist/'));
});

gulp.task('js', function() {
  gulp.src('./src/app/**/*.coffee')
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
    gulp.watch('./src/app/**/*.coffee', ['js']);
    gulp.watch('./src/app/controllers/**/*.html', ['html']);
});