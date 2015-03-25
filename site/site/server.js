var sys = require( "sys" );
var http = require('http'),
    mongojs = require("mongojs"),
    fs = require('fs');

var uri = "mongodb://127.0.0.1/moodar",
     db = mongojs.connect(uri, ["tweets"]);



var server = http.createServer(requestHandler);
function requestHandler(request, response) {
    sys.puts("got request");
    response.writeHead(200, {"Content-Type": "text/JSON"});
    db.tweets.find().toArray(function(err, records) {
	if(err) {
            sys.puts("There was an error querying the database");
            resopnse.end();
            return;
        }
	sys.puts("no error from db");
	sys.puts(records[0]["location"]);
	for(var index = 0; index < records.length; index++) {
		sys.puts("rating: ");
		sys.puts(records[index]["location"]);
		response.write(records[index]["location"] + "|");
	}
        //response.write(records);
        response.end();
    });
   
}
server.listen(8080);
                                                 
// For logging....
sys.puts( "Server is running on 8080" );
