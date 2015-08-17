$(document).ready(function() {
	dictionary = dicts['English']['Spanish']
	english_word_array = Object.keys(dictionary)
	var fetchRandom = function() {
	    var english_word = english_word_array[Math.floor(Math.random() * english_word_array.length)]
	    var spanish_word = dictionary[english_word]
	    return [english_word, spanish_word]
	}

	words = fetchRandom();
	console.log(words[0], words[1]);
});
