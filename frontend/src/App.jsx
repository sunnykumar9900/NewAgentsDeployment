
import { useState } from "react";

function App() {
  const [skills, setSkills] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    if (!skills.trim()) {
      alert("Please enter your skills");
      return;
    }

    setLoading(true);
    setResult("");
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/search-jobs", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ skills }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Job search failed");
      }

      setResult(data.result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Naukri Job Research Agent</h1>
      <p>Search job openings using AI</p>

      <input
        type="text"
        placeholder="Enter skills (e.g. Playwright, Python, Java)"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
      />

      <button onClick={handleSearch} disabled={loading}>
        {loading ? "Searching..." : "Search Jobs"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div>
          <h2>Job Search Results</h2>
          <pre style={{ whiteSpace: "pre-wrap" }}>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
