from pymongo import MongoClient
import datetime, time, settings

def main():
	while(1):
		limit = datetime.datetime.now() - datetime.timedelta(hours=settings.hoursTilDelete)
	
		client = MongoClient()
		db = client.moodar
		tweets = db.tweets
	
		numRemoved = tweets.find({"timestamp": {"$lt": limit}}).count()
		#tweets.remove({})
		tweets.remove({"timestamp": {"$lt": limit}})
		print "\033[22;32m%s:\033[0m Removed \033[22;33m%d\033[0m entries." % (str(datetime.datetime.now()), numRemoved)
	
		time.sleep(60*10)
		
main()
