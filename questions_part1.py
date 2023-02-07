# Name: Md Toufique Hasan
# Email: hasan.mdtoufique@gmail.com
####################################

import json
import requests
from bs4 import BeautifulSoup
import re
import sys

# Read URLs from the text file
with open(sys.argv[1], 'r') as file:
    urls = file.read().splitlines()

# Initialize an empty dictionary to store keywords
keywords = {}

# Visit each URL and extract keywords
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    words = re.findall(r'\w+', text)
    for word in words:
        if word not in keywords:
            keywords[word] = 1
        else:
            keywords[word] += 1

# Save the dictionary of keywords to a file
with open("dictionary.json", "w") as file:
    json.dump(keywords, file)