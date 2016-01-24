#!/bin/bash
#THIS IS OUTDATED. use imgur_downloader.py
now=$(date +%Y_%m_%d_%T)
#These are the subreddits you want to download imgur albums from
if [ "$1" == -h ]
	then
	printf "Help \n\n -lo 	 Get links but do not download \n -l 	 Logs time when ran\n"
	exit
fi
SUBREDDITS=~/.config/imgur_down/subreddits.txt
while read line;
do
	curl https://www.reddit.com/r/"$line".json >> /tmp/reddit_json
done < "$SUBREDDITS"
grep -o  "http://imgur.com/a......" /tmp/reddit_json >> /tmp/links.txt
grep -o  "https://imgur.com/a......" /tmp/reddit_json >> /tmp/links.txt
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
while read line;
do
	sed -i 's@$line@ @g' /tmp/links.txt
done < ~/imgur_links
sort /tmp/links.txt | uniq > /tmp/links2.txt 
 cd ~/Pictures/Imguralbums
 while read line;
 	do
 	 imguralbum.py "$line" 
 done < /tmp/links2.txt
 cd ~/Pictures/Imguralbums
 for i in *; do zip -r "${i%/}.cbr" "$i" -x *.cbr; done
 rm -r */
  Logs when/if it ran
cat /tmp/links.txt >> ~/imgur_links
rm /tmp/links.txt
rm /tmp/reddit_json
echo "imgur_down ran at $now" >> ~/script_log
