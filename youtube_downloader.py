from pytube import YouTube
from sys import argv
import sys

url = input("Enter the YouTube URL: ")
youtube = YouTube(url)

print("Title: ", youtube.title)

print("Views: ", youtube.views) 

ytd = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Your destination folders after downloading the video...to be changed according to your os.
ytd.download('/Users/isaaccherry/Documents/YouTube Download')

print('All Done!')
