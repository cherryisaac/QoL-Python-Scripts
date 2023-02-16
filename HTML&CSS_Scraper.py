import requests
from bs4 import BeautifulSoup

website = "youtube"

# Set the URL of the website to fetch
url = f'https://{website}.com/'

# Make a GET request to the website
response = requests.get(url)

# Extract the HTML content from the response
html_content = response.text

# Create a BeautifulSoup object for parsing the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the CSS styles from the HTML
css_styles = soup.findAll('style')

# Write the HTML content to a file
with open(f'{website}.html', 'w') as file:
    file.write(html_content)

# Write the CSS styles to a file
with open(f'{website}.css', 'w') as file:
    for css_style in css_styles:
        file.write(str(css_style))