import urllib2
import json

#HackerNews API documentation: https://github.com/HackerNews/API

api_url='https://hacker-news.firebaseio.com/v0/topstories.json'
item_url='https://hacker-news.firebaseio.com/v0/item/'

#Pull all story numbers into a Python data dictionary
response = urllib2.urlopen(api_url)
data=json.load(response)

#Takes each story number and extracts the title by treating as Python dictionary
with open("headlines.txt", "w") as output_file:
	for i in data:
		genurl="%s%s.json?print=pretty" % (item_url, i) 
		item_response=urllib2.urlopen(genurl)  
		parsed_response=json.load(item_response)
		output_file.write(parsed_response["title"].encode('utf-8'))


