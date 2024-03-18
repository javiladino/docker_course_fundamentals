import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Javier",
        "lastname": "Ladino",
        "socialMedia":
        [
            {"facebookUser": "ladino22"},
            {"instagramUser": "javierladino"},
            {"xUser": "javierladino"},
            {"linkedin": "jladino"},
            {"githubUser": "javiladino"}
        ],
        "blog": "https://www.javierladino.com",
        "author": "Javier Ladino"
    }
    return json.dumps(value)