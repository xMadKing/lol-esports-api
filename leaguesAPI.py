from supfunc import  request

def getLeagues():
    url = "https://esports-api.lolesports.com/persisted/gw/getLeagues?hl=en-US"

    return request(url)


def getTournamentsForLeague(leagueID):
    url = "https://esports-api.lolesports.com/persisted/gw/getTournamentsForLeague?leagueId={0}&hl=en-US".format(
        leagueID
    )

    return request(url)


def getStandings(tournamentID):
    url = "https://esports-api.lolesports.com/persisted/gw/getStandings?tournamentId={0}&hl=en-US".format(
        tournamentID
    )

    return request(url)


LCS = 98767991299243165
