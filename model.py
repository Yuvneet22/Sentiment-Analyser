# filepath: c:\Users\hp\Desktop\My Projects\Tech T\model.py
# app.py (Flask backend)
from flask import Flask, request, jsonify, abort
from flask_cors import CORS # Import CORS
import joblib
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

# ...existing code...
app = Flask(__name__)
CORS(app) # Enable CORS for the entire app

# Load the vectorizer and model
# Use the correct filenames and assume they are in the same directory as the script
vectorizer_path = 'vectorizer.joblib' # Correct filename
model_path = 'model.joblib'          # Correct filename

if not os.path.exists(vectorizer_path) or not os.path.exists(model_path):
    # Make the error message more specific
    raise FileNotFoundError(f"Vectorizer ('{vectorizer_path}') or model ('{model_path}') file not found in the current directory. Please check the paths and filenames.")

vectorizer = joblib.load(vectorizer_path)
model = joblib.load(model_path)
# ...rest of the code...
# NLTK downloads
nltk.download('stopwords')
nltk.download('punkt')

# Preprocess function
def preprocess(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    # Join tokens back into a single string
    return ' '.join(filtered_tokens)

@app.route('/predict', methods=['POST'])
def predict():
    # ... (your existing predict function code) ...
    if not request.is_json:
        abort(400, description="Request must be JSON")

    data = request.get_json()
    review = data.get('review')

    if review is None:
         abort(400, description="Missing 'review' key in JSON payload")
    if not isinstance(review, str):
         abort(400, description="'review' must be a string")

    try:
        processed = preprocess(review)
        vectorized = vectorizer.transform([processed])
        prediction = model.predict(vectorized)[0]
        if hasattr(prediction, 'item'):
             prediction = prediction.item()
        return jsonify({'prediction': prediction})
    except Exception as e:
        print(f"Error during prediction: {e}")
        abort(500, description="Internal server error during prediction")


if __name__ == '__main__':
    app.run(debug=True) # Runs on port 5000 by default