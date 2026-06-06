import PredictionForm from "../components/PredictionForm";

function Home() {
  return (
    <div className="container mx-auto p-6">
      <div className="text-center mb-6">
        <h1 className="text-4xl font-bold">
          Spam Email Detector
        </h1>

        <p className="text-gray-600 mt-2">
          Detect spam emails using Machine Learning
        </p>
      </div>

      <PredictionForm />
    </div>
  );
}

export default Home;