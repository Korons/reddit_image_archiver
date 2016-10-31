# reddit-imgur-download
This is a python script which downloads media from the front page of subreddits
(jpg, jpeg, png, gif, gifv and mp4 (from gfycat)) currently

## Set up
Put [imgur-album-downloader](https://github.com/alexgisby/imgur-album-downloader) in your path as imgurdl

    sudo mv imguralbum.py /usr/bin/imgurdl

And run setup.sh

    ./setup.sh

### Or to do everything by hand

Make a folder called Imguralbums in ~/Pictures

    mkdir ~/Pictures/Imguralbums

Make a folder called imgur_down in ~/.config

    mkdir ~/.config/imgur_down

Then make a file called subreddits.txt in imgur_down and a file call downloaded.txt

    touch downloaded.txt
    touch subreddits.txt
    touch log.txt

Enter the name of the sub reddits you want to download from in subreddits.txt. You only need the subreddit name not the full url.

The script will download all imguralbums from the front page of those subreddits and save the images to ~/Pictures/Imguralbums/SUBREDDIT/RANDOMSTRING/

It will also download all dot jpg, png and gif files from those posts on those subreddits and save them to ~/Pictures/Imguralbums/SUBREDDIT/RANDOMSTRING.PNG|JPG|GIF

And then put them in .cbr archives so they can be read with the comic reader of your choice, meaning the end files with look like ~/Pictures/Imguralbums/SUBREDDIT/RANDOMSTRING.cbr

They can be view with any comic reader

## Usage

Add the subreddits you want to download from to ~/.config/imgur_down/subreddits.txt (1 per line)

Run the program with

```python3 imgur_download.py```

To log the number of files downloaded and their type add the -l option

```python3 imgur_download.py -l```


## WARNING

The program will compress and delete all folders in the ~/Pictures/Imguralbums/SUBREDDIT dir

## FAQ

### How do I run this on windows?

This was made to run on Linux based systems and it cannot be run on windows as it is.

### Why are some CBRs massive?

As far as I can tell this is a issue with the images not with the program.
