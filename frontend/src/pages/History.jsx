import HistoryTable from "../components/HistoryTable";

function History() {
  return (
    <div className="container mx-auto p-6">
      <h2 className="text-3xl font-bold mb-4">
        Prediction History
      </h2>

      <HistoryTable />
    </div>
  );
}

export default History;