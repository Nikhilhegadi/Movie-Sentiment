from flask import Flask, render_template, request, jsonify
import pymongo
from datetime import datetime
import pickle

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sentimentDB"]
reviews_col = db["reviews"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["review"]
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    # Save to MongoDB
    reviews_col.insert_one({
        "review": text,
        "sentiment": prediction,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    return jsonify({"sentiment": prediction})

if __name__ == "__main__":
    app.run(debug=True)
