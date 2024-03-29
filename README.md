# URL-Analyzer

General
-------

This is an exercise to test ideas for content classification.

This exercise has 2 parts:
Part 1 - Generating the dictionary of keywords.
Part 2 - Using the dictionary of keywords to classify a website.

Part 1
1. Hunt for as much websites as you can that you can classify as a Gambling site. These have to be websites in the English language, and you can look for as many websites as possible. List the URLs of the websites in a text file.
Eg:
	text file contains:
		http://site1.gambling
		http://sportsbetting.tld
		http://bettingtips.blog/a.html


2. Using the text file you generated above, create a Python script that will visit those websites, parse out the keywords and generate a dictionary of Gambling-related terms. This dictionary can be any file format (text, json, csv, etc.) that you will be using in Part 2. You can use any method that you deem necessary to generate the appropriate keywords.
	- INPUT: yourscript1.py <the text file with the gambling URLs>
	- OUTPUT: dictionary file

Part 2
Using the dictionary from Part 1, create a Python script that will expect a URL input, and then generate a classification if it's a Gambling site or not.
	- INPUT: yourscript2.py <Any URL>
	- OUTPUT1: Gambling site
	- OUTPUT2: Non-Gambling site


The Python scripts must be compatible with Python 3.5 and higher.

## Files of this Repository
1. The questions_1.py is the solution of questions_1.txt.
2. The URL_List.txt file is the text file with gambling URLs.
3. The questions_part1.py is the solution of questions.txt (Part 1).
4. The dictionary.json file is the dictionary generated from Part 1.
5. The questions_part2.py is the solution of questions.txt (Part 2).

N.B: questions_part1.py and questions_part2.py may take some times to execute.
