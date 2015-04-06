var express = require('express')
var app = express()

var sys = require( "sys" );
var mongojs = require("mongojs"),
    fs = require('fs'),
    cors = require('cors');	

var uri = "mongodb://127.0.0.1/moodar",
     db = mongojs.connect(uri, ["tweets"]);



app.use(cors());
app.get('/', function (req, res) {
	
   	sys.puts("got request");
	var field = req.headers['search'];
	if(!field){
		field = "";
	}
	var search = '.*' + field  + '.*';
	sys.puts("Search Feild = " + req.headers['search']);
	db.tweets.find({ 'text':new RegExp(search)}).toArray(function(err, records) {
		if(err) {
            		sys.puts("There was an error querying the database");
            		res.send("Error");
            		return;
        	}
		sys.puts("no error from db");
		//sys.puts(records[0]["location"]);
	
		var startIndex = parseInt(req.headers['start']);
		var done = "false"; 
		var response = "";
	        sys.puts("starting at " + startIndex + " Records Length = " + records.length); 	
		for(var index = startIndex; index < startIndex + 10000; index++) {
			//sys.puts("rating: ");
			//sys.puts(records[index]["location"]);
			if(index >= records.length){
				done = "true";
				break;
			}
			response += (records[index]["location"] + "," + records[index]["rating"] +  "|");
		}
		response = done + "|" + response;
		sys.puts(response.length);
		res.send(response);
	});
})

var server = app.listen(8080, function () {

  var host = server.address().address
  var port = server.address().port

  console.log('Example app listening at http://%s:%s', host, port)

})

