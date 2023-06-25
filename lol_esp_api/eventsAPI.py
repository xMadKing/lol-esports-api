from supfunc import request


def getSchedule(leagueID, PageToken=""):
    url = (
        "https://esports-api.lolesports.com/persisted/gw/getSchedule?leagueId={0}&PageToken={1}"
        "&hl=en-US".format(leagueID, PageToken)
    )

    return request(url)


def getLive():
    url = "https://esports-api.lolesports.com/persisted/gw/getLive?hl=en-US"

    return request(url)


def getCompeletedEvents(eventID=""):
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
