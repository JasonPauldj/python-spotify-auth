from django.shortcuts import render, redirect
from django.http import HttpResponse
from urllib.parse import urlencode
import requests
import base64
import os


redirect_uri='http://localhost:8000/callback/spac'
client_id=os.environ.get('CLIENT_ID')
client_secret=os.environ.get('CLIENT_SECRET')
access_token=None
refresh_token=None

def spotify_authorize(request):
    base_url='https://accounts.spotify.com/authorize'
    query={'client_id': '0c52eb31f65e4d229ba147a9fc9b8e7c','response_type':'code','redirect_uri': redirect_uri, 'scope' : 'user-read-private user-read-email'}
    query_string=urlencode(query);

    url='{}?{}'.format(base_url,query_string)
    return redirect(url)

def spotify_accesstoken(request):
    base_url= 'https://accounts.spotify.com/api/token'
    data={
        'grant_type':'authorization_code',
        'code':request.GET.get('code'),
        'redirect_uri':redirect_uri
    }

    message = f"{client_id}:{client_secret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')
    headers={
        'content_type':'application/x-www-form-urlencoded',
        'Authorization': f"Basic {base64Message}"
    }
    if request.method=='GET':
        print('in GET of spotify access token')
        response = requests.post(base_url,data=data, headers=headers)
        data = response.json()
        global access_token
        access_token=data['access_token']
        global refresh_token
        refresh_token=data['refresh_token']
        return HttpResponse(response)

def spotify_user(request):
     base_url='https://api.spotify.com/v1/me'
     global access_token
     print(access_token)
     headers={
        'content_type':'application/json',
        'Authorization': f"Bearer {access_token}"
     }
     if request.method=='GET':
        print('in GET of spotify user')
        response = requests.get(base_url, headers=headers)
        data = response.json()
        return HttpResponse(response)

def spotify_user_playlists(request):
     base_url='https://api.spotify.com/v1/me/playlists'
     global access_token
     print(access_token)
     headers={
        'content_type':'application/json',
        'Authorization': f"Bearer {access_token}"
     }
     if request.method=='GET':
        print('in GET of spotify user playlist')
        response = requests.get(base_url, headers=headers)
        data = response.json()
        return HttpResponse(response)


