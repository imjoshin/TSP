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
	//res.send('Hello World!')
   	sys.puts("got request");
    	db.tweets.find().toArray(function(err, records) {
		if(err) {
            		sys.puts("There was an error querying the database");
            		res.send("Error");
            		return;
        	}
		sys.puts("no error from db");
		//sys.puts(records[0]["location"]);
		var response = "";
		for(var index = 0; index < records.length; index++) {
			//sys.puts("rating: ");
			//sys.puts(records[index]["location"]);
			response += (records[index]["location"] + "|");
		}
		sys.puts(response.length);
		res.send(response);
	});
})

var server = app.listen(8080, function () {

  var host = server.address().address
  var port = server.address().port

  console.log('Example app listening at http://%s:%s', host, port)

})

