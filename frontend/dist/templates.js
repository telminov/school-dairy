angular.module('schoolDairy').run(['$templateCache', function($templateCache) {
    $templateCache.put('src/app/controllers/login.html',
        "<div class=\"header\">\n    <h3 class=\"text-muted\">{{ header }}</h3>\n</div>\n\n<div>\n    <alert ng-repeat=\"error in loginErrors\" type=\"danger\" close=\"closeAlert($index)\">\n        {{ error }}\n    </alert>\n\n    <h1>Вход</h1>\n    <form class=\"form-horizontal authentication\" ng-submit=\"logIn()\">\n        <div class=\"form-group\">\n            <label for=\"inputLogin\" class=\"col-lg-2 control-label\">Логин</label>\n            <div class=\"col-lg-8\">\n                <input type=\"text\" class=\"form-control\" id=\"inputLogin\" placeholder=\"логин\"\n                       ng-model=\"login\" autofocus=\"autofocus\" required>\n            </div>\n        </div>\n        <div class=\"form-group\">\n            <label for=\"inputPassword\" class=\"col-lg-2 control-label\">Пароль</label>\n            <div class=\"col-lg-8\">\n                <input type=\"password\" class=\"form-control\" id=\"inputPassword\"\n                       placeholder=\"пароль\" ng-model=\"password\" required>\n            </div>\n        </div>\n        <div class=\"form-group\">\n            <div class=\"col-lg-offset-2 col-lg-8\">\n                <button type=\"submit\" class=\"btn btn-default\">Войти</button>\n            </div>\n        </div>\n    </form>\n</div>");
}]);
angular.module('schoolDairy').run(['$templateCache', function($templateCache) {
    $templateCache.put('src/app/controllers/logout.html',
        "<div class=\"header\">\n    <h3 class=\"text-muted\">{{ header }}</h3>\n</div>\n\n<alert type=\"danger\" ng-show=\"logoutError\">{{ logoutError }}</alert>\n\n<h1>Выход</h1>\n<p ng-if=\"inProcess\">\n    Выхожу...\n</p>\n");
}]);
angular.module('schoolDairy').run(['$templateCache', function($templateCache) {
    $templateCache.put('src/app/controllers/main.html',
        "Главная");
}]);
angular.module('schoolDairy').run(['$templateCache', function($templateCache) {
    $templateCache.put('src/app/controllers/schedule.html',
        "<div class=\"panel panel-default\" sw-loading=\"loading\">\n    <div class=\"panel-heading\">Расписание занятий</div>\n\n    <table class=\"table table-striped table-hover\" ng-show=\"dayItems.length > 0\">\n        <thead>\n            <tr>\n                <th>#</th>\n                <th ng-repeat=\"day in schedule.days\">{{ day.name }}</th>\n                <th><span class=\"glyphicon glyphicon-time\"></span></th>\n            </tr>\n        </thead>\n\n        <tbody>\n            <tr ng-repeat=\"dayItem in dayItems\">\n                <td>{{ $index+1 }}</td>\n\n                <td ng-repeat=\"day in schedule.days\" ng-class=\"{warning: schedule.getItem(day.name, dayItem).is_current_day}\">\n                    {{ schedule.getItem(day.name, dayItem).subject.name }}\n                </td>\n\n                <td>\n                    <span class=\"label label-info\">{{ dayItem.time_from }} - {{ dayItem.time_to }}</span>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n\n</div>");
}]);