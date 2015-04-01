angular.module('schoolDairy').run(['$templateCache', function($templateCache) {
    $templateCache.put('src/app/controllers/main.html',
        "Главная");
}]);
angular.module('schoolDairy').run(['$templateCache', function($templateCache) {
    $templateCache.put('src/app/controllers/schedule.html',
        "<div class=\"panel panel-default\" sw-loading=\"loading\">\n    <div class=\"panel-heading\">Расписание занятий</div>\n\n    <table class=\"table table-striped table-hover\" ng-show=\"dayItems.length > 0\">\n        <thead>\n            <tr>\n                <th>#</th>\n                <th ng-repeat=\"day in schedule.days\">{{ day.name }}</th>\n                <th><span class=\"glyphicon glyphicon-time\"></span></th>\n            </tr>\n        </thead>\n\n        <tbody>\n            <tr ng-repeat=\"dayItem in dayItems\">\n                <td>{{ $index+1 }}</td>\n\n                <td ng-repeat=\"day in schedule.days\" ng-class=\"{warning: schedule.getItem(day.name, dayItem).is_current_day}\">\n                    {{ schedule.getItem(day.name, dayItem).subject.name }}\n                </td>\n\n                <td>\n                    <span class=\"label label-info\">{{ dayItem.time_from }} - {{ dayItem.time_to }}</span>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n\n</div>");
}]);