#!/usr/bin/env python3
import os
from datetime import datetime, timedelta
import sys
import time
import logging
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# ** Your downloads folder directory...to be changed according to your os.
source_dir = '/Users/isaaccherry/Downloads'

# ** Your destination folders after filtering downloads...to be changed according to your os.
dest_dir_docs = '/Users/isaaccherry/Documents/Docs'
dest_dir_video = '/Users/isaaccherry/Movies'
dest_dir_music = '/Users/isaaccherry/Music'
dest_dir_image = '/Users/isaaccherry/Pictures' 
dest_dir_webpages = '/Users/isaaccherry/Documents/Webpages'

def make_unique(name):
    num = int(name.split(".")[0]) + 1
    return f"{num}.{name.split('.')[1]}"

def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = make_unique(name)
        shutil.move(entry, os.path.join(dest, unique_name))
    else:
        shutil.move(entry, dest)

def sort_current_files():
    entries = os.scandir(source_dir)
    for entry in entries:
        name = entry.name
        dest = source_dir
        if name.endswith(('.wav','.mp3')):
            dest = dest_dir_music
            move(dest, entry, name)
        elif name.endswith(('.pdf', '.rtf', '.txt', '.csv', '.xls', '.xlsx')):
            dest = dest_dir_docs
            move(dest, entry, name)
        elif name.endswith(('.mov', '.mp4', '.avi', '.wmv')):
            dest = dest_dir_video
            move(dest, entry, name)
        elif name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.raw', '.avif')):
            dest = dest_dir_image
            move(dest, entry, name)
        elif name.endswith(('.html', '.svg', 'webp')):
            dest = dest_dir_webpages
            move(dest, entry, name) 

sort_current_files()

def delete_files_after_90_days(folder, extensions):
  now = datetime.now()
  # ? In the os.walk() function, dirs is a list of the names of the subdirectories in the current directory (i.e. root).
  for root, dirs, files in os.walk(folder):
    for f in files:
      file_path = os.path.join(root, f)
      if (now - datetime.fromtimestamp(os.path.getctime(file_path))).days >= 90 and f.endswith(tuple(extensions)):
        os.remove(file_path)

delete_files_after_90_days(source_dir, ['.rar', '.exe', '.dmg', '.gz', '.pkg'])

print('All Done!')


# class MoveHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         try:
#             entries = os.scandir(source_dir)
#             for entry in entries:
#                 name = entry.name
#                 dest = source_dir
#                 if name.endswith(('.wav','.mp3')):
#                     dest = dest_dir_music
#                     move(dest, entry, name)
#                 elif name.endswith(('.pdf', '.rtf', '.txt', '.csv', '.xls', '.xlsx')):
#                     dest = dest_dir_docs
#                     move(dest, entry, name)
#                 elif name.endswith(('.mov', '.mp4', '.avi', '.wmv')):
#                     dest = dest_dir_video
#                     move(dest, entry, name)
#                 elif name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.raw', '.avif')):
#                     dest = dest_dir_image
#                     move(dest, entry, name)
#                 elif name.endswith(('.html', '.svg')):
#                     dest = dest_dir_webpages
#                     move(dest, entry, name) 
#         except Exception as e:
#             print(f'Error: {e}')

#     def on_created(self, event):
#         try:
#             entries = os.scandir(source_dir)
#             for entry in entries:
#                 name = entry.name
#                 dest = source_dir
#                 if name.endswith(('.wav','.mp3')):
#                     dest = dest_dir_music
#                 elif name.endswith(('.pdf', '.rtf', '.txt', '.csv', '.xls', '.xlsx')):
#                     dest = dest_dir_docs
#                     move(dest, entry, name)
#                 elif name.endswith(('.mov', '.mp4', '.avi', '.wmv')):
#                     dest = dest_dir_video
#                     move(dest, entry, name)
#                 elif name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.raw', '.avif')):
#                     dest = dest_dir_image
#                     move(dest, entry, name)
#                 elif name.endswith(('.html', '.svg')):
#                     dest = dest_dir_webpages
#                     move(dest, entry, name) 
#         except Exception as e:
#             print(f'Error: {e}')


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = '/Users/isaaccherry/Downloads' 
#     event_handler = MoveHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     finally:
#         observer.stop()
#         observer.join()

    
# To run constantly in the background type 'nohup python Download_Management.py &' 

# If you want to terminate the script, you can use the `ps` command to find the process ID 
# of the script and then use the `kill` command to terminate the process.

# ps aux | grep Download_Management.py
# Find the process ID of the script

# kill 12345
# Replace 12345 with the process ID of the script

