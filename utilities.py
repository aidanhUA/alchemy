import requests
from os import environ
import json
SPOTIFY_TOKEN_API = 'https://accounts.spotify.com/api/token'
SPOTIFY_USERS_ARTISTS_API = 'https://api.spotify.com/v1/me/top/artists'
ACCESS_TOKEN_REDIRECT = '/access_token_callback'


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def get_spotify_access_tokens(code):
    data = {
        "redirect_uri": {environ.get("HOME_BASE_URL")} + ACCESS_TOKEN_REDIRECT,
        "code": code,
        "grant_type": "authorization_code"
    }
    resp = requests.post(SPOTIFY_TOKEN_API, data=data,
                         auth=(environ.get('SPOTIFY_CLIENT_ID'), environ.get('SPOTIFY_CLIENT_SECRET')))
    return json.loads(resp)


def get_spotify_client_id():
    return {'spotify_client_id': environ.get('SPOTIFY_CLIENT_ID')}


def get_users_top_read(access_token, limit):
    url = f'{SPOTIFY_USERS_ARTISTS_API}?time_range=long_term&limit={limit}'
    resp = requests.get(url, auth=BearerAuth(access_token))
    return json.loads(resp)

