import requests

def getSchedule(leagueID, pageToken):
    url = "https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=en-US"

    response = requests.get(url, headers={'x-api-key':'0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'})
    json = response.json()

    return json
