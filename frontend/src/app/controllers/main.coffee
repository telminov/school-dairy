angular.module('schoolDairy')
.controller 'MainCtrl', ($scope, $location) ->
    $location.path('/schedule/')