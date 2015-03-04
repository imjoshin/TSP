from urllib2 import Request, urlopen, URLError
from urllib import unquote
import json

from apiclient import discovery

googleEngineKey = "AIzaSyBEgTOg8eljGOa5-nsu27CN56ARWWnVAX8"   
service = discovery.build('mapsengine', 'v1',developerKey=googleEngineKey)

# Read the location of every Feature in a Table.
