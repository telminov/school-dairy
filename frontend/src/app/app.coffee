angular.module('schoolDairy', [
    'ngResource'
    'ngSanitize'
    'ngRoute'
    'ngAnimate'

    'ui.bootstrap'

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

.run ($location, $rootScope, swTitle) ->
    $rootScope.swTitle = swTitle

    $rootScope.$on '$routeChangeSuccess', (event, current, previous) ->
        baseTitle = current.$$route?.label or ''
        swTitle.setTitleBase(baseTitle)
        swTitle.setTitleStart('')
        swTitle.setTitleEnd('')