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
                                    <h1> <p align="center"> &nbsp; MOOD RADAR!</p></h1>
				    <form action = "http://i.imgur.com/13SWnPa.gif" method="get">
                                        <input type="text" placeholder="Enter a state..." name="fname" id = "inBox"><br>
                                       <input type="submit" value="Submit" id="submit-button">
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
                                    <font size="1"><h1>Info:</h1></font>
                                    <p>Moodar created by Joshua Johnson, Rory Straubel, Brian Ferus, Riley Hirn, and Brian Keith for Team Software Project 2015. </br> Moodar was created using the Stanford Natural Language Processing Group's API and Twitter's API.</p>
                            </div>
                            
                            
                            
                    </div>
            </body>
    </html>
    """
	return s
