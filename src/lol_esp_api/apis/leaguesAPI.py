from lol_esp_api.apis.supfunc import request

def getLeagues():
    url = "https://esports-api.lolesports.com/persisted/gw/getLeagues?hl=en-US"

    return request(url)

def getLeagueBySlug(slug):
    response = getLeagues()
    leagues = response['data']['leagues']

    for league in leagues:
        if league['slug'] == slug:
            return league
        
    return "league not found"

def getLeagueById(id):
    response = getLeagues()
    leagues = response['data']['leagues']

    for league in leagues:
        if league['id'] == id:
            return league
        
    return "league not found"

def getTournamentsForLeague(leagueID):
    url = "https://esports-api.lolesports.com/persisted/gw/getTournamentsForLeague?leagueId={0}&hl=en-US".format(
        leagueID
    )

    return request(url)

def getTournaments():
    url = "https://esports-api.lolesports.com/persisted/gw/getTournaments?hl=en-US"

    return request(url)

def getTournamentById(id):
    response = getTournaments()
    tournaments = response['data']['tournaments']

    for tournament in tournaments:
        if tournament['id'] == id:
            return tournament
        
    return "Tournament not found!"

def getTournamentBySlug(slug):
    response = getTournaments()
    tournaments = response['data']['tournaments']

    for tournament in tournaments:
        if tournament['slug'] == slug:
            return tournament
        
    return "Tournament not found!"

def getStandings():
    url = "https://esports-api.lolesports.com/persisted/gw/getStandings?hl=en-US"

    return request(url)

def getStandingsBy_TID(tournamentID):
    url = "https://esports-api.lolesports.com/persisted/gw/getStandings?tournamentId={0}&hl=en-US".format(
        tournamentID
    )

    return request(url)

def getStandingsByStage(TournamentID, stage_slug):
    response = getStandingsBy_TID(TournamentID)
    stages = response['data']['standings'][0]['stages']

    for stage in stages:
        if stage['slug'] == stage_slug:
            return stage

    return "Standings not found!"