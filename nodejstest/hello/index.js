var http = require('http')
var fs = require('fs')
var extract = require('./extract')
var mywebsocketsrv = require('./websockets-server')
var NO_RESOURCE = '<h1>Cannot find the resource</h1>'
var HTTP_SERVER_PORT = 3000
var WS_SERVER_PORT = 3001
var htmlregexp = /\.html$/i
var jsregexp = /\.js$/i

var handleError = function(err, res) {
  res.writeHead(404);
  res.end(NO_RESOURCE);
}
var server = http.createServer(function (req, res) {
  console.log('Responding to a request.');
  var url = req.url;
  var myextract = new extract('app');
  var filename = myextract.filePath(url);
  console.log(url);
  console.log(filename);
  fs.readFile(filename, function(err, data){
    if (err){
      handleError(err, res);
    }
    else{
      if (htmlregexp.test(filename)){
        res.setHeader('Content-Type', 'text/html');
      }
      else if (jsregexp.test(filename)){
        res.setHeader('Content-Type', 'application/javascript');
      }
      res.end(data);
    }
  });
  //res.end('<h1>Hello, world</h1>');
});

var wss = new mywebsocketsrv(WS_SERVER_PORT); 

server.listen(3000);
