import os							#setup packages and variables
import sys
import json
from flask import Flask, request
import requests
app = Flask(__name__)
import script

@app.route('/', methods=['POST'])	#clients feed this endpoint
def webhook():
	data = request.get_json()
	keyword = data["keyword"]
	log('The keyword "{}" was receieved.'.format(keyword))
	message = script.keywords[keyword]
	return message, 200

def log(msg): 
	print(str(msg))
	sys.stdout.flush()