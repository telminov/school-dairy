angular.module('schoolDairy')
.service 'schedule', ($http, config) ->
    this.days = []

    this.load = ->
        this.days.length = 0

        url = "#{ config.serverAddress }/get_schedule/"
        promise = $http.get(url)
        promise.then(
            (response) =>
                for item in response.data.schedule
                    this.days.push(item)
        )
        return promise

    this.getAllDayItems = ->
        return []

    return