import os
import signal
import requests
import pyperclip
import webbrowser
import time
def war_files():
	print('')
	print('You are now accessing property of the Operahouse Government.')
	print('Please allow time to secure the connection.')
	print('')
	time.sleep(5)
	codename = input('Give your assigned codename. ')
	pwd = input('Give your PIN: ')
	file = input('What is the file you need? ')
	url = 'https://fakesmsbot.herokuapp.com/war'
	data = {'codename':codename, 'pwd':pwd, 'file':file}
	r = requests.post(url, json=data)
	if r.text[0:4] == 'http':
		webbrowser.open_new(r.text)
		exit()
	else: 
		print(r.text)
		time.sleep(5)

print('')
keyword = input('Enter the keyword: ')
if(keyword == 'war_files'):
	war_files()

else:
	url = 'https://fakesmsbot.herokuapp.com/'
	data = {'keyword':keyword}
	r = requests.post(url, json=data)
	pyperclip.copy(r.text)
	print(r)
