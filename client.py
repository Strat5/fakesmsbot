import os
import signal
import requests
import pyperclip
import webbrowser

keyword = input('Enter the keyword: ')
if(keyword == 'WAR_FILES'):
	keyword = input('Please enter the Document ID: ')
	if(keyword == 'backup_communication'):
		url = 'https://docs.google.com/document/d/1_CUCJjSI2kxA984FsZSq4gLT4Xr1r8XMWQcuXHLNX60/edit?usp=sharing'
		webbrowser.open_new(url)
	elif(keyword == 'declaration_of_war'):
		keyword = input("Are you sure you want to view this? It may be too intimidating for you.")
		url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
		webbrowser.open_new(url)
	exit()

url = 'https://fakesmsbot.herokuapp.com/'
data = {'keyword':keyword}
r = requests.post(url, json=data)
pyperclip.copy(r.text)
print(r)