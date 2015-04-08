# TSP
Team Se7en's TSP Project Mood Radar.

The goal of this Web Application is relay the general mood of a large area to the user. Using Tweets that have an accompanying location ID Moodar parses the mood using Standford Natural Language Processing Group's API and plots its location on a map provided by the Google Map API. Moodar is viewable at http://www.moodar.me.


Moodar uses a Node Express application to recieve\send data from a MonogoDB database. This data is collected using a python script. Using the Express application and normal javascript we are able to create and display a Google Map with five differant heatmaps showing different moods.

User Interaction
  Search for tweets with a certain word to view the mood of that word.
  Toggle the five different heatmaps on and off to view only select moods.
  View trending tweets and view their moods by clicking on them.
  Zoom on the map to get a closer\wider view.


Used APIS:

Tweepy- http://www.Tweepy.org

Twitter- https://dev.twitter.com/overview/documentation

Google Maps- https://developers.google.com/maps/

TextBlob- http://textblob.readthedocs.org/en/dev/

Node- https://nodejs.org/

Bootstrap- http://getbootstrap.com/2.3.2/
