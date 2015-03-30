angular.module('schoolDairy')

.service 'schedule', ($http, config) ->
    this.days = []
    this._items = {}

    this.load = ->
        this.days.length = 0
        this._items = {}

        url = "#{ config.serverAddress }/get_schedule/"
        promise = $http.get(url)
        promise.then(
            (response) =>
                for day in response.data.schedule
                    this.days.push(day)

                    for item in day.items
                        if not this._items[day.name]
                            this._items[day.name] = {}
                        this._items[day.name][item.day_item.id] = item

        )
        return promise

    this.getItem = (dayName, dayItem) =>
        return this._items[dayName]?[dayItem.id]

    return