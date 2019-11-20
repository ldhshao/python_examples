var http = require('http')
var fs = require('fs')
var NO_RESOURCE = '<h1>Cannot find the resource</h1>'

var handleError = function(err, res) {
  res.writeHead(404);
  res.end(NO_RESOURCE);
}
var server = http.createServer(function (req, res) {
  console.log('Responding to a request.');
  var url = req.url;
  var filename = 'index.html';
  if (url.length > 1) {
    filename = url.substring(1);
  }
  console.log(filename);
  fs.readFile('app/' + filename, function(err, data){
    if (err){
      handleError(err, res);
    }
    else{
      res.end(data);
    }
  });
  //res.end('<h1>Hello, world</h1>');
});

server.listen(3000);
