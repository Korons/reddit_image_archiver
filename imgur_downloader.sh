#!/bin/bash
now=$(date +%Y_%m_%d_%T)



#These are the subreddits you want to download imgur albums from
if [ "$1" == -h ]
	then
	printf "Help \n\n -lo 	 Get links but do not download \n -l 	 Logs time when ran\n"
	exit
fi
subreddits=() # The subreddits you want to download from go here
for i in "${subreddits[@]}"
do
	echo "$i"
curl https://www.reddit.com/r/"$i".json >> /tmp/reddit_json
grep -o  "http://imgur.com/a......" /tmp/reddit_json >> /tmp/links.txt
grep -o  "https://imgur.com/a......" /tmp/reddit_json >> /tmp/links.txt
done
#This changes http to https 
sed -i 's/https/http/g' /tmp/links.txt
sed -i 's/http/https/g' /tmp/links.txt
# This puts each link on a newline
awk '{ for (i=1;i<=NF;i++) print $i }' /tmp/links.txt
#Passing the script -lo only gets the links but does not download them
if [ "$1" == -lo ]; then
cat /tmp/links.txt >> ~/imgur_links
rm /tmp/links.txt
rm /tmp/reddit_json
exit
fi
cd ~/Pictures/Imguralbums
while read line;
	do
	 torsocks imguralbum.py "$line" 
done < /tmp/links.txt
# Logs when/if it ran
if [ "$1" == -l ]
	then
	touch ~/imgur_log
	echo "Ran at $now" >> ~/imgur_log
fi
rm /tmp/links.txt
rm /tmp/reddit_json
