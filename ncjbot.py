## ncjbot.py
## Basic IRC chat bot
## author: nicholascjones


import sys
import json
import os
import socket
import signal
import time
import json
import random
import requests
import re

from slackclient import SlackClient

#constant variables

OWNER = "nicholascjones"
#HOST = 'slack.com'
NICK = "notnickjones"
PORT = 6667
TOKEN = ''
readbuffer=""
CHAN = "ncj"

sc = SlackClient(TOKEN)
if sc.rtm_connect():
	#	time.sleep(1)
	print "Got it"
else:
	print "Connection Failed, invalid token?"

print sc.api_call("api.test")
hey = "I see they rebooted the student machine!"
print sc.api_call("chat.postMessage", token=TOKEN, username=NICK, as_user='true', channel=CHAN, text=hey)
#print sc.api_call('chat.postMessage', token=TOKEN,  username=NICK, icon_emoji=':ghost:', as_user='true', channel='CHAN', text='Hello World!')

while True:
	x = sc.rtm_read()
	for ev in x:
		print(ev)
		if "type" in ev:
			if ev["type"] == "message" and "text" in ev:
				message=ev["text"]
				if re.search(message, 'notnickjones'):
					print sc.api_call("chat.postMessage", token=TOKEN, username=NICK, as_user='true', channel=CHAN, text='What do you want?')




