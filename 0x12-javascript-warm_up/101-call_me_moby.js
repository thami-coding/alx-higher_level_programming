#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  if (parseInt(x)) {
    while (x--) {
      theFunction();
    }
  }
};
