# python-spotify-auth
For anyone who is interested, you can follow the below steps after cloning the repo to see it in action
Steps to follow:
- Create an app in https://developer.spotify.com/
- While creating an app specify the redirect uri as http://localhost:8000/callback/spac in the settings
- Create environment variables called CLIENT_ID and CLIENT_SECRET and set it to the values you get in the dashboard in https://developer.spotify.com/
- Install the packages in requirements.txt using pip
- Set up your MS SQL database and change the password and Name in settings.py as per your database name and password(After the steps, I have included my database settings for reference)
- cd into the project folder and run the command python manage,py runserver
- If no error is thrown, then open your browser and hit the endpoint http://localhost:8000/login
- Enter in your spotify details and log in
- Next hit the endpoint http://localhost:8000/user/data
- Next hit the endpoint http://localhost:8000/user/playlists
