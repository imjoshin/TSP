function initialize() {

	var mapOptions = {
		center: { lat: 47.1172 , lng: -88.5625},
		zoom: 12
	};
	var map = new google.maps.Map(document.getElementById('Map'), mapOptions);

}
google.maps.event.addDomListener(window, 'load', initialize);

var response = httpGet("moodar.me:8080");

var locations = response.split("|");

function httpGet(theUrl)
{
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
