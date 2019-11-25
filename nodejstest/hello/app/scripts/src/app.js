import WsClient from './wsclient';
import {ChatForm} from './dom.js';

const FORM_SELECTOR = '[data-chat="form"]';
const MSG_SELECTOR = '[data-chat="message"]';
const CHATLIST_SELECTOR = '[data-chat="chathistory"]';

class ChatApp{
  constructor(){
    console.log('Hello, ES6 Chat App');
    this.form = new ChatForm(FORM_SELECTOR, MSG_SELECTOR);
    WsClient.init('ws://localhost:3001');
    WsClient.addOpenHandler(() => {
      console.log('have connected to server');
      this.form.addBtnClickHandler((msg) => {
        let chatMsg = new ChatMessage({message:msg});
        WsClient.sendMessage(chatMsg);
      });
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
