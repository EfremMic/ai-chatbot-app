from authlib.integrations.flask_client import OAuth
from flask import session, redirect, url_for
import os

class GoogleAuthService:
    def __init__(self, app):
        oauth = OAuth(app)
        app.config['GOOGLE_CLIENT_ID'] = os.getenv('GOOGLE_CLIENT_ID')
        app.config['GOOGLE_CLIENT_SECRET'] = os.getenv('GOOGLE_CLIENT_SECRET')
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        app.config['GOOGLE_DISCOVERY_URL'] = "https://accounts.google.com/.well-known/openid-configuration"
        
        self.google = oauth.register(
            name='google',
            client_id=app.config['GOOGLE_CLIENT_ID'],
            client_secret=app.config['GOOGLE_CLIENT_SECRET'],
            server_metadata_url=app.config['GOOGLE_DISCOVERY_URL'],
            client_kwargs={
                'scope': 'openid email profile'
            }
        )
    
    def login(self):
        redirect_uri = url_for('auth', _external=True)
        return self.google.authorize_redirect(redirect_uri)
    
    def logout(self):
        session.pop('user', None)
        return redirect(url_for('index'))
    
    def authorize(self):
        token = self.google.authorize_access_token()
        user_info = self.google.parse_id_token(token)
        session['user'] = user_info
        return redirect(url_for('chatbot'))
    
    def get_user(self):
        return session.get('user')
