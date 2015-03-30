angular.module('schoolDairy')
.controller 'ScheduleCtrl', ($scope, schedule, DayItem) ->
    $scope.schedule = schedule
    $scope.dayItems = DayItem.query()

    $scope.loading = true
    schedule.load().then(
        -> $scope.loading = false
        -> $scope.loading = false
    )
