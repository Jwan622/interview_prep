/*
So I didn't see any requirements so this program will require that you pass in strings through the command line and access them through process.argv

for example: from the root of this folder, you can type 'node pig_latin.js "there" "today" "apple" "through"' and it should return
-> 'erethay
odaytay
appleay
oughthray'
*/

var rawARGV = process.argv
/* apparently process.argv contains the command line strings but the first two elements are paths to node and the relevant file */
var cleanedARGV = rawARGV.slice(2)

/* I think looping through the vowels will be quicker than looping through the consonants so I made an array of vowels */
var vowels = ["a", "e", "i", "o", "u"];
var pigLatinSuffix = "ay"

cleanedARGV.forEach(function(word) {
  while (vowels.indexOf(word.substring(0,1)) === -1) {
    var cutOffWord = word.slice(1);

    word = cutOffWord.concat(word.substring(0,1));
  }
  console.log(word.concat(pigLatinSuffix))
});
