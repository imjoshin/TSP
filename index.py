from cgi import escape
from urllib import unquote
import json
from urllib2 import Request, urlopen, URLError

# The Publisher passes the Request object to the function
def index():
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
	
   request = Request('https://api.twitter.com/1.1/trends/1')
   
   try:
	response = urlopen(request)
	data=json.load(response)
	print data
   except URLError, e:
	print 'Error', e

   t = "<h1>TEST TWO</h1>"
   
   return s % t
