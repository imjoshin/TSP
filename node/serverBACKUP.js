var sys = require( "sys" );
var http = require('http'),
    fs = require('fs');

fs.readFile('./index.html', function (err, html) {
    if (err) {
        throw err; 
    }       
    http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.writeHeader(200, {"Content-Type": "text/html"});
	response.write(html);  
        response.end();  
    }).listen(8080);
});
                                                   
// For logging....
sys.puts( "Server is running on 8080" );
