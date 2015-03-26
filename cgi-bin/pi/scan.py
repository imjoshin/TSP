from tweepy.streaming import StreamListener
from tweepy import Stream
from pymongo import MongoClient
from textblob import TextBlob
import tweepy, datetime, time, settings, termios, signal, struct, fcntl, sys, readline, os, httplib, urllib, urllib2, json, subprocess



# Listener to handle discovered tweets
class TweetListener(StreamListener):
	
	# Tweet found with given hashtag
	def on_status(self, status):
		

		if str(status.geo) != 'None':

			blank_current_readline()
			blank_current_readline()
			blank_current_readline()

			parse_tweet(status)
			print '\n'

			global count
			count += 1
			print "\033[32m-----------------------\033[0m"
			print "\033[7mTweets scanned: %d\033[0m" % (count,)
			print "\033[32m-----------------------\033[0m"		

		return True

	def on_error(self, status_code):
		print '\033[22;31mTweet error: \033[4;31m' + str(status_code) + '\033[0m'
		if status_code == 420:
			reconnect(5)
		else:
			reconnect(3)
		return True

	def on_timeout(self):
		print('\033[22;31mTimeout...\033[0m')
		reconnect(3)
		return True

	  
#############
# functions #
#############

# Print method for debug mode
def debug_print(text):
	if settings.debug:
		print "\033[0m\033[22;36m" + text.encode('utf-8') + '\033[0m'

def parse_tweet(status):

	text = status.text.encode('utf-8')
	author = status.user.screen_name.encode('utf-8')
	tweetID = status.id
	location = "%s,%s" % (str(status.geo['coordinates'][0]), str(status.geo['coordinates'][1]))
	timestamp = status.created_at - datetime.timedelta(hours=5);

	hashtags = ""

	for hashtag in status.entities['hashtags']:
		hashtags += hashtag['text'].encode('utf-8') + ","

	#tb = TextBlob(status.text)
	#polarity = tb.sentiment.polarity
	#rating = (polarity + 1) * 50
	rating = subprocess.Popen(['./getMood', text], stdout=subprocess.PIPE).stdout.read()

	#post = {"timestamp": timestamp, "hashtags": hashtags, "location": location, "rating": rating}
	post = {"id": tweetID, "author": author, "text": text, "timestamp": timestamp, "hashtags": hashtags, "location": location, "rating": rating}
	tweets.insert(post)

	print 'Tweet: \033[4;22;37m%s\033[0m' % (text)
	print 'Author: \033[22;32m@%s\033[0m' % (author)
	print 'ID: \033[22;33m%s\033[0m' % (tweetID)
	print 'Location: \033[22;34m%s\033[0m' % (location)
	print 'Timestamp: \033[22;31m%s\033[0m' % (timestamp)
	print 'Hashtags: \033[22;35m%s\033[0m' % (hashtags)
	print 'Rating: \033[7m%d\033[0m' % (rating)


# Reply to the user, if reply=True in the config file
def reply(user, tweetID, response):
	if not settings.reply: return True

	try:
		newTweet = '@' + user + ' ' + response
		api.update_status(newTweet, tweetID)
		debug_print('Posted tweet: ' + newTweet)
	except Exception:
		print('\033[22;31mTwitter account is not authorized to post.\nPlease enable here: \033[4mhttps://apps.twitter.com/ \033[0m')

def reconnect(wait):

		for i in range(wait, 0, -1):
			print "Reconnecting in %d seconds..." % (i,)
			time.sleep(1)
			blank_current_readline()
		
		print 'Reconnecting...'

		auth = tweepy.OAuthHandler(settings.cKey, settings.cSecret)
		auth.set_access_token(settings.aToken, settings.aSecret)

		api = tweepy.API(auth)
		listener = TweetListener()

		debug_print('\nStarting stream...')#' for #%s...' % (settings.hashtag1,))

		stream = Stream(auth, listener)
		print 'Now scanning...'# for #' + settings.hashtag1 + '...'

		stream.filter(track=settings.search)

def blank_current_readline():
	# Next line said to be reasonably portable for various Unixes
	(rows,cols) = struct.unpack('hh', fcntl.ioctl(sys.stdout, termios.TIOCGWINSZ,'1234'))

	text_len = len(readline.get_line_buffer())+2

	# ANSI escape sequences (All VT100 except ESC[0G)
	sys.stdout.write('\x1b[1A')                         # Move cursor up
	sys.stdout.write('\x1b[0G')                         # Move to start of line
	sys.stdout.write('\x1b[2K')                         # Clear current line

def interruptHandler(signal, frame):
	print '\n\033[31mExiting...\033[0m'
	global stop
	stop.set()
	sys.exit(0)

##########
# script #
##########

print "\n"
for i in range(3, 0, -1):
	print "\033[7mStarting script in %d seconds...\033[0m" % (i,)
	time.sleep(1)
	blank_current_readline()

signal.signal(signal.SIGINT, interruptHandler)

#setup database connection
client = MongoClient()
db = client.moodar
tweets = db.tweets

#count of tweets
count = 0

#twitter authorization
auth = tweepy.OAuthHandler(settings.cKey, settings.cSecret)
auth.set_access_token(settings.aToken, settings.aSecret)

api = tweepy.API(auth)

listener = TweetListener()

blank_current_readline()
print chr(27) + "[2J"

stream = Stream(auth, listener)

print 'Now scanning...'#' for #' + settings.hashtag1 + '...\n\n'

#stream.filter(track=[settings.search])
stream.filter(track=settings.search, languages=["en"]) #track=settings.search)
