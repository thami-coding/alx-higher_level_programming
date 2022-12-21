#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  if (parseInt(x) > 0) {
    while (x--) {
      theFunction();
    }
  }
};
