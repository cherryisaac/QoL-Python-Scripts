import requests
from bs4 import BeautifulSoup
# To install BeautifulSoup type "pip3 install beautifulsoup4" in the cmd bar below

# Make a request to a webpage
url = 'http://www.csgnetwork.com/htmlcodetest.html'
res = requests.get(url)

# # Create a beautiful soup object
soup = BeautifulSoup(res.content, "html.parser")

#Find all the text on a webpage
text = soup.find_all(text=True)

#Filter out text elements that are just whitespaces
filtered_text = [t.strip() for t in text if t.strip()] 

# Open a file called "Raw_data.txt" for writing
with open('Scraped_Data.txt', 'w') as f:

    for results in filtered_text:
        f.write(results + '\n')

print('All Done!')