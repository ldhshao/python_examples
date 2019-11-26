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
