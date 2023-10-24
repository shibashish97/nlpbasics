from summarizer import Summarizer

model = Summarizer()
text = """
Text summarization is a process of creating a concise and coherent summary of a document. It can be done in an extractive manner by selecting important sentences or in an abstractive manner by generating new sentences. Gensim is a library that provides extractive summarization using the TextRank algorithm.
"""

summary = model(text)
print(summary)
