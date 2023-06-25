from lol_esp_api.apis.supfunc import request

def getWindow(gameID="", startingTime="", participantIds=""):
    url = "https://feed.lolesports.com/livestats/v1/window/{0}?startingTime={1}&participentId={2}".format(
        gameID, startingTime, participantIds
    )

    return request(url)


def getDetails(gameID, startingTime="", participantIds=""):
    url = "https://feed.lolesports.com/livestats/v1/details/{0}?startingTime={1}&participentId={2}".format(
        gameID, startingTime, participantIds
    )

    return request(url)
