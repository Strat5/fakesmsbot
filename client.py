import os
import signal
import requests
import pyperclip
loop = true
while loop:
	keyword = input('Enter the keyword: ')
	url = 'https://fakesmsbot.herokuapp.com/'
	data = {'keyword':keyword}
	r = requests.post(url, json=data)
	pyperclip.copy(r.text)
	print(r)