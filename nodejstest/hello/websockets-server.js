'use strict';
var WebSocket = require('ws')
var WebSocketServer = WebSocket.Server;
var clts = [];
var msgs = [];

function MyWebSocketServer(port) {
  this.port = port;
  this.server = new WebSocketServer({
    port: port
  });
  console.log("websockets server start");

  this.server.on('connection', function(socket) {
    console.log('client connection estabished');
    clts.push(socket);
    if (msgs.length > 0){
        msgs.forEach(function(value, index, array) {
        socket.send(value);
      });
    }

    socket.on('message', function(data) {
      console.log('receive message: ' + data);
      msgs.push(data);
      clts.forEach(function(value, index, array){
        value.send(data);
      });
    });
  });
}

module.exports = MyWebSocketServer;
