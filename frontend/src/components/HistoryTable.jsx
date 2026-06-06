import { useEffect, useState } from "react";
import API from "../services/api";

function HistoryTable() {
  const [history, setHistory] = useState([]);

  const loadHistory = async () => {
    try {
      const response = await API.get("/history");
      setHistory(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    loadHistory();
  }, []);

  const clearHistory = async () => {
    try {
      await API.delete("/history");
      setHistory([]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <button
        onClick={clearHistory}
        className="bg-red-500 text-white px-4 py-2 rounded mb-4"
      >
        Clear History
      </button>

      <table className="w-full border">
        <thead>
          <tr className="bg-gray-200">
            <th className="border p-2">ID</th>
            <th className="border p-2">Message</th>
            <th className="border p-2">Prediction</th>
            <th className="border p-2">Confidence</th>
            <th className="border p-2">Timestamp</th>
          </tr>
        </thead>

        <tbody>
          {history.map((item) => (
            <tr key={item.id}>
              <td className="border p-2">
                {item.id}
              </td>

              <td className="border p-2">
                {item.message}
              </td>

              <td
                className={`border p-2 font-bold ${
                  item.prediction === "Spam"
                    ? "text-red-600"
                    : "text-green-600"
                }`}
              >
                {item.prediction}
              </td>

              <td className="border p-2">
                {item.confidence}%
              </td>

              <td className="border p-2">
                {item.timestamp}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default HistoryTable;