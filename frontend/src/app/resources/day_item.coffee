angular.module('schoolDairy')

.factory 'DayItem', ($resource, config) ->
    url = "#{ config.serverAddress }/day_item/:id/"
    return $resource(url)