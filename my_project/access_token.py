# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Define your Fyers API credentials
client_id = "P03A2KTUG1-100"
secret_key = "Q778A7Z33H"
redirect_uri = "Https://www.google.com"
response_type = "code"  
grant_type = "authorization_code"  

# The authorization code received from Fyers after the user grants access
auth_code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE3MTY5Nzk0MjIsImV4cCI6MTcxNzAwOTQyMiwibmJmIjoxNzE2OTc4ODIyLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYQTQ4Njk0Iiwib21zIjoiSzEiLCJoc21fa2V5IjoiMDhmMmEyM2ZlMTI3MTMyNTc0NzJiZTA0NmRmZGUwMDg2MGEzMGZjZWM2YTFkNWUxNDY4ZjM2NmYiLCJub25jZSI6IiIsImFwcF9pZCI6IlAwM0EyS1RVRzEiLCJ1dWlkIjoiNmFlMmQzOGY5MzRmNDdkOWI3YjFhNDEwZmQxNDkyYTMiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.M1jblumZ2gYBMIB72dwOEQISiWYVuf4rLZEnViYJSac"

# Create a session object to handle the Fyers API authentication and token generation
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key, 
    redirect_uri=redirect_uri, 
    response_type=response_type, 
    grant_type=grant_type
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token()

# Print the response, which should contain the access token and other details
print(response)

