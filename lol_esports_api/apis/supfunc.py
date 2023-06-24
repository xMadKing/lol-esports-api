import requests
import requests_cache

requests_cache.install_cache('api_cache', expire_after=(60*15))


def request(url):
    response = requests.get(
        url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
    )

    return response.json()
