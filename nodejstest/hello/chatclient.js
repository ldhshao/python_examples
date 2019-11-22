(function(window){
  'use strict'

  var App = window.App;
  var FormHandler = App.FormHandler;
  var FORM_SELECTOR = '[data-client="form"]';
  var BTNCON_SELECTOR = '[data-btn="connect"]';
  var BTNSND_SELECTOR = '[data-btn="send"]';

  var formHandler = new FormHandler(FORM_SELECTOR);
  formHandler.addClickHandler(BTNCON_SELECTOR, function(){
    console.log('button connect clicked');
  });
  formHandler.addClickHandler(BTNSND_SELECTOR, function(){
    console.log('button send clicked');
  });

})(window);

