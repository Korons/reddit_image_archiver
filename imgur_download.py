import sys
import re
import urllib.request, urllib.parse, urllib.error, urllib
import os
import time
import string
import random
home = os.getenv("HOME")
downloaded = home + '/.config/imgur_down/downloaded.txt'
SUBREDDITS = home + '/.config/imgur_down/subreddits.txt'
logfile = home + '/Pictures/Imguralbums/log.txt'
with open(SUBREDDITS) as f:
	lines = f.read().splitlines()
	print (lines)
for i in lines:
	url = "https://reddit.com/r/" + i + ".json"
	req = urllib.request.Request(
    url, 
    # The user-agent we send so we don't get massively limited
    headers={'User-Agent': "abotbyATGUNAT"}
	)
	print (url)
	reddit_call = urllib.request.urlopen(req)
	result = reddit_call.read().decode('utf-8')
	results = re.findall('https?://imgur.com/a......', result)
	for image_url in results:
		# This can and should be changed to a os.mkdir
		os.system("mkdir -p " + home + "/Pictures/Imguralbums/" + i)
		os.chdir(home + "/Pictures/Imguralbums/" + i)
		if image_url not in open(downloaded).read():
			os.system("imgurdl " + image_url)
			# We write the downloaded url to a file so we can quickly skip already downloaded files
			f = open(downloaded,'a')
			f.write(image_url + '\n')
			f.close()
	result = result.replace('"','')
	# This regex is from https://stackoverflow.com/questions/169625/regex-to-check-if-valid-url-that-ends-in-jpg-png-or-gif
	direct_links = re.findall('https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg|gif|png|jpeg|gifv)', result)
	for d_image_url in direct_links:
		char_set = string.ascii_uppercase + string.digits
		randstring = ''.join(random.sample(char_set*6, 6))
		os.system("mkdir -p " + home + "/Pictures/Imguralbums/" + i)
		if not re.findall('https?://i.redditmedia.com/............................................jpg', d_image_url) and not re.findall('https?://..thumbs.redditmedia.com/............................................jpg', d_image_url) and d_image_url not in open(downloaded).read():
			print ('Downloading\n 	' + d_image_url + ' in ' + os.getcwd() + '\n')
			# All the trys here are for 403 errors, I'm assuming becuase I haven;t hit a 403 since putting them in that they work.
			if d_image_url[-3:] == 'jpg':
				try:
					urllib.request.urlretrieve(d_image_url, home + '/Pictures/Imguralbums' + '/' + i +'/' + randstring +'.jpg')
				except Exception:
					pass
			elif d_image_url[-3:] == 'png':
				try:
					urllib.request.urlretrieve(d_image_url, home + '/Pictures/Imguralbums' + '/' + i +'/' + randstring +'.png')
				except Exception:
					pass
			elif d_image_url[-3:] == 'gif':
				try:
					urllib.request.urlretrieve(d_image_url, home + '/Pictures/Imguralbums' + '/' + i +'/' + randstring +'.gif')
				except Exception:
					pass
			elif d_image_url[-4:] == 'gifv':
				try:
					urllib.request.urlretrieve(d_image_url, home + '/Pictures/Imguralbums' + '/' + i +'/' + randstring +'.gifv')
				except Exception:
					pass
			elif d_image_url[-4:] == 'jpeg':
				try:
					urllib.request.urlretrieve(d_image_url, home + '/Pictures/Imguralbums' + '/' + i +'/' + randstring +'.jpeg')
				except Exception:
					pass
			print ('Done\n')
			f = open(downloaded,'a')
			f.write(d_image_url + '\n')
			f.close()
print ('debug')
for i in lines:
	os.chdir(home + "/Pictures/Imguralbums/" + i)
	# These system calls seem to hang the program some times no idea why
	os.system('for i in */; do zip -r "${i%/}.cbr" "$i" -x *.cbr; done')
	os.system('rm -r */')
	# Logging 
	# time = time.strftime("%H:%M:%S:%d/%m/%Y")
	# f = open(logfile,'r+')
	# f.write(("Ran at " + time))
	# f.close
