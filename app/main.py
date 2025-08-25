from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from app.utils import preprocess_text
import os

# Globals for model/vectorizer
vectorizer = None
model = None

# Helper to load models only once
def load_models():
    global vectorizer, model
    if vectorizer is None or model is None:
        if not os.path.exists("models/tfidf_vectorizer.joblib") or not os.path.exists("models/logistic_model.joblib"):
            raise FileNotFoundError("Model or vectorizer file not found in /models folder")
        vectorizer = joblib.load("models/tfidf_vectorizer.joblib")
        model = joblib.load("models/logistic_model.joblib")
    return vectorizer, model

# FastAPI instance
app = FastAPI(title="Ticket Classification API", version="1.0")

# Request body schema
class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input_data: TextInput):
    vec, clf = load_models()
    processed = preprocess_text(input_data.text)
    transformed = vec.transform([processed])
    prediction = clf.predict(transformed)[0]
    return {"text": input_data.text, "predicted_topic": prediction}

@app.get("/")
def home():
    return {"message": "Ticket Classification API is running 🚀"}
