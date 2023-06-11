import requests


def getLeagues():
    url = "https://esports-api.lolesports.com/persisted/gw/getLeagues?hl=en-US"

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json


def getTournamentsForLeague(leagueID):
    url = "https://esports-api.lolesports.com/persisted/gw/getTournamentsForLeague?leagueId={0}&hl=en-US".format(
        leagueID
    )

    print(url)

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json


def getStandings(tournamentID):
    url = "https://esports-api.lolesports.com/persisted/gw/getStandings?tournamentId={0}&hl=en-US".format(
        tournamentID
    )

    print(url)

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json


LCS = 98767991299243165
