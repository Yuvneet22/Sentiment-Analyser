# Sentiment IQ

Sentiment IQ is a sentiment analysis tool that leverages advanced natural language processing (NLP) techniques to analyze public sentiment from text data. It uses Python libraries such as NLTK for text preprocessing, scikit-learn for machine learning, and Flask to provide a backend API. The frontend is a simple web interface that allows users to input text and get real-time sentiment predictions.

## Technologies Used

- Python
- Flask
- NLTK
- scikit-learn
- joblib
- HTML, CSS, JavaScript

## Dataset

The model is trained on the IMDB Dataset, which contains movie reviews labeled with sentiment (positive or negative). The dataset is preprocessed by converting text to lowercase, removing punctuation, tokenizing, and removing stopwords.

## Model Training

The project uses TF-IDF vectorization to convert text data into numerical features. Two models were experimented with: Logistic Regression and Multinomial Naive Bayes. The final model and vectorizer are saved using joblib for use in the Flask backend API.

## Backend API

The backend is a Flask application exposing a `/predict` endpoint that accepts POST requests with JSON payload:

```json
{
  "review": "Your text to analyze"
}
```

The API preprocesses the input text, vectorizes it, and returns a JSON response with the sentiment prediction:

```json
{
  "prediction": "positive"  // or "negative"
}
```

## Frontend User Interface

The frontend is a simple web page (`ui.html`) styled with `style.css`. It provides:

- A text input box to enter a sentence or review.
- An "Analyze" button that sends the input to the backend API.
- A display area showing the sentiment prediction result.
- An image illustrating sentiment analysis.

## How to Run

### Prerequisites

- Python 3.x installed
- Required Python packages: Flask, nltk, scikit-learn, joblib, flask-cors
- Node.js and npm (optional, if you want to serve frontend with a local server)

### Setup

1. Install Python dependencies:

```bash
pip install flask nltk scikit-learn joblib flask-cors
```

2. Download NLTK data (stopwords and punkt):

Run the following Python commands or let the backend do it automatically on first run:

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

3. Ensure the following files are in the `code` directory:

- `model.joblib`
- `vectorizer.joblib`
- `ui.html`
- `style.css`
- `sentiment.jpg`

### Running the Backend

From the `code` directory, run:

```bash
python model.py
```

This will start the Flask server on `http://localhost:5000`.

### Running the Frontend

Open the `ui.html` file in a web browser directly or serve it using a local HTTP server.

For example, using Python's built-in HTTP server:

```bash
cd code
python -m http.server 8000
```

Then open `http://localhost:8000/ui.html` in your browser.

### Using the Application

- Enter a sentence or review in the input box.
- Click the "Analyze" button.
- The sentiment prediction will be displayed below the button.

## Contact

For any questions or feedback, please contact the project maintainer.

---

&copy; 2023 Sentiment IQ. All rights reserved.
