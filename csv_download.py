from pytube import YouTube

###HOW TO USE###
#put youtube links in videos.csv
#python csv_download.py

def csv_download(option):
    with open("videos.csv", "r") as file:
        for line in file:
            yt = YouTube(line)
            #print("Title: ", yt.title)
            #print("Views: ", yt.views)

            if option == 'audio':
                yd = yt.streams.filter(only_audio=True).first()
            elif option == 'both':
                yd = yt.streams.get_highest_resolution()

            yd.download('./Downloaded Videos')

if __name__ == '__main__':
    csv_download('both')