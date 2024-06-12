from flask import Flask, request, redirect
from fyers_apiv3 import fyersModel

app = Flask(__name__)

# Replace these values with your actual API credentials
client_id = "P03A2KTUG1-100"
secret_key = "Q778A7Z33H"
redirect_uri = "Https://www.google.com"  # Replace this with your callback URL

# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type="code"
)

# Route to initiate the authentication flow
@app.route('/login')
def login():
    auth_url = session.generate_authcode()
    return redirect(auth_url)

# Route to handle the callback from FYERS after authentication
@app.route('/callback')
def callback():
    auth_code = request.args.get('code')
    # Exchange the authentication code for an access token
    access_token = exchange_auth_code_for_token(auth_code)
    return f"Access token: {access_token}"

def exchange_auth_code_for_token(auth_code):
    token_endpoint = "https://api.fyers.in/auth/authorize"
    session.set_token(auth_code)
    response = session.generate_token()
    access_token = response.get('access_token')
    return access_token

if __name__ == '__main__':
    app.run(debug=True)
