import requests

def getTeams(slug=""):
    url = "https://esports-api.lolesports.com/persisted/gw/getTeams?id={}&hl=en-US".format(slug)

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json

