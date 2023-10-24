from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Example text data and labels
documents = ["This is a positive document.", "This is a negative document."]
labels = [1, 0]  # 1 for positive, 0 for negative

# Vectorize the text using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Train a classifier (Naive Bayes in this example)
classifier = MultinomialNB()
classifier.fit(X, labels)

# Predict the class of a new document
new_document = ["This is another positive document."]
X_new = vectorizer.transform(new_document)
predicted_class = classifier.predict(X_new)
print("Predicted Class:", predicted_class[0])
