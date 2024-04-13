#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && !isNaN(h) && !isNaN(w)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
