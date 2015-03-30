angular.module('schoolDairy')
.controller 'ScheduleCtrl', ($scope, schedule) ->
    $scope.schedule = schedule

    $scope.loading = true
    schedule.load().then(
        -> $scope.loading = false
        -> $scope.loading = false
    )
