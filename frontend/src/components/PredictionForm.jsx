import { useState } from "react";
import API from "../services/api";
import Loader from "./Loader";
import PredictionResult from "./PredictionResult";

function PredictionForm() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handlePredict = async () => {
    if (!message.trim()) {
      setError("Please enter email content");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const response = await API.post("/predict", {
        message,
      });

      setResult(response.data);
    } catch (err) {
      console.error(err);
      setError("Failed to connect to server");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <textarea
        rows="8"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter email content..."
        className="w-full border rounded p-3"
      />

      {error && (
        <p className="text-red-500 mt-2">{error}</p>
      )}

      <button
        onClick={handlePredict}
        className="bg-blue-600 text-white px-5 py-2 rounded mt-3"
      >
        Predict
      </button>

      {loading && <Loader />}

      {result && (
        <PredictionResult result={result} />
      )}
    </div>
  );
}

export default PredictionForm;