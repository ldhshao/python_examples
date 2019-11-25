import WsClient from './wsclient'

class ChatApp{
  constructor(){
    console.log('Hello, ES6 Chat App');
    WsClient.init('ws://localhost:3001');
    WsClient.addOpenHandler(() => {
      console.log('have connected to server');
      //let hellomsg = new ChatMessage();
      WsClient.sendMessage(new ChatMessage({message:'hello'}));
    });
    WsClient.addMessageHandler((data) => {
      console.log(data);
    });
  }
}

class ChatMessage{
  constructor({message: m, user:u = 'dhliu', timestamp: t = (new Date()).getTime()}){
    this.message = m;
    this.user = u;
    this.timestamp = t;
  }
}

export default ChatApp;
