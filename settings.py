import tweepy
import datetime
import json
from datetime import timedelta
from urllib2 import Request, urlopen, URLError

def trendy():

	
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
	time = datetime.datetime.now()
	timeString = str(time)
	
	testThis = datetime.datetime.strptime(initTime, "%Y-%m-%d %H:%M:%S")

	trends = 0
	i=0
	fiveMin = timedelta(minutes = 5)
	
	#fix if state
	if( (testThis + fiveMin ) <  datetime.datetime.now()):
		try:
			mat=api.trends_place(1)
			allOfThem=""
			names_set = set([trend['name']
					for trend in mat[0]['trends']])
			for tw in names_set:
				i+=1
				hashtag = tw
				if "#" in tw:
					hashtag = "<a class='trend' href='https://twitter.com/hashtag/%s?src=tren'>%s</a>" % (tw.replace("#", ""), tw) 
				else:
					hashtag = "<a class='trend' href='https://twitter.com/search?q=%s&src=tren'>%s</a>" % (tw.replace(" ", "%20"), tw)
				allOfThem += " %i: %s<br>"  % (i, hashtag)
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
