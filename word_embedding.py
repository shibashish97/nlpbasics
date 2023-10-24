from gensim.models import Word2Vec

sentences = [
    "Machine learning is fun.",
    "Natural language processing is interesting.",
    "Word embeddings are useful."
]

sentences = [sentence.split() for sentence in sentences]
model = Word2Vec(sentences,vector_size = 100 , window = 5 , min_count = 1 ,sg=0)

# Get the vector representation of a word
vector = model.wv['learning']
print(vector)