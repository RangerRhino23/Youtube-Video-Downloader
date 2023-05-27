from youtube_search import YoutubeSearch
from pytube import YouTube
import time

###HOW TO USE###
#MAKE SURE videos.csv IS EMPTY BEFORE STARTING!!!!!
#put youtube prompts in youtube_prompts.csv
#python youtube_search_to_download.py

#Opens file where video link will be stored
file_download = open('videos.csv', 'a')


def youtube_search():
    #Opens video search prompts and searches youtube for video
    with open('youtube_prompts.csv', 'r') as file:
        for line in file:
            results = YoutubeSearch(line, max_results=1).to_dict()
            video = results[0]
            
            video_file = f"https://www.youtube.com/watch?v={video['id']}"

            file_download.write(video_file+'\n')
    file_download.close()


def download_videos():
    #Opens file where vidoe links are stored and downloads them
    with open("videos.csv", "r") as file:
        for line in file:
            yt = YouTube(line)
            #print("Title: ", yt.title)
            #print("Views: ", yt.views)
            yd = yt.streams.get_highest_resolution()

            yd.download('./Downloaded Videos')
    file.close()


print("Starting Youtube Search...")
youtube_search()
print("Done!")
time.sleep(1)
print("Starting Downloading Videos...")
download_videos()
print("Done!")