from pytube import YouTube
from sys import argv

###HOW TO USE###
#python download_link.py (youtube link)

link = argv[1]
yt = YouTube(link)

#print("Title: ", yt.title)

#print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()


yd.download('./Downloaded Videos')