import nltk

text = "This is example sentence for pos tagging"
words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print(tags)

'''
'DT' represents a determiner (e.g., 'This', 'an').
'VBZ' represents a verb (e.g., 'is').
'NN' represents a noun (e.g., 'example', 'sentence', 'POS').
'IN' represents a preposition or subordinating conjunction (e.g., 'for').
'NNP' represents a proper noun, singular (e.g., 'POS').
'VBG' represents a verb, gerund or present participle (e.g., 'tagging').
'.' represents punctuation (e.g., '.').

'''