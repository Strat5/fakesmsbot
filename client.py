import os
import signal
import requests
import pyperclip
confirmation='N'
keyword = ''

while confirmation=='N':
	keyword = input('Enter the keyword: ')
	print ('Received input was: "{}", is that correct?'.format(keyword))
	confirmation = input('Y or N ').upper()

url = 'https://fakesmsbot.herokuapp.com/'
data = {'keyword':keyword}
r = requests.post(url, json=data)
print(r)
pyperclip.copy(r.text)