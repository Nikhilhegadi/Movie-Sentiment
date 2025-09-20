from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Tiny sample dataset
texts = ["I love this movie", "This movie is terrible", "Awesome!", "Worst film ever"]
labels = ["Positive", "Negative", "Positive", "Negative"]

# Vectorizer + model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# Save them
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model and vectorizer saved!")
