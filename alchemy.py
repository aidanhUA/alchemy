from flask import Flask, request
from os import path
from dotenv import load_dotenv
import requests
import utilities

app = Flask(__name__)
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    print("This is COOL")


@app.route('/spotify-client-id', methods=['POST'])
def get_client_id():
    app.logger.info('Retrieved Spotify Client ID')
    return utilities.get_spotify_client_id()


@app.route('/spotify-login-callback', methods=['GET'])
def handle_spotify_login_callback():
    try:
        code = request.args.get('code')
        app.logger.info('Received Spotify Auth Code')
    except ValueError:
        app.logger.info('Spotify login unsuccessful')

    try:
        token_payload = utilities.get_spotify_access_tokens(code)
    except requests.HTTPError as e:
        return 'That did not work as planned. Try it again maybe?'

    try:
        users_top_read = utilities.get_users_top_read(token_payload['access_token'])
    except requests.HTTPError as e:
        return 'For some reason I can not get your top artists from Spotify. ' \
               'This usually happens if you listen to a lot of Celine Dion'

    ### HERE WE COMPARE TO MY DATA ###
    return 'Thanks, we got it!'
