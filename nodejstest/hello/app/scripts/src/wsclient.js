//var WebSocket = require('ws')
let socket;

function init(url){
  console.log('connecting to server');
  socket = new WebSocket(url); 
}

function addOpenHandler(fn){
  socket.onopen = () => {
    fn();
  };
}

function addMessageHandler(fn){
  socket.onmessage = (e) => {
    let data = JSON.parse(e.data);
    fn(data);
  };
}

function sendMessage(data){
  console.log(data);
  socket.send(JSON.stringify(data));
}

export default {init, addOpenHandler, addMessageHandler, sendMessage};
