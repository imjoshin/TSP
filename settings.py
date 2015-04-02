#This python file grabs trending tweets on a 5 minute timer using the Tweepy api 

import tweepy
import datetime
import json
from datetime import timedelta
from urllib2 import Request, urlopen, URLError

#Retrievs the trending tweets
def trendy():

	#Uses our auth keys and the Tweepy API to connect to the Twitter API
	f = open(r'/var/www/html/TSP/savetime.txt', 'r+')
	z = open(r'/var/www/html/TSP/trendsHERE.txt', 'r+')
	initTime = f.read(19)
	allOfThem = z.read()
	consKey = "aOfQrwx793BVuTRMoO3UzJMUW"
	consSecret = "AEeq70OpKzyJdP4W8OOHN5dx2IwD6NVkbI9VEosMbSuzbkoocE"
	accessToken = "3065054746-ksthvpPy5MTMO88F7pwS8J5oGv3mVkC7Dy1RRd3"
	accessTokenSecret = "8KqxINVNcyCzqP9HV7TkERgcC8QFadL1Xo9Fz0R8ZKpKl"
	auth = tweepy.OAuthHandler(consKey,consSecret)
	auth.set_access_token(accessToken, accessTokenSecret)
	api = tweepy.API(auth)

	#Time variables for our 5 minute trending requests
	time = datetime.datetime.now()
	timeString = str(time)	
	testThis = datetime.datetime.strptime(initTime, "%Y-%m-%d %H:%M:%S")

	trends = 0
	i=0
	fiveMin = timedelta(minutes = 5)
	
	#Twitter lets a user request trending every 5 minutes
	#So this code only occurs if 5 minutes have passed since the last time we requested them
	if( (testThis+fiveMin) <  datetime.datetime.now()):
		#Attemps to grab the trending tweets, which is a JSON object
		try:
			mat=api.trends_place(23424977)
			allOfThem=""
			
			#Grabs just the names of the trending tweets, we don't need other JSON fields
			names_set = set([trend['name']
					for trend in mat[0]['trends']])

			#Removes Unicode Characters (Python doesn't like them)
			for tw in names_set:
				i+=1
				hashtag = tw
				if "#" in tw:
					hashtag = "<label onclick='myFunction(" + "&quot;" + tw + "&quot;" +  ")' target='_blank' class='trend' > %s </label>" % (tw) 
				else:
					hashtag = "<label onclick='myFunction(" +    "&quot;" + tw +  "&quot;" +  ")' target='_blank' class='trend'> %s </label>" % (tw )
				allOfThem += " %i: %s<br><br><br>"  % (i, hashtag)
			allOfThem = allOfThem.encode('ascii','ignore')
			
			z.seek(0)
			z.truncate(0)	
			z.write(allOfThem)
			
			f.seek(0)
			f.truncate(0)
			f.write(timeString[:19])
		except URLError, e:
			1+1	
	
	return allOfThem
