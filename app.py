import os
import json
from flask import Flask, request
import requests

@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	keyword = data['keyword']
	log(('Keyword is: {}'.format(keyword))


def log(msg): 
	print(str(msg))
	sys.stdout.flush()
