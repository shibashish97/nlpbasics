import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Sample text
text = "Tokenization is the process of splitting text into words or smaller units. Stop words like 'the' and 'is' are removed, and words are stemmed or lemmatized. Lowercasing ensures consistency. Text cleaning removes special characters, punctuation, and noise. Bag of Words (BoW) and TF-IDF are used for text representation. N-grams are extracted. Text normalization standardizes text to a common format."

# Tokenization
tokens = nltk.word_tokenize(text)
# print(tokens)

# Stopwords Removal
stop_words = set(stopwords.words("english"))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
# print(filtered_tokens)

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
# print(stemmed_tokens)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_token = [lemmatizer.lemmatize(word) for word in filtered_tokens]
# print(lemmatized_token)

# Lower casing
lowercase_tokens = [word.lower() for word in lemmatized_token]
# print(lowercase_tokens)

# Text cleaning
cleaned_text = ' '.join(re.findall(r'\b\w+\b',' '.join(lowercase_tokens)))
# print(cleaned_text)

# Bag of words(BOW)
vectorizer_bow = CountVectorizer()
bow_matrix = vectorizer_bow.fit_transform([cleaned_text])
# print(bow_matrix)

# TF-IDF
vectorizer_tfidf = TfidfVectorizer()
tfidf_matrix = vectorizer_tfidf.fit_transform([cleaned_text])
# print(tfidf_matrix)

# N-grams(for bigrams)
vectorizer_bigrams = CountVectorizer(ngram_range=(2,2))
bigram_matrix = vectorizer_bigrams.fit_transform([cleaned_text])
# print(bigram_matrix)

# Print the results
print("Original Text:")
print(text)

print("\nTokenization:")
print(tokens)

print("\nStop Word Removal:")
print(filtered_tokens)

print("\nStemming:")
print(stemmed_tokens)

print("\nLemmatization:")
print(lemmatized_token)

print("\nLowercasing:")
print(lowercase_tokens)

print("\nText Cleaning:")
print(cleaned_text)

print("\nBag of Words (BoW):")
print(bow_matrix.toarray())

print("\nTF-IDF:")
print(tfidf_matrix.toarray())

print("\nN-grams (Bigrams):")
print(bigram_matrix.toarray())