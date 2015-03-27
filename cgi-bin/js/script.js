var pointArray,heatmap;

function initialize() {

        var mapOptions = {
                center: { lat: 39.8 , lng: -98.5625},
                zoom: 4
        };

        var map = new google.maps.Map(document.getElementById('Map'), mapOptions);


	var response = httpGet("http://moodar.me:8080");

		
	var locations = response.split("|");
	var dataPoints = [];
	
	for(var i = 0; i < locations.length-1;i++){
	        var intLoc = locations[i].split(",");
        	dataPoints.push(new google.maps.LatLng(parseFloat(intLoc[0]), parseFloat(intLoc[1])));
	}

	map = new google.maps.Map(document.getElementById('Map'), mapOptions);
	
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
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.response;
}
