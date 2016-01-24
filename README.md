# reddit-imgur-download
This is a bash script which uses imguralbum.py from https://github.com/alexgisby/imgur-album-downloader to download all imgur albums from the front page of subreddits

## Usage
Put imgur-album-downloader in your path as imgurdl

    sudo mv imguralbum.py /usr/bin/imgurdl

Then make a folder called imgur_down in ~/.config

    mkdir ~/.config/imgur_down
    
Then make a file called subreddits.txt in imgur_down

    nano subreddits.txt

And enter the name of the sub reddits you want to download from. You only need the subreddit name not the full url.

The script will download all imguralbums from the front page of those subreddits and save the images to ~/Pictures/Imguralbums/SUBREDDIT/RANDOMSTRING
    
