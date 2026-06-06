import pandas as pd
import joblib

from utils import clean_text

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv(
    "dataset/spam.csv"
)

# Convert Labels
df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

# Clean Text
df["message"] = df["message"].apply(
    clean_text
)

X = df["message"]
y = df["label"]

# TF-IDF
vectorizer = TfidfVectorizer(
    stop_words="english"
)

X_vectorized = vectorizer.fit_transform(X)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = MultinomialNB()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    f"Accuracy: {accuracy*100:.2f}%"
)

# Save Files
joblib.dump(
    model,
    "model.pkl"
)

joblib.dump(
    vectorizer,
    "vectorizer.pkl"
)

print("Model Saved")