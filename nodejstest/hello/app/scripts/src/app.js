import WsClient from './wsclient';
import {ChatForm, Point, ChatList, promptForUsername} from './dom';
import {UserStore} from './datastore'

const USER_KEY = 'x-chatapp/u';
//const WS_URL = 'ws://172.16.3.160:3001';
const WS_URL = 'ws://localhost:3001';
const FORM_SELECTOR = '[data-chat="form"]';
const MSG_SELECTOR = '[data-chat="message"]';
const CHATLIST_SELECTOR = '[data-chat="chathistory"]';


class ChatApp{
  constructor(){
    console.log('Hello, ES6 Chat App');
    let usrstore = new UserStore(USER_KEY);
    this.username = usrstore.get();
    if (!this.username){
      this.username = promptForUsername();
      usrstore.set(this.username);
    }
    this.form = new ChatForm(FORM_SELECTOR, MSG_SELECTOR);
    //this.point = new Point(10, 50);
    this.chatlist = new ChatList(CHATLIST_SELECTOR, this.username);
    WsClient.init(WS_URL);
    WsClient.addOpenHandler(() => {
      console.log('have connected to server');
      this.form.addBtnClickHandler((msg) => {
        let chatMsg = new ChatMessage({message:msg, user:this.username});
        WsClient.sendMessage(chatMsg);
      });
    });
    WsClient.addMessageHandler((data) => {
      console.log(data);
      this.chatlist.drawMessage(data);
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
