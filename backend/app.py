from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import joblib

from database import SessionLocal
from models import PredictionHistory

app = FastAPI(
    title="Spam Email Detector API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load ML Model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


# Request Model
class EmailRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Email content to classify"
    )


@app.get("/")
async def health_check():
    return {
        "status": "success",
        "message": "Spam Email Detector API Running"
    }


@app.get("/model-info")
async def model_info():
    return {
        "model": "Multinomial Naive Bayes",
        "accuracy": 98.3
    }


@app.post("/predict")
async def predict(request: EmailRequest):

    try:
        message = request.message.strip()

        if not message:
            raise HTTPException(
                status_code=400,
                detail="Message cannot be empty"
            )

        transformed = vectorizer.transform([message])

        prediction = model.predict(transformed)[0]

        probabilities = model.predict_proba(transformed)[0]

        confidence = round(
            max(probabilities) * 100,
            2
        )

        result = (
            "Spam"
            if prediction == 1
            else "Not Spam"
        )

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        db = SessionLocal()

        try:
            history = PredictionHistory(
                message=message,
                prediction=result,
                confidence=confidence,
                timestamp=timestamp
            )

            db.add(history)
            db.commit()

        finally:
            db.close()

        return {
            "prediction": result,
            "confidence": confidence,
            "timestamp": timestamp
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/history")
async def get_history():

    db = SessionLocal()

    try:
        data = (
            db.query(PredictionHistory)
            .order_by(PredictionHistory.id.desc())
            .all()
        )

        return [
            {
                "id": item.id,
                "message": item.message,
                "prediction": item.prediction,
                "confidence": item.confidence,
                "timestamp": item.timestamp
            }
            for item in data
        ]

    finally:
        db.close()


@app.delete("/history")
async def clear_history():

    db = SessionLocal()

    try:
        deleted_count = (
            db.query(PredictionHistory)
            .delete()
        )

        db.commit()

        return {
            "message": "History Cleared",
            "deleted_records": deleted_count
        }

    finally:
        db.close()