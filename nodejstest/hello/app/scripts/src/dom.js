import $ from 'jquery';

export class ChatForm {
  contructor(formsel, inputsel){
    this.$formElement = $(formsel);
    this.$inputElement = $(inputsel);
    this.test = 'test';
    this.$test = 'test2';
    console.log(this.$formElement);
    console.log(this.test);
    console.log(this.$test);
  }

  addBtnClickHandler(fn){
    //console.log(this.$formElement);
    //console.log(this.$inputElement);
    this.$formElement.find('button').on('click', () => {
      let val = this.$inputElement.val;
      fn(val);
      this.$inputElement.val = '';
    });
  }
}
export class ChatList {
}
