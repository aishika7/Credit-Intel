import { useEffect, useState } from "react";
import { getScoreNow } from "../lib/api";

export default function ScoreCard({ ticker }: { ticker: string }) {
  const [score, setScore] = useState<number | null>(null);

  useEffect(() => {
    getScoreNow(ticker).then(data => setScore(data.score));
  }, [ticker]);

  return (
    <div className="bg-white rounded-2xl shadow p-6">
      <h2 className="text-lg font-semibold mb-2">Current Credit Score</h2>
      <p className="text-3xl font-bold">{score !== null ? score.toFixed(2) : "Loading..."}</p>
    </div>
  );
}
