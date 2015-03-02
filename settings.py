import tweepy
import datetime

consKey = "aOfQrwx793BVuTRMoO3UzJMUW"
consSecret = "AEeq70OpKzyJdP4W8OOHN5dx2IwD6NVkbI9VEosMbSuzbkoocE"
accessToken = "3065054746-ksthvpPy5MTMO88F7pwS8J5oGv3mVkC7Dy1RRd3"
accessTokenSecret = "8KqxINVNcyCzqP9HV7TkERgcC8QFadL1Xo9Fz0R8ZKpKl"
auth = tweepy.OAuthHandler(consKey,consSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

initTime = datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

time = datetime.datetime.now()

testAgainst = datetime.timedelta(0,0,0,0,6)

if((initTime-time) > testAgainst):
	try:
		trends=api.trends_place(1)
	except URLError, e:
		print 'Error', e
initTime = time
