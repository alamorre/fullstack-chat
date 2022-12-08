from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
import os, requests

app = Flask(__name__)
CORS(app)
load_dotenv()

@app.route('/login', methods=['POST'])
def login():
    response = requests.get('https://api.chatengine.io/users/me/', 
        headers={ 
            "Project-ID": os.environ['CHAT_ENGINE_PROJECT_ID'],
            "User-Name": request.get_json()['username'],
            "User-Secret": request.get_json()['secret']
        }
    )
    return response.json()

@app.route('/signup', methods=['POST'])
def signup():
    response = requests.post('https://api.chatengine.io/users/', 
        data={
            "username": request.get_json()['username'],
            "secret": request.get_json()['secret'],
            "email": request.get_json()['email'],
            "first_name": request.get_json()['first_name'],
            "last_name": request.get_json()['last_name'],
        },
        headers={ "Private-Key": os.environ['CHAT_ENGINE_PRIVATE_KEY'] }
    )
    return response.json()