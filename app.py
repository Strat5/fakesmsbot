import os							#setup packages and variables
import sys
import json
from flask import Flask, request
import requests
app = Flask(__name__)
import sms_script as script
import war_data as war

@app.route('/', methods=['POST'])	#clients feed this endpoint
def webhook():
	data = request.get_json()
	keyword = data["keyword"]
	log('The keyword "{}" was receieved.'.format(keyword))
	if keyword == 'end':
		message = 'That is not a recognized keyword. Text END to end this program. Text TEEN to restart it.'
	elif keyword.upper() in script.keywords:
		message = 'SmokefreeTXT: ' + script.keywords[keyword.upper()]
	else: 
		message = 'That is not a recognized keyword. Text END to end this program. Text TEEN to restart it.'
	return message, 200

def log(msg): 
	print(str(msg))
	sys.stdout.flush()
