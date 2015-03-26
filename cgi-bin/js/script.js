var pointArray,heatmap;
var response = httpGet("http://moodar.me:8080");

var locations = response.split("|");
var dataPoints;   

for(var i = 0; i < locations.length;i++){
        var intLoc = locations[i].split(",");
        dataPoints.push(new google.maps.LatLng(parseInt(intLoc[0]), parseInt(intLoc[1])));
}

function initialize() {

	var mapOptions = {
		center: { lat: 47.1172 , lng: -88.5625},
		zoom: 12
	};
	var map = new google.maps.Map(document.getElementById('Map'), mapOptions);
	
  	var pointArray = new google.maps.MVCArray(dataPoints);

  	heatmap = new google.maps.visualization.HeatmapLayer({
		data: pointArray
  	});

  	heatmap.setMap(map);

}


google.maps.event.addDomListener(window, 'load', initialize);

function httpGet(theUrl)
{
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, true );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
