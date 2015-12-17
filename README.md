# reddit-imgur-download
This is a bash script which uses imguralbum.py from https://github.com/alexgisby/imgur-album-downloader to download all imgur albums from the front page of subreddits

## Usage

Make a file with the list of subreddits you want to download imgutalbums from and replace the following line in the script with the path to your file

    SUBREDDITS=~/.config/imgur_down/subreddits.txt
    
    
After you do that you can set a cron job for the script and it will download all imgur albums from the front pages of the subreddits you specified
