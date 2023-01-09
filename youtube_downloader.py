from pytube import YouTube
import subprocess

urls = []

while True:
    url = input("Enter the YouTube URL (enter 'q' to finish): ")
    print('\n')
    if url == 'q':
        break
    urls.append(url)

# Download the videos one by one
for url in urls:
    youtube = YouTube(url)

    print("Title: ", youtube.title)

    print("Views: ", youtube.views) 

    ytd = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Your destination folders after downloading the video...to be changed according to your os.
    ytd.download('/Users/isaaccherry/Documents/YouTube Download')

    print('Done!')

print('All video(s) downloaded!')

# Open the folder where the video(s) are located
subprocess.run(['open', '/Users/isaaccherry/Documents/YouTube Download'])