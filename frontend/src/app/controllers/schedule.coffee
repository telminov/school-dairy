angular.module('schoolDairy')
.controller 'ScheduleCtrl', ($scope, $log, toaster, schedule, DayItem) ->
    $scope.schedule = schedule
    $scope.dayItems = DayItem.query()

    $scope.loading = true
    schedule.load().then(
        -> $scope.loading = false
        (response) ->
            $scope.loading = false
            toaster.pop('error', 'Ошибка', 'Не удалось получить расписание занятий')
            $log.error(response)
    )
