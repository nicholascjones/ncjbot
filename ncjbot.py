## ncjbot.py
## Basic IRC chat bot
## author: nicholascjones
## takes some ideas from Peter Bui's Bobbit https://bitbucket.org/pbui/bobbit
## also borrows some from http://archive.oreilly.com/pub/h/1968


import sys
import json
import os
import socket
import signal
import time
import json
import random
import requests

from slackclient import SlackClient

#constant variables

OWNER = "nicholascjones"
#HOST = 'slack.com'
NICK = "notnickjones"
PORT = 6667
TOKEN = 'xoxb-25750572867-S8sB4KyTypsBhWV6x77QRHVF'
readbuffer=""
CHAN = "#lug"

sc = SlackClient(TOKEN)
if sc.rtm_connect():
	while True:
		print sc.rtm_read()
		time.sleep(1)
		break
else:
	print "Connection Failed, invalid token?"

print sc.api_call("api.test")
hey = "Um...why am I here again?"
print sc.api_call("chat.postMessage", token=TOKEN, username=NICK, as_user='true', channel=CHAN, text=hey)
#print sc.api_call('chat.postMessage', token=TOKEN,  username=NICK, icon_emoji=':ghost:', as_user='true', channel='CHAN', text='Hello World!')






