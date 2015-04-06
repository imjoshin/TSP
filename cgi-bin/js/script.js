var submit = document.getElementById('submit-button');
var savedNames = [];
var savedPoints = [];

var g1 = ['rgba(255, 130, 130, 0)',
'rgba(255, 120, 120, 1)',
'rgba(255, 110, 110, 1)',
'rgba(255, 100, 100, 1)',
'rgba(255, 90, 90, 1)',
'rgba(255, 80, 80, 1)',
'rgba(255, 70, 70, 1)',
'rgba(255, 60, 60, 1)',
'rgba(255, 50, 50, 1)',
'rgba(255, 40, 40, 1)',
'rgba(255, 30, 30, 1)',
'rgba(255, 20, 20, 1)',
'rgba(255, 10, 10, 1)',
'rgba(255, 0, 0, 1)']

var g2 = ['rgba(255, 194, 130, 0)',
'rgba(255, 187, 120, 1)',
'rgba(255, 179, 110, 1)',
'rgba(255, 172, 100, 1)',
'rgba(255, 165, 90, 1)',
'rgba(255, 158, 80, 1)',
'rgba(255, 151, 70, 1)',
'rgba(255, 144, 60, 1)',
'rgba(255, 137, 50, 1)',
'rgba(255, 130, 40, 1)',
'rgba(255, 123, 30, 1)',
'rgba(255, 116, 20, 1)',
'rgba(255, 109, 10, 1)',
'rgba(255, 102, 0, 1)']

var g3 = ['rgba(255, 255, 130, 0)',
'rgba(255, 255, 120, 1)',
'rgba(255, 255, 110, 1)',
'rgba(255, 255, 100, 1)',
'rgba(255, 255, 90, 1)',
'rgba(255, 255, 80, 1)',
'rgba(255, 255, 70, 1)',
'rgba(255, 255, 60, 1)',
'rgba(255, 255, 50, 1)',
'rgba(255, 255, 40, 1)',
'rgba(255, 255, 30, 1)',
'rgba(255, 255, 20, 1)',
'rgba(255, 255, 10, 1)',
'rgba(255, 255, 0, 1)']

var g4 = ['rgba(130, 255, 130, 0)',
'rgba(120, 255, 120, 1)',
'rgba(110, 255, 110, 1)',
'rgba(100, 255, 100, 1)',
'rgba(90, 255, 90, 1)',
'rgba(80, 255, 80, 1)',
'rgba(70, 255, 70, 1)',
'rgba(60, 255, 60, 1)',
'rgba(50, 255, 50, 1)',
'rgba(40, 255, 40, 1)',
'rgba(30, 255, 30, 1)',
'rgba(20, 255, 20, 1)',
'rgba(10, 255, 10, 1)',
'rgba(0, 255, 0, 1)']


var g5 = ['rgba(150, 0, 150, 0)',
'rgba(120, 120, 255, 1)',
'rgba(110, 110, 255, 1)',
'rgba(100, 100, 255, 1)',
'rgba(90, 90, 255, 1)',
'rgba(80, 80, 255, 1)',
'rgba(70, 70, 255, 1)',
'rgba(60, 60, 255, 1)',
'rgba(50, 50, 255, 1)',
'rgba(40, 40, 255, 1)',
'rgba(30, 30, 255, 1)',
'rgba(20, 20, 255, 1)',
'rgba(10, 10, 255, 1)',
'rgba(0, 0, 255, 1)']


var gray = "#f0ede5";
var red = "rgb(232, 51, 51)";
var orange = "orange";
var yellow = "yellow";
var green = "rgb(29, 207, 50)";
var blue = "rgb(62, 75, 250)";

var map;
var heatmap1;
var heatmap2;
var heatmap3;
var heatmap4;
var heatmap5;
var numHeatmaps;


function initialize() {
	numHeatmaps = 0;
        document.getElementById('inBox').value = "";
	search();
}


google.maps.event.addDomListener(window, 'load', initialize);

function httpGet(theUrl,searchString, start)
{
    var xmlHttp = null;
    	
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );	    
    xmlHttp.setRequestHeader('search',searchString.toLowerCase());
    xmlHttp.setRequestHeader('start', start);
    xmlHttp.send( null );
    return xmlHttp.response;
}

