function PredictionResult({ result }) {
  if (!result) return null;

  return (
    <div
      className={`mt-5 p-4 rounded shadow ${
        result.prediction === "Spam"
          ? "bg-red-100 border border-red-500"
          : "bg-green-100 border border-green-500"
      }`}
    >
      <h2 className="text-xl font-bold">
        {result.prediction}
      </h2>

      <p>
        Confidence: {result.confidence}%
      </p>

      <p>
        Timestamp: {result.timestamp}
      </p>
    </div>
  );
}

export default PredictionResult;