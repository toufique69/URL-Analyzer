# Name: Md Toufique Hasan
# Email: hasan.mdtoufique@gmail.com
####################################

import json
import sys
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Load the gambling-related terms from the JSON file
with open("dictionary.json", "r") as file:
    gambling_terms = json.load(file)


# Function to classify a website as a gambling site or not
def classify_website(url):
    # Use requests to get the HTML content of the website
    html = requests.get(url).text
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    # Extract the text from the website
    text = soup.get_text()
    # Tokenize the text
    tokens = word_tokenize(text)
    # Initialize the Porter stemmer
    stemmer = PorterStemmer()
    # Remove stopwords and stem the remaining tokens
    filtered_tokens = [stemmer.stem(token) for token in tokens if token.lower() not in stopwords.words('english')]
    # Compare the filtered tokens against the gambling-related terms
    gambling_count = sum(token in gambling_terms for token in filtered_tokens)
    # Classify the website as a gambling site or not based on the number of gambling-related terms found
    if gambling_count > len(filtered_tokens) * 0.1:  # 10% of the total tokens
        return "Gambling Site"
    else:
        return "Non-Gambling Site"


# test the function
if __name__ == '__main__':
    url = sys.argv[1]
    print(classify_website(url))