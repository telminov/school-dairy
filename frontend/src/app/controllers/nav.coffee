angular.module('schoolDairy')
.controller 'NavBarCtrl', ($scope, $location, auth) ->
    $scope.auth = auth

    $scope.isActive = (viewLocation) ->
        return viewLocation == $location.path()
