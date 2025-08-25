import re
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
nltk.download("stopwords", quiet=True)
stop_words = set(stopwords.words("english"))

def preprocess_text(text: str) -> str:
    """Clean and preprocess input text"""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation & special chars
    text = " ".join(word for word in text.split() if word not in stop_words)
    return text