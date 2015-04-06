#This file creates the string for the index.html file using python 

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
                    
               
                    
            </head>
    
            <body>
                    <div id="Main" class="container">
                            
                            <div id="Title">
                                    <h1> <p align="center"> &nbsp; MOOD RADAR!</p></h1>
				    
                                        <input type="text" placeholder="Search..." name="fname" id = "inBox" onkeypress="handle(event);"><br>
                                      
					<input type="submit" class="moodButton" value="Very Negative" id="veryNegative" onclick="toggleMoods('vneg')" style="background-color: #E83333">
					<input type="submit" class="moodButton" value="Negative" id="negative" onclick="toggleMoods('neg')" style="background-color: orange">
					<input type="submit" class="moodButton" value="Neutral" id="neutral" onclick="toggleMoods('neu')" style="background-color: yellow">
					<input type="submit" class="moodButton" value="Positive" id="positive" onclick="toggleMoods('pos')" style="background-color: #1DCF32">
					<input type="submit" class="moodButton" value="Very Positive" id="veryPositive" onclick="toggleMoods('vpos')" style="background-color: #3E4BFA">
					<!--<input type="submit" value="Submit" id="submit-button">-->

                             </div>
                              
                            <div id="Trending">
                                   
				 <h1>Trending</h1><br><br>
                        	""" + info + """ 
			    </div>
			    
                            <div id="Map">

                            </div>
                          
                            
                         
                                    
                            <div id="Info">
                                    <font size="1"><h1>Info:</h1></font>
                                    <p>Moodar created by Joshua Johnson, Rory Straubel, Brian Ferus, Riley Hirn, and Brian Keith for Team Software Project 2015. </br> Moodar was created using the TextBlob and Tweepy Python APIs, accompanied by Google's Map API.</p>
                            </div>
                            
                            
                            
                    </div>
		    <script>
		    function myFunction(t){
			console.log("test");
			document.getElementById("inBox").value= t;
			search();
		    }
		    </script>
		       <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true&libraries=visualization"></script>
                    <script type="text/javascript" src="//code.jquery.com/jquery-1.10.2.js"></script>
		   <script src="cgi-bin/js/script.js">
                              </script>

            </body>
    </html>
    """
	return s
