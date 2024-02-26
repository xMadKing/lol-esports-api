from lol_esp_api.apis.supfunc import request


def getSchedule(leagueID, pageToken=""):
    url = (
        "https://esports-api.lolesports.com/persisted/gw/getSchedule?leagueId={0}&pageToken={1}"
        "&hl=en-US".format(leagueID, pageToken)
    )

    return request(url)


def getAllEvents(leagueID):
    events = []
    pageToken = ""
    while True:
        schedule = getSchedule(leagueID=leagueID, pageToken=pageToken)["data"]["schedule"]
        nextEvents, pageToken = schedule["events"], schedule["pages"]["newer"]
        events += nextEvents
        if not pageToken:
            break
    return events


def getLive():
    url = "https://esports-api.lolesports.com/persisted/gw/getLive?hl=en-US"

    return request(url)


def getCompeletedEvents(eventID):
    url = "https://esports-api.lolesports.com/persisted/gw/getCompletedEvents?tournamentId={0}&hl=en-US".format(
        eventID
    )

    return request(url)


def getEventDetails(eventID):
    url = "https://esports-api.lolesports.com/persisted/gw/getEventDetails?Id={0}&hl=en-US".format(
        eventID
    )

    return request(url)


def getGames(gameID=""):
    url = "https://esports-api.lolesports.com/persisted/gw/getGames?id={}&hl=en-US".format(
        gameID
    )

    return request(url)
