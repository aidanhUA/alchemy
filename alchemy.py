from flask import Flask, request
from os import environ, path
from dotenv import load_dotenv

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG')
SPOTIFY_TOKEN_API = 'https://accounts.spotify.com/api/token'
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    print("This is COOL")


@app.route('/spotify-client-id', methods=['POST'])
def get_client_id():
    app.logger.info('Retrieved Spotify Client ID')
    return {'spotify_client_id': environ.get('SPOTIFY_CLIENT_ID')}


@app.route('/spotify-callback', methods=['GET'])
def handle_spotify_callback():
    try:
        code = request.args.get('code')
        print(code)

        # Return a message to go back to the site.
        return 'Hello'
    except ValueError:
        app.logger.info('Spotify login unsuccessful')

