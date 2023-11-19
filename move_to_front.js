(function() {
  'use strict';

  var moveToFront = function(data, frontData) {
    frontData.forEach(function(country){
      console.log(country)

      if (data.indexOf(country) != -1) {
        var duplicateIndex = data.indexOf(country)
        data.splice(duplicateIndex,1)
      }
    })
    console.log(data)
    return frontData.concat(data);
  }

  module.exports = moveToFront;
})();
