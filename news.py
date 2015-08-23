import urllib2
import json

#HackerNews API documentation: https://github.com/HackerNews/API

#Pull all story numbers into a Python data dictionary
response = urllib2.urlopen('https://hacker-news.firebaseio.com/v0/topstories.json')
data=json.load(response)

#Takes each story number and extracts the title by treating as Python dictionary
for i in data:
	genurl='https://hacker-news.firebaseio.com/v0/item/%s.json?print=pretty' % (i) 
	#print genurl
	item_response=urllib2.urlopen(genurl)  
	parsed_response=json.load(item_response)
	print parsed_response["title"].encode('utf-8')
