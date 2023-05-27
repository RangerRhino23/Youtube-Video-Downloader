from youtube_search import YoutubeSearch
import os

###HOW TO USE###
#python youtube_search_link.py
#enter video prompt

def youtube_search(ytvideo):
    results = YoutubeSearch(ytvideo, max_results=1).to_dict()
    video = results[0]
    
    video_file = f"https://www.youtube.com/watch?v={video['id']}"

    os.system(f'python download_link.py {video_file} both')


if __name__ == '__main__':
    youtube_video = input("Youtube Search: ")
    youtube_search(youtube_video)