def order(sentence):
  # code here
  if len(sentence) <= 1:
    return sentence
  words = sentence.split(' ')
  words_idx = {}
  for word in words:
    words_idx[int(''.join(filter(str.isdigit, word)))] = word
  return ' '.join([words_idx[i] for i in sorted(words_idx)])
