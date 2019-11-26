import $ from 'jquery';

export class ChatForm {
  constructor(formsel, inputsel){
    this.$form = $(formsel);
    this.$input = $(inputsel);
    this.dump();
  }

  addBtnClickHandler(fn){
    this.$form.find('button').on('click', () => {
      let val = this.$input.val();
      if (val.length > 0)
      {
        fn(val);
        this.$input.val('');
      }
    });
  }
  dump(){
    //console.log(this.$formElement);
    console.log(this.$form);
    console.log(this.$input);
  }
}
export class ChatList {
  constructor(listsel, username){
    this.$list = $(listsel);
    this.username = username;
  }
  drawMessage({message:m, user:u, timestamp: t}){
    let $msgrow = $('<li>', {'class':'message-row'});
    let $message = $('<p>');
    $message.append($('<span>', {
      'class':'message-username',
      text: u
    }));
    $message.append($('<span>', {
      'class':'message-timestamp',
      'sendtime':t,
      text: formatDate(new Date(t))
    }));
    $message.append($('<span>', {
      'class':'message-message',
      text:m
    }));
    $msgrow.append($message);
    this.$list.append($msgrow);
    $msgrow.get(0).scrollIntoView();
  }
}
export class Point {
  constructor(x, y){
    this.x = x;
    this.y = y;
    this.dump();
  }
  dump(){
    console.log('point(' + this.x + ', ' + this.y + ')');
  }
}

function formatDate(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'pm' : 'am';
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  return date.getFullYear() + '/' + date.getMonth()+1 + "/" + date.getDate() + "/" + "  " + strTime;
}

