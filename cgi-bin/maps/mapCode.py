from urllib2 import Request, urlopen, URLError
from urllib import unquote
import json

from apiclient import discovery

mapTest = ""
googleEngineKey = "AIzaSyBEgTOg8eljGOa5-nsu27CN56ARWWnVAX8"   
service = discovery.build('mapsengine', 'v1',developerKey=googleEngineKey)

# Read the location of every Feature in a Table.
features = service.tables().features()
request = features.list(id='12421761926155747447-06672618218968397709',maxResults=500, version='published')
while request is not None:
   response = request.execute()
   for feature in response['features']:
      mapTest += feature['geometry']['coordinates'] + " <br>"

   # Is there an additional page of features to load?
   request = features.list_next(request, response)

