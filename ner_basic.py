import nltk

nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk import pos_tag,word_tokenize,ne_chunk

text = "Barack Obama was born in Hawaii. He was the 44th President of the United States."
words = word_tokenize(text)
tags = pos_tag(words)
tree = ne_chunk(tags)

print(tree)

'''
(PERSON Barack/NNP) and (PERSON Obama/NNP) are recognized as named entities of type "PERSON."
(GPE Hawaii/NNP) is recognized as a named entity of type "GPE" (Geopolitical Entity).
(GPE United/NNP States/NNPS) is recognized as a named entity of type "GPE."

'''