(function(window){
  'use strict'

  var App = window.App || {};
  var $ = window.jQuery;

  function FormHandler(selector){
    if (!selector){
      throw new Error('No selector provided');
    }

    this.$formElement = $(selector);
  }

  FormHandler.prototype.addClickHandler = function(clkslt, fn){
    this.$formElement.on('click', clkslt, fn);
  };

  App.FormHandler = FormHandler;
  window.App = App;
})(window);
