import nltk

sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
tree = cp.parse(tagged)
tree.draw()
