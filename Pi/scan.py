from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy, time, settings, termios, signal, struct, fcntl, sys, readline, os, httplib, urllib, urllib2, json, subprocess



# Listener to handle discovered tweets
class TweetListener(StreamListener):
	
	# Tweet found with given hashtag
	def on_status(self, status):
		

		if str(status.geo) != 'None':

			blank_current_readline()
			blank_current_readline()
			blank_current_readline()

			print 'Tweet: \033[4;22;37m%s\033[0m' % (status.text.encode('utf-8'),)
			print 'Tweet Author: \033[22;32m@%s\033[0m' % (status.user.screen_name,)
			print_tweet_info(status)
			parse_tweet(status)
			print '\n\n'

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

def print_tweet_info(status):
	print 'Tweet ID: \033[22;33m%s\033[0m' % (str(status.id),)
	print 'Tweet Geo: \033[22;34m%s\033[0m' % (str(status.geo),)

	url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s" % (status.geo['coordinates'][0], status.geo['coordinates'][1])
	response = urllib2.urlopen(url)
	jsongeocode = response.read()
	location = json.loads(jsongeocode)
	
	if(len(location['results']) > 0):
		print 'Tweet Location: \033[22;36m%s\033[0m' % (location['results'][0]['formatted_address'].encode('utf-8').strip(),)


def parse_tweet(status):
	proc = subprocess.Popen(["curl", "-d", "text='%s'" % status.text.encode('utf-8'), "http://text-processing.com/api/sentiment/"], stderr = subprocess.PIPE,stdout = subprocess.PIPE)
	mood = json.loads(proc.stdout.read())
	if mood['label'] == 'pos':
		print 'Tweet Mood: \033[7;22;32mPositive\033[0m'
	elif mood['label'] == 'neutral':
		print 'Tweet Mood: \033[7;22;33mNeutral\033[0m'
	else:
		print 'Tweet Mood: \033[7;22;31mNegative\033[0m'


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
