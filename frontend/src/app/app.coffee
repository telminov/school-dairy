angular.module('schoolDairy', [
    'ngResource'
    'ngSanitize'
    'ngRoute'
    'ngAnimate'

    'ui.bootstrap'
    'toaster'

    'swAuth'
    'swUtils'
])

.config ($routeProvider) ->
    $routeProvider

    .when('/',
        templateUrl: 'src/app/controllers/main.html'
        controller: 'MainCtrl'
        label: ''
    )

    .when('/schedule/',
        templateUrl: 'src/app/controllers/schedule.html'
        controller: 'ScheduleCtrl'
        label: 'Расписание'
    )

    .when('/login/',
        templateUrl: 'src/app/controllers/login.html'
        controller: 'AuthLoginCtrl'
        label: 'Вход'
    )
    .when('/logout/',
        templateUrl: 'src/app/controllers/logout.html'
        controller: 'AuthLogoutCtrl'
        label: 'Выход'
    )


.config (authConfigProvider, config) ->
    authConfigProvider.setSystemLabel('Дневник')
    authConfigProvider.setServerAddress(config.serverAddress)

.config ($httpProvider) ->
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'

.run ($location, $rootScope, swTitle) ->
    $rootScope.swTitle = swTitle

    $rootScope.$on '$routeChangeSuccess', (event, current, previous) ->
        baseTitle = current.$$route?.label or ''
        swTitle.setTitleBase(baseTitle)
        swTitle.setTitleStart('')
        swTitle.setTitleEnd('')