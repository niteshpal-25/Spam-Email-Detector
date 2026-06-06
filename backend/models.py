from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float

class Base(DeclarativeBase):
    pass


class PredictionHistory(Base):

    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True)

    message = Column(String)

    prediction = Column(String)

    confidence = Column(Float)

    timestamp = Column(String)