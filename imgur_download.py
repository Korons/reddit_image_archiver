import sys
import re
import urllib.request, urllib.parse, urllib.error, urllib
import os
import math


SUBREDDITS='/home/wil/.config/imgur_down/subreddits.txt'
with open(SUBREDDITS) as f:
	lines = f.read().splitlines()
for i in lines:
	url = "https://reddit.com/r/" + i + ".json"
	req = urllib.request.Request(
    url, 
    headers={'User-Agent': "abotbyineedmorealts"}
	)
	print (url)
	reddit_call = urllib.request.urlopen(req)
	result = reddit_call.read().decode('utf-8')
	results = re.findall('http://imgur.com/a......', result)
	for u in results:
		os.system("mkdir -p /home/wil/Pictures/Imguralbums/" + i)
		os.chdir("/home/wil/Pictures/Imguralbums/" + i)
		os.system("imgurdl " + u)
