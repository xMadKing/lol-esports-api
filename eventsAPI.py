import requests


def getSchedule(leagueID="", pageToken=""):
    url = (
        "https://esports-api.lolesports.com/persisted/gw/getSchedule?leagueId={0}&pageToken={1}"
        "&hl=en-US".format(leagueID, pageToken)
    )

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json


def getLive():
    url = "https://esports-api.lolesports.com/persisted/gw/getLive?hl=en-US"

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json


def getCompeletedEvents(eventID=""):
    url = "https://esports-api.lolesports.com/persisted/gw/getCompletedEvents?tournamentId={0}&hl=en-US".format(
        eventID
    )

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json

def getEventDetails(eventID):
    url = "https://esports-api.lolesports.com/persisted/gw/getEventDetails?Id={0}&hl=en-US".format(eventID)

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json

def getGames(gameID=""):
    url = "https://esports-api.lolesports.com/persisted/gw/getGames?id={}&hl=en-US".format(gameID)

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json

print(getSchedule(98767991299243165))