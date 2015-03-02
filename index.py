from cgi import escape
from urllib import unquote
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
import tweepy
from urllib2 import Request, urlopen, URLError

# The Publisher passes the Request object to the function
def index():
   consKey = "aOfQrwx793BVuTRMoO3UzJMUW"
   consSecret = "AEeq70OpKzyJdP4W8OOHN5dx2IwD6NVkbI9VEosMbSuzbkoocE"
   accessToken = "3065054746-ksthvpPy5MTMO88F7pwS8J5oGv3mVkC7Dy1RRd3"
   accessTokenSecret = "8KqxINVNcyCzqP9HV7TkERgcC8QFadL1Xo9Fz0R8ZKpKl"
   auth = tweepy.OAuthHandler(consKey,consSecret)
   auth.set_access_token(accessToken, accessTokenSecret)
   api = tweepy.API(auth)
   info = "test"
   request = Request('https://api.twitter.com/1.1/trends/place.json?id=1')

   try:
       	response = urlopen(request)
        data=json.load(response)
        info  = data.trends[0].name
   except URLError, e:
        print 'Error', e
   

   s = """\

    <html>
            <head>
                    <title>Mood Radar</title>
                    <link rel="shortcut icon" type="image/x-icon" href="ico.png" />
                    <link rel="stylesheet" type="text/css" href="css/style.css">
            
                    <script type="text/javascript" src="//code.jquery.com/jquery-1.10.2.js"></script>
                    <script type="text/javascript" src="../cgi-bin/js/script.js"></script>
                    
            </head>
    
            <body>
                    <div id="Main" class="container">
                            
                            <div id="Title">
                                    <h1>MOOD RADAR!</h1>
                            </div>
                            
                            <div id="Map">
                                    <h1>MAP</h1>
                            </div>
                            
                            <div id="Trending">
                                    <h1>Trending</h1>
                            </div>
                            
                            <div id="Search">
                                    <h1>Search</h1>	
                            </div>
                                    
                            <div id="Info">
                                    <h1>Info</h1>
                                    %s
                            </div>
                            
                            
                            
                    </div>
            </body>
    </html>
    """
	

   t = "<h1>" + info +"</h1>"
   
   return s % t
