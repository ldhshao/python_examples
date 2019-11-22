'use strict';

function Extract(dir) {
  this.dir = '';
  this.jsregexp = /\.js$/i;
  if (dir.length > 0){
    this.dir = dir + '/';
  }

  this.filePath = function(url) {
    var fileName = 'index.html';
    if (url.length > 1) {
      fileName = url.substring(1);
    }
    if (this.jsregexp.test(url)){
      return fileName;
    }
    
    return this.dir + fileName;
  };
}

module.exports = Extract;
