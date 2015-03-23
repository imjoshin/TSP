from cgi import escape
import settings
from urllib import unquote
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
import tweepy
from urllib2 import Request, urlopen, URLError
import maps

# The Publisher passes the Request object to the function
def index():
	googleMap = ""
  
	output = settings.trendy()
	info = str(output)
	test = "H!"
	s = """\

    <html>
            <head>
                  <style type="text/css">
                     html, body, #map-canvas { height: 100%; margin: 0; padding: 0;}
                  </style>
                    <title>Mood Radar</title>
                    <link rel="shortcut icon" type="image/x-icon" href="ico.png" />
                    <link rel="stylesheet" type="text/css" href="css/style.css">
                    
                    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true&libraries=visualization"></script>
                    <script type="text/javascript" src="//code.jquery.com/jquery-1.10.2.js"></script>
                
                    
            </head>
    
            <body>
                    <div id="Main" class="container">
                            
                            <div id="Title">
                                    <h1>MOOD RADAR!</h1>
				    <form action = "http://i.imgur.com/13SWnPa.gif" method="get">
                                       State: <input type="text" name="fname"><br>
                                       Mood: <input type="text" name="lname"><br>
                                       <input type="submit" value="Submit">
                                    </form>
                            </div>
                              
                            <div id="Trending">
                                   
				 <h1>Trending</h1><br><br>
                        	""" + info + """ 
			    </div>
			    
                            <div id="Map">
                              <script src="cgi-bin/js/script.js">
                              </script>
                            </div>
                          
                            
                         
                                    
                            <div id="Info">
                                    <h1>Info</h1>
                                   
                            </div>
                            
                            
                            
                    </div>
            </body>
    </html>
    """
	return s
