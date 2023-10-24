from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

documents = [
    "Topic modeling is a technique in natural language processing.",
    "It is used to discover topics in a collection of documents.",
    "Latent Dirichlet Allocation is a popular method for topic modeling."
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

lda = LatentDirichletAllocation(n_components=2)
lda.fit(X)

print(lda.transform(X))