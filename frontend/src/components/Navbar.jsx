import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-blue-600 text-white p-4 shadow-md">
      <div className="container mx-auto flex justify-between">
        <h1 className="font-bold text-xl">
          Spam Email Detector
        </h1>

        <div className="space-x-4">
          <Link to="/">Home</Link>
          <Link to="/history">History</Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;