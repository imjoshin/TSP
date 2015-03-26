var sys = require( "sys" );
var http = require('http'),
    mongojs = require("mongojs"),
    fs = require('fs');
/*
var uri = "mongodb://127.0.0.1/moodar",
     db = mongojs.connect(uri, ["tweets"]);
*/


http.createServer(function (req, res) {
   sys.puts("got request");
    if(req.url.indexOf('.js') != -1){ //req.url has the pathname, check if it conatins '.js'

      fs.readFile(__dirname + '/js/script.js', function (err, data) {
        if (err) console.log(err);
        res.writeHead(200, {'Content-Type': 'text/javascript'});
        res.write(data);
        res.end();
      });

    } else if(req.url.indexOf('.css') != -1){ //req.url has the pathname, check if it conatins '.css'

      fs.readFile(__dirname + '/css/style.css', function (err, data) {
        if (err) console.log(err);
        res.writeHead(200, {'Content-Type': 'text/css'});
        res.write(data);
        res.end();
      });

    } else if(req.url.indexOf('.cords') != -1){ //req.url has the pathname, check if it conatins '.cords'

      fs.readFile(__dirname + '/css/style.css', function (err, data) {
        if (err) console.log(err);
        res.writeHead(200, {'Content-Type': 'text/css'});
        res.write(data);
        res.end();
      });

    } else {
      	sys.puts("Had a html request!");
	fs.readFile('./index.html',function (err,html) {
      		if(err) {
			throw err;
		}
		res.writeHeader(200, {"Content-Type": "text/html"});
		res.write(html);  
        	res.end(); 
	});
    }


}).listen(8080);
                                                 
// For logging....
sys.puts( "Server is running on 8080" );
