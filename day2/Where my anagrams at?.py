def anagrams(word, words):
    return [_word for _word in words if sorted(_word) == sorted(word)]
