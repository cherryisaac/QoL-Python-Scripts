QoL Python Scripts by Isaac Cherry

These are some small projects/scripts that I've created to make my job/life a bit easier

1. Download_Management.py
Function - This script was made to move downloaded files (that usually end up in the Downloads folder) and put them in their proper perspective folders based on their file type. Like .jpg and .png files would go into the Pictures folder or .mp3 and .wav files would go into the Music folder, etc. 

Bonus feature(s) - I've added a function that deletes specified programs from the Downloads folder after some time has passed (e.g. 90 days) This was made because a lot of times I have .zip or .rar or .exe files that I don't use anymore or I've already unpacked the files. So why keep them in my Downloads folder/on my computer to take up unecessary space?

2. WebpageData_to_Text.py (webscraping)
Function - This script uses beautiful soap to scrape all the data from a website and outputs it to a text file.

3. YouTube_Downloader.py
Function - This script downloads a video from YouTube. After running the script it prompts the user to input a youtube url for download. After the user puts the url in then the console outputs the title of the video and the amount of views it has then proceeds to download the video. The video goes into the specified pre-ordained folder.

4. Countdown_Timer.py
Function - Prompts for time and counts down from your input time. To change when the time is printed to the console change time.sleep() and time_sec. Example: time.sleep(5) and time_sec -= 5 will print to the console after every 5 seconds of your input.

5. Google_Search.py
Function - Searches for a subject/topic in Google and clicks on the first link
- Install seleniun with "pip install selenium"

6. HTML&CSS_Scraper.py
Function - Gets the HTML & CSS elements from a website

7. Repo_Script.py
Function - A script that gets all the repos from an organization with the properties: 
- repo_name 
- repo_size 
- archived 
- license 
- private 
- contributor_counts 
- team_counts