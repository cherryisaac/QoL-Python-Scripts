QoL Python Scripts by Isaac Cherry

These are some small projects/scripts that I've created to make my job/life a bit easier

1. Download_Management.py
Function - This script was made to move downloaded files (that usually end up in the Downloads folder) and put them in their proper perspective folders based on their file type. Like .jpg and .png files would go into the Pictures folder or .mp3 and .wav files would go into the Music folder, etc. 

Bonus feature(s) - I've added a function that deletes specified programs from the Downloads folder after some time has passed (e.g. 90 days) This was made because a lot of times I have .zip or .rar or .exe files that I don't use anymore or I've already unpacked the files. So why keep them in my Downloads folder/on my computer to take up unecessary space?

Future feature(s) - I want to set up this script so that it's either always active or that it runs once per day automatically. That shouldn't be too difficult, but for now for what it's worth that's a very low priority task.

2. WebpageData_to_text.py (webscraping)
Function - This script uses beautiful soap to scrape all the data from a website and outputs it to a text file.

Future feature(s):
- I want to be able to filter the text data so that it scrapes all the visible data and NOT the JavaScript data. 
- I also want to be able to scrape the data from sites where after I login I can scrape that data and not just the data before I login.

3. YouTube_Downloader
Function - This script downloads a video from YouTube. After running the script it prompts the user to input a youtube url for download. After the user puts the url in then the console outputs the title of the video and the amount of views it has then proceeds to download the video. The video goes into the specified pre-ordained folder.

4. Countdown_Timer
Function - Prompts for time and counts down from your input time. To change when the time is printed to the console change time.sleep() and time_sec. Example: time.sleep(5) and time_sec -= 5 will print to the console after every 5 seconds of your input.

5. Google_Search
Function - Searches for a subject/topic in Google and clicks on the first link
- Install seleniun with "pip install selenium"