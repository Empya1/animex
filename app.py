import os
from flask import Flask, render_template
from functools import partial
import requests
from appdata import *


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

render = partial(render_template, tag=multitag, banners=banners, interstitial=interstitial, vignette=vignette, facebook_link=fb_link, whatsapp_link=wa_link, twitter_link=x_link)


@app.route("/")

def index(): 
      
      try:
            response = request_updates()
            
      except Exception as e:
            response = {}
            response["data"] = []
            response["status"] = "error"
            response["message"] = str(e)
            
      updates = response["data"]
      status = response["status"]
            
      return render("index.html", updates=updates, status=status)
      
      
def request_updates(url=API_URL): 

      response = requests.get(url+GET)
      
      return response.json()
      
