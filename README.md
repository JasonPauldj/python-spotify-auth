# python-spotify-auth
For anyone who is interested, you can follow the below steps after cloning the repo to see it in action
Steps to follow:
- Create an app in https://developer.spotify.com/
- While creating an app specify the redirect uri as http://localhost:8000/callback/spac in the settings
- Create environment variables called CLIENT_ID and CLIENT_SECRET and set it to the values you get in the dashboard in https://developer.spotify.com/
- Set up your MS SQL database and change the password and Name in settings.py as per your database name and password
- cd into the project folder and run the below command to create a virtual environment
```
python -m venv virtualenvironmentname
```
- For MAC users, run the below command to activate the virtual environment
```
source virtualenvironmentname/bin/activate
```
- Install the packages in requirements.txt by running the command
```
pip3 install -r ./requirements.txt
```
- Run the command to start the server
```
python manage.py runserver
```
- If no error is thrown, then open your browser and hit the endpoint http://localhost:8000/login
- Enter in your spotify details and log in
- Next hit the endpoint http://localhost:8000/user/data
- Next hit the endpoint http://localhost:8000/user/playlists

## API Flow
1. First hit http://localhost:8000/login. The view for this endpoint does the following: 
  - User will be redirected to the url 'https://accounts.spotify.com/authorize'
  - queryparams passed
    - client_id
    - response_type
    - redirect_uri
    - scope
2. Once the user grants his permission, he is redirected to the specified redirect_uri which is the same as what is mentioned in the App in Spotify Developer portal. The redirect_uri will be having a query parameter called 'code' which needs to be exchanged for a access token.
The view for the endpoint http://localhost:8000/callback/spac does the following:
  - Hits the endpoint 'https://accounts.spotify.com/api/token'
  - We capture the access_token and refresh_token from the response
  - We use the access_token to hit other spotify endpoints
  - We need the refresh_token to obtain a new access_token every 60 minutes.
