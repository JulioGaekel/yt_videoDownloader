# ytDownloader.py - This program will be able to download a YouTube video by using the command line.

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print('Title: ', yt.title)
print('Views: ', yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/juliogaekel/Documents/youtubeVideos')
