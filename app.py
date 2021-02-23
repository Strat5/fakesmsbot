import os							#setup packages and variables
import json
from flask import Flask, request
import requests
app = Flask(__name__)


@app.route('/', methods=['POST'])	#clients feed this endpoint
def webhook():
	data = request.get_json()
	keyword = data["keyword"]
	log(keyword)
	return "ok", 200

def log(msg): 
	print(str(msg))
	sys.stdout.flush()