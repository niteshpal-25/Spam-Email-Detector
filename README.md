# 📧 Spam Email Detector

A full-stack Machine Learning web application that classifies emails/messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) and Machine Learning.

## 🚀 Project Overview

Spam Email Detector is an AI-powered application built using **React.js**, **FastAPI**, and **Scikit-learn**. Users can enter email content and receive an instant prediction along with a confidence score. All predictions are stored in a SQLite database and can be viewed through a history dashboard.

---

## ✨ Features

### Frontend

* Modern React.js UI
* Responsive Design
* Email Prediction Form
* Prediction Result Display
* Confidence Score
* Prediction Timestamp
* History Page
* Clear History Option
* Loading Spinner
* Error Handling

### Backend

* FastAPI REST APIs
* SQLite Database Integration
* CORS Enabled
* Request Validation using Pydantic
* Prediction History Storage
* Swagger API Documentation

### Machine Learning

* SMS Spam Collection Dataset
* Text Preprocessing
* TF-IDF Vectorization
* Multinomial Naive Bayes Classification
* Model Persistence using Joblib

---

## 🛠 Technology Stack

### Frontend

* React.js
* React Router
* Axios
* Tailwind CSS

### Backend

* FastAPI
* Pydantic
* SQLAlchemy
* SQLite
* Uvicorn

### Machine Learning

* Python
* Scikit-learn
* Pandas
* NumPy
* Joblib

---

## 📂 Project Structure

```text
spam-email-detector/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   └── package.json
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── train_model.py
│   ├── create_db.py
│   ├── model.pkl
│   ├── vectorizer.pkl
│   ├── spam_detector.db
│   ├── requirements.txt
│   └── dataset/
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/spam-email-detector.git
cd spam-email-detector
```

---

## Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create database:

```bash
python create_db.py
```

Train model:

```bash
python train_model.py
```

Run FastAPI:

```bash
uvicorn app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run application:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## 📡 API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "status": "success",
  "message": "Spam Email Detector API Running"
}
```

---

### Model Information

```http
GET /model-info
```

Response:

```json
{
  "model": "Multinomial Naive Bayes",
  "accuracy": 98.3
}
```

---

### Predict Email

```http
POST /predict
```

Request:

```json
{
  "message": "Congratulations! You won a free iPhone."
}
```

Response:

```json
{
  "prediction": "Spam",
  "confidence": 98.5,
  "timestamp": "2026-06-07 10:30:00"
}
```

---

### Get Prediction History

```http
GET /history
```

---

### Clear Prediction History

```http
DELETE /history
```

---

## 🧠 Machine Learning Workflow

1. Load SMS Spam Collection Dataset
2. Text Cleaning and Preprocessing
3. Convert Text to TF-IDF Features
4. Train Multinomial Naive Bayes Model
5. Save Model using Joblib
6. Load Model in FastAPI
7. Predict Spam/Not Spam

---

## 📊 Sample Predictions

| Message                                  | Prediction |
| ---------------------------------------- | ---------- |
| You won a free iPhone. Claim now!        | Spam       |
| Meeting scheduled for tomorrow at 11 AM. | Not Spam   |
| Earn ₹50,000 per week from home.         | Spam       |
| Please review the attached report.       | Not Spam   |

---

## 🔮 Future Enhancements

* User Authentication
* Export History to CSV
* Email Attachment Analysis
* Deep Learning Models (LSTM/BERT)
* Email Inbox Integration
* Cloud Deployment
* Docker Support

---

## 👨‍💻 Author

**Vishal Kumar Pal**

Software Developer | Data Engineer | AI Enthusiast

---

## 📜 License

This project is developed for educational and research purposes.
