# for Run this app  --> uvicorn main:app --reload

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the model and tokenizer
model = load_model('yelp_review_Model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
max_length = 200

class Review(BaseModel):
    text: str

def preprocess_review(review, tokenizer, max_length):
    sequence = tokenizer.texts_to_sequences([review])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post', truncating='post')
    return padded_sequence

def predict_sentiment(review, model, tokenizer, max_length):
    preprocessed_review = preprocess_review(review, tokenizer, max_length)
    prediction = model.predict(preprocessed_review)
    sentiment_classes = ['negative', 'neutral', 'positive']
    predicted_class = sentiment_classes[prediction.argmax()]
    return predicted_class

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(request: Request, review_text: str = Form(...)):
    sentiment = predict_sentiment(review_text, model, tokenizer, max_length)
    return templates.TemplateResponse("result.html", {"request": request, "sentiment": sentiment, "review_text": review_text})


# Build the Docker Image
# docker build -t sentiment-analysis-app .

# Run the Docker Container
# docker run -d -p 8000:80 sentiment-analysis-app
