import requests


# LEAGUES API

def getLeagues():
    url = "https://esports-api.lolesports.com/persisted/gw/getLeagues?hl=en-US"

    response = requests.get(url, headers={'x-api-key':'0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'})
    json = response.json()
    
    return json

def getTournamentsForLeague(leagueID):
    results = []

    url = "https://esports-api.lolesports.com/persisted/gw/getTournaments?hl=en-US"

    response = requests.get(url, headers={'x-api-key':'0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'})
    json = response.json()

    if not isinstance(leagueID, str):
        leagueID = str(leagueID)

    for i in range(0, len(json['data']['tournaments'])):
        if json['data']['tournaments'][i]['leagueId'] == leagueID:
            results.append(json['data']['tournaments'][i])

    return results

def getStandings(tournamentID):
    url = "https://esports-api.lolesports.com/persisted/gw/getStandings?hl=en-US"

    response = requests.get(url, headers={'x-api-key':'0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'})
    json = response.json()

    return json

