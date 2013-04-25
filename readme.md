Requirements:

python 2.7.3
mplayer

```pip install -r requirements.txt```

This was done for an assignment as part of the University of Virginia's Software Testing Course.  
This project takes in a youtube url, or local file depending on the arguments passed to the main python script, downloads, and plays it.

* It also optionally takes in the seek parameter if you would like to skip to a certain part of the video.
* It also optionally takes in the osd parameter if you would like to see the current playing time.

* Credit to rg3 of youtube-dl for the use of youtube-dl and the regex validing youtube links.

```python py-mplayer.py --youtube YOUTUBEURL --seek 10 --osd 2```
