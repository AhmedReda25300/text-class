# 🎫 Ticket Classification API

This project provides a **FastAPI-based REST API** for automatic ticket classification using a **TF-IDF vectorizer** and a **Logistic Regression model**.  
It is fully containerized with **Docker** for easy deployment.

---

## 📌 Features

- Pretrained **TF-IDF vectorizer** and **Logistic Regression classifier**
- REST API endpoints built with **FastAPI**
- Dockerized for easy setup and deployment
- Simple preprocessing pipeline for text cleaning

---

## 📂 Project Structure

```plaintext
.
├── app/
│   ├── main.py                  # FastAPI entry point
│   ├── utils.py                 # Text preprocessing utilities
├── models/
│   ├── tfidf_vectorizer.joblib  # Saved TF-IDF vectorizer
│   ├── logistic_model.joblib    # Saved Logistic Regression model
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker setup
└── README.md                    # Documentation
```

---

## ⚡ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/AhmedReda25300/text-class.git
cd ticket-classification-api
```

### 2. Build the Docker image

```bash
docker build -t ticket-classification-api .
```

### 3. Run the container

```bash
docker run -d -p 8000:8000 ticket-classification-api
```

---

## 🏋️ Training the Model (Optional)

If you want to train your own model and generate the `.joblib` files:

1. **Prepare your dataset**  
    Ensure you have a CSV file with at least these columns:  
    - `text`: the ticket description/content  
    - `label`: the topic/class of the ticket

2. **Train the model using the training notebook**

3. **Place models in `/models`**  
    Ensure the generated files are inside the `models/` folder:

    ```plaintext
    models/
    ├── tfidf_vectorizer.joblib
    ├── logistic_model.joblib
    ```

---

## 🔥 API Usage

Once running, the API will be available at:

```bash
curl http://localhost:8000/
```

Response:

```json
{"message": "Ticket Classification API is running 🚀"}
```

---

## 🎯 Predict Endpoint

```bash
curl -X POST "http://localhost:8000/predict" \
      -H "Content-Type: application/json" \
      -d '{"text": "reset my account password"}'
```

Response:

```json
{
  "text": "reset my account password",
  "predicted_topic": "Access"
}
```

---

## 🚀 Tech Stack

- **FastAPI**: for API
- **scikit-learn**: for ML model
- **Joblib**: for model persistence
- **Docker**: for deployment