import os
import signal
import requests
import pyperclip
import webbrowser
import time
def war_files():
	print('')
	print('You are now accessing property of the ------- Government.')
	print('Please allow time to secure the connection.')
	print('')
	time.sleep(5)
	codename = input('Give your assigned codename. ')
	pwd = input('Give your PIN: ')
	file = input('What is the file you need? ')
	url = 'https://fakesmsbot.herokuapp.com/wartime'
	data = {'codename':codename, 'pwd':pwd, 'file':file}
	r = requests.post(url, json=data)
	if r.text[0:5] == 'http':
		webbrowser.open_new(r.text)
		exit()
	else: 
		print(r.text)
		time.sleep(5)

print('')
keyword = input('Your next message will be added to your clipboard after you enter their latest one-word response: ')
if(keyword == 'WAR_FILES'):
	war_files()

else:
	url = 'https://fakesmsbot.herokuapp.com/'
	data = {'keyword':keyword}
	r = requests.post(url, json=data)
	pyperclip.copy(r.text)
	print(r)