import requests

def getWindow(gameID="", startingTime="", participantIds=""):
    url = "https://feed.lolesports.com/livestats/v1/window/{0}?startingTime={1}&participentId={2}" \
    .format(gameID, startingTime, participantIds)

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json

def getDetails(gameID, startingTime="", participantIds=""):
    url = "https://feed.lolesports.com/livestats/v1/details/{0}?startingTime={1}&participentId={2}" \
    .format(gameID, startingTime, participantIds)

    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )
    json = response.json()

    return json
