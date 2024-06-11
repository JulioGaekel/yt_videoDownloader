# ytDownloader.py - This program will be able to download a YouTube video by using the command line.

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print('Title: ', yt.title)
print('Views: ', yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/juliogaekel/Documents/youtubeVideos')

#TODO: Add error handling (try-except) and print any errors that occur during the download process
#TODO: Add feature optional path, if nothing is declared, have default path.
#TODO: Validate that the path exists, if it does exist, it should create it.
#TODO: Organize code. Devide into functions and add main function.
#TODO: Add comments and refactor for better readability.