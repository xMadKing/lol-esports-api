from lol_esp_api.apis.supfunc import request


# this works with either slug or team Id.
def getTeams(slug=""):
    if slug == "":
        url = "https://esports-api.lolesports.com/persisted/gw/getTeams?hl=en-US"
    else:
        url = "https://esports-api.lolesports.com/persisted/gw/getTeams?id={}&hl=en-US".format(
            slug
        )

    return request(url)


# this works with either slug or team Id.
def getTeamPlayers(slug):
    response = getTeams(slug)
    players = response["data"]["teams"][0]["players"]

    return players


def getTeamId(slug):
    response = getTeams(slug)
    teamID = response["data"]["teams"][0]["id"]

    return teamID


def getTeamSlug(id):
    response = getTeams(id)
    teamSlug = response["data"]["teams"][0]["slug"]

    return teamSlug


# this works with either slug or team Id.
def getTeamImgUrl(slug):
    response = getTeams(slug)
    teamImgUrl = response["data"]["teams"][0]["image"]

    return teamImgUrl


# this works with either slug or team Id.
def getTeamCode(slug):
    response = getTeams(slug)
    teamCode = response["data"]["teams"][0]["code"]

    return teamCode
