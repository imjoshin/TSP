function initialize() {

	var mapOptions = {
		center: { lat: 47.1172 , lng: -88.5625},
		zoom: 12
	};
	var map = new google.maps.Map(document.getElementById('Map'), mapOptions);
}
google.maps.event.addDomListener(window, 'load', initialize);

