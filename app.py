import os
import json
from flask import Flask, request
import requests

@app.route('/', methods=['POST'])	#messages from GroupMe chats land here
def webhook():
	data = request.get_json()