function search(){
	resetButtons();

        var mapOptions = {
                center: { lat: 39.8 , lng: -98.5625},
                zoom: 4
        };

        map = new google.maps.Map(document.getElementById('Map'), mapOptions);

	var index = 0;
	var locations = [];
	var split;

	var curSearch = document.getElementById('inBox').value;
	if(savedNames.indexOf(curSearch) != -1) {
		locations = savedPoints[savedNames.indexOf(curSearch)];
	} else {
		do {
			var response = httpGet("http://moodar.me:8080", document.getElementById('inBox').value, index);

			split = response.split("|");
		      	locations = locations.concat(split.slice(1, split.length - 1));
			index = locations.length;
			console.log(index);
		} while(split[0] == "false");
		if(locations.length > 5000) {
			savedNames.push(curSearch);
			savedPoints.push(locations);
		}
	}

       	var dataPoints1 = [];
        var dataPoints2 = [];
        var dataPoints3 = [];
        var dataPoints4 = [];
        var dataPoints5 = [];

      	for(var i = 1; i < locations.length-1;i++){
               	var intLoc = locations[i].split(",");
	        if(intLoc[2] < 30)
                        dataPoints1.push(new google.maps.LatLng(parseFloat(intLoc[0]), parseFloat(intLoc[1])));
                else if(intLoc[2] < 45)
                        dataPoints2.push(new google.maps.LatLng(parseFloat(intLoc[0]), parseFloat(intLoc[1])));
                else if(intLoc[2] < 55)
                        dataPoints3.push(new google.maps.LatLng(parseFloat(intLoc[0]), parseFloat(intLoc[1])));
                else if(intLoc[2] < 70)
                        dataPoints4.push(new google.maps.LatLng(parseFloat(intLoc[0]), parseFloat(intLoc[1])));
                else 
                        dataPoints5.push(new google.maps.LatLng(parseFloat(intLoc[0]), parseFloat(intLoc[1])));

        }

	var n1 = dataPoints1.length; var n2 = dataPoints2.length; var n3 = dataPoints3.length; var n4 = dataPoints4.length; var n5 = dataPoints5.length;
	var average = (n1 + n2 * 2 + n3 * 3 + n4 * 4 + n5 * 5) / (n1 + n2 + n3 + n4 + n5);
	console.log("\nVery Negative: " + n1 + "\nNegative: " + n2 + "\nNeutral: " + n3 + "\nPositive: " + n4 + "\nVery Positive: " + n5);
	console.log("Average Rating: " + average);

        map = new google.maps.Map(document.getElementById('Map'), mapOptions);

        var pointArray1 = new google.maps.MVCArray(dataPoints1);
        var pointArray2 = new google.maps.MVCArray(dataPoints2);
        var pointArray3 = new google.maps.MVCArray(dataPoints3);
        var pointArray4 = new google.maps.MVCArray(dataPoints4);
        var pointArray5 = new google.maps.MVCArray(dataPoints5);

        heatmap3 = new google.maps.visualization.HeatmapLayer({data: pointArray3, map:map, gradient : g3, opacity: .5, radius : 10});

        heatmap1 = new google.maps.visualization.HeatmapLayer({data: pointArray1, map:map, gradient : g1, opacity: .5, radius : 10});
        heatmap2 = new google.maps.visualization.HeatmapLayer({data: pointArray2, map:map, gradient : g2, opacity: .5, radius : 10});
//        var heatmap3 = new google.maps.visualization.HeatmapLayer({data: pointArray3, map:map, gradient : g3, opacity: .3});
        heatmap4 = new google.maps.visualization.HeatmapLayer({data: pointArray4, map:map, gradient : g4, opacity: .5, radius : 10});
        heatmap5 = new google.maps.visualization.HeatmapLayer({data: pointArray5, map:map, gradient : g5, opacity: .5, radius : 10});
//	var heatmap1 = new google.maps.visualization.HeatmapLayer({data: pointArray1, map:map, gradient : g1, opacity: .4, radius : 10});
//        var heatmap3 = new google.maps.visualization.HeatmapLayer({data: pointArray3, map:map, gradient : g3, opacity: .45, radius : 10});
//        var heatmap5 = new google.maps.visualization.HeatmapLayer({data: pointArray5, map:map, gradient : g5, opacity: .4, radius : 10});


        //heatmap.setMap(map);	
}

//submit.onclick = search;


function resetButtons(){
	numHeatmaps = 5;
	document.getElementById("veryNegative").style.backgroundColor = red;
	document.getElementById("negative").style.backgroundColor = orange;
	document.getElementById("neutral").style.backgroundColor = yellow;
	document.getElementById("positive").style.backgroundColor = green;
	document.getElementById("veryPositive").style.backgroundColor = blue;

}
function handle(e){
	e = e || window.event;
	if(e.keyCode === 13){
		search();
	}
}

function toggleMoods(mood){
	if(mood == 'vneg'){
		var element = document.getElementById("veryNegative");
		if(element.style.backgroundColor == red){
			element.style.backgroundColor = gray;
			heatmap1.setMap(null);
			numHeatmaps--;
		}else{
			element.style.backgroundColor = red;
			heatmap1.setMap(map);
                        numHeatmaps++;

		}

	}else if(mood == 'neg'){
                var element = document.getElementById("negative");
                if(element.style.backgroundColor == orange){
                        element.style.backgroundColor = gray;
			heatmap2.setMap(null);
                        numHeatmaps--;
                }else{
                        element.style.backgroundColor = orange;
			heatmap2.setMap(map);
                        numHeatmaps++;

                }

	
	}else if(mood == 'neu'){
                var element = document.getElementById("neutral");
                if(element.style.backgroundColor == yellow){
                        element.style.backgroundColor = gray;
			heatmap3.setMap(null);
                        numHeatmaps--;
                }else{
                        element.style.backgroundColor = yellow;
			heatmap3.setMap(map);
                        numHeatmaps++;

                }


	}else if(mood == 'pos'){
                var element = document.getElementById("positive");
                if(element.style.backgroundColor == green){
                        element.style.backgroundColor = gray;
			heatmap4.setMap(null);
                        numHeatmaps--;
                }else{
                        element.style.backgroundColor = green;
			heatmap4.setMap(map);
                        numHeatmaps++;
                }


	}else if(mood == 'vpos'){
                var element = document.getElementById("veryPositive");
                if(element.style.backgroundColor == blue){
                        element.style.backgroundColor = gray;
			heatmap5.setMap(null);
                        numHeatmaps--;
                }else{
                        element.style.backgroundColor = blue;
			heatmap5.setMap(map);
                        numHeatmaps++;
                }
	

	}
	
	var s = 1; //starting value
	var t = 12; //denominator for subtraction
        heatmap1.set('opacity', s - (numHeatmaps / t));
        heatmap2.set('opacity', s - numHeatmaps / t);
        heatmap3.set('opacity', s - numHeatmaps / t);
        heatmap4.set('opacity', s - numHeatmaps / t);
        heatmap5.set('opacity', s - (numHeatmaps / t));

}
