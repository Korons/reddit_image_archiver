import sys
import re
import urllib.request, urllib.parse, urllib.error, urllib
import os
import string
import random
home = os.getenv("HOME")
downloaded = home + '/.config/imgur_down/downloaded.txt'
SUBREDDITS = home + '/.config/imgur_down/subreddits.txt'
logfile = home + '/.config/imgur_down/log.txt'
download_dir = home + '/Pictures/Imguralbums'

def image_down(url,ext):
	# All the trys here are for 403/404 errors
	try:
		urllib.request.urlretrieve(url, download_dir + '/' + i + '/' + randstring + ext)
	except Exception:
		print ("WARNING: There was an exception downloading from a direct link (likely a 403 or 404)\n")
		pass

with open(SUBREDDITS) as f:
	lines = f.read().splitlines()
	print (lines)
for i in lines:
	reddit_url = "https://reddit.com/r/" + i + ".json"
	req = urllib.request.Request(
    reddit_url, 
    # The user-agent we send so we don't get massively limited
    headers={'User-Agent': "abotbyATGUNAT"}
	)
	print (reddit_url)
	reddit_call = urllib.request.urlopen(req)
	result = reddit_call.read().decode('utf-8')
	results = re.findall('https?://imgur.com/a......', result)
	for image_url in results:
		# This can and should be changed to a os.mkdir
		os.system("mkdir -p " + download_dir + '/' + i)
		os.chdir(home + "/Pictures/Imguralbums/" + i)
		if image_url not in open(downloaded).read():
			os.system("imgurdl " + image_url)
			# We write the downloaded url to a file so we can quickly skip already downloaded files
			f = open(downloaded,'a')
			f.write(image_url + '\n')
			f.close()
	# We remove qoutes so the urls aren't qouted
	result = result.replace('"','')
	# This regex is from https://stackoverflow.com/questions/169625/regex-to-check-if-valid-url-that-ends-in-jpg-png-or-gif
	direct_links = re.findall('https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg|gif|png|jpeg|gifv)', result)
	# This regex with get all links to gfycat
	gfycat_links = re.findall('https?://gfycat.com/\w*', result)
	for gfy_links in gfycat_links:
		# DO NOT MOVE THE RANDSTRING. If you do it may only generate 1 random string and overwrite all downloaded files!
		char_set = string.ascii_uppercase + string.digits
		randstring = ''.join(random.sample(char_set*6, 6))
		# We need to get the mp4 from the link. We get the mp4 and not the gif to save on bandwidth
		# We need to request the mp4 from giant.gfycat.com instead of gfycat.com
		down_gfy_link = gfy_links.replace('gfycat.com','giant.gfycat.com')
		# This chanages http to https
		down_gfy_link = down_gfy_link.replace('http://','https://')
		down_gfy_link = down_gfy_link + '.mp4'
		if gfy_links not in open(downloaded).read():
			print (gfy_links)
			print ('Downloading\n 	' + down_gfy_link + ' in ' + download_dir + '/' + i + ' as ' + randstring + '\n')
			try:
				urllib.request.urlretrieve(down_gfy_link, download_dir + '/' + i + '/' + randstring +'.mp4')
			except Exception:
				print ("WARNING: There was an exception downloading from gfycat (likely a 403 or 404)\n")
				try:
					# Here we try to use the fat.gfycat.com server instead of the giant.gfycat.com. For some reason we get a 
					# 403 if we use the wrong one when we try the mp4
					down_gfy_link = down_gfy_link.replace('giant','fat')
					print ('Trying fat.gfycat.com\n')
					print ('Downloading\n 	' + down_gfy_link + ' in ' + download_dir + '/' + i + ' as ' + randstring + '\n')
					urllib.request.urlretrieve(down_gfy_link, download_dir + '/' + i +'/' + randstring +'.mp4')
				except Exception:
					# I'm not going to code all the back up servers right now because tracking them all down is a pain
					print ('fat.gfycat failed\n')
					pass
			print ('Done!\n\n')
			f = open(downloaded,'a')
			f.write(gfy_links + '\n')
			f.close()
	for d_image_url in direct_links:
		# DO NOT MOVE THE RANDSTRING. If you do it may only generate 1 random string and overwrite all downloaded files!
		char_set = string.ascii_uppercase + string.digits
		randstring = ''.join(random.sample(char_set*6, 6))
		os.system("mkdir -p " + home + "/Pictures/Imguralbums/" + i)
		# The d_image_url not in open(downloaded).read() is what keeps this from redownloading images
		# This stops us from downloading (some) thumbnails
		if not re.findall('https?://i.redditmedia.com/............................................jpg', d_image_url) and not re.findall('https?://..thumbs.redditmedia.com/............................................jpg', d_image_url) and d_image_url not in open(downloaded).read():
			print ('Downloading\n 	' + d_image_url + ' in ' + download_dir + '/' + i + ' as ' + randstring + '\n')
			if d_image_url[-3:] == 'jpg':
				image_down(d_image_url,'.jpg')
			elif d_image_url[-3:] == 'png':
				image_down(d_image_url,'.png')
			elif d_image_url[-3:] == 'gif':
				# Ext is the file extension
				# This checks if the gif is coming from imgur. If it is we change it from gif to mp4 to save on bandwidth
				#TODO clean this up
				try:
					if bool(re.search('https?://i.imgur.com/\w*.gif', d_image_url)) == True:
						d_image_url = d_image_url.replace('.gif','.mp4')
						image_down(d_image_url,'.mp4')
						d_image_url = d_image_url.replace('.mp4','.gif')
					else:
						image_down(d_image_url,'.gif')
				except Exception:
					print ("WARNING: There was an exception downloading from a direct link (likely a 403 or 404)\n")
					pass
			elif d_image_url[-4:] == 'gifv':
				image_down(d_image_url,'.gifv')
			elif d_image_url[-4:] == 'jpeg':
				image_down(d_image_url,'.jpeg')
			print ('Done\n')
			# We need to added downloaded urls to the list so we don't redownload them
			f = open(downloaded,'a')
			f.write(d_image_url + '\n')
			f.close()
for i in lines:
	if os.path.isdir(download_dir + '/' + i) == True:
		pass
	elif os.path.isdir(download_dir + '/' + i) == False:
		print ("WARNING: " + download_dir + '/' + i + ' does not exist\nExiting')
		sys.exit()
	os.chdir(download_dir + '/' + i)
	# These system calls seem to hang the program some times no idea why
	os.system('for i in */; do zip -r "${i%/}.cbr" "$i" -x *.cbr; done')
	os.system('rm -r */')
