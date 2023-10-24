from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Example data
documents = ["Apple Inc. was founded by Steve Jobs.", "Microsoft was founded by Bill Gates."]
labels = ["founder", "founder"]

# Vectorize the text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Train a classifier
classifier = MultinomialNB()
classifier.fit(X, labels)

# Predict a relation for a new sentence
new_sentence = ["Amazon was founded by Jeff Bezos."]
X_new = vectorizer.transform(new_sentence)
predicted_relation = classifier.predict(X_new)
print("Predicted Relation:", predicted_relation[0])
