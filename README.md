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
