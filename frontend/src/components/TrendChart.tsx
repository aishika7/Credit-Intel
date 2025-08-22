import { useEffect, useState } from "react";
import { getScores } from "../lib/api";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function TrendChart({ ticker }: { ticker: string }) {
  const [data, setData] = useState([]);

  useEffect(() => {
    getScores(ticker).then(setData);
  }, [ticker]);

  return (
    <div className="bg-white rounded-2xl shadow p-6 h-80">
      <h2 className="text-lg font-semibold mb-4">Score Trend</h2>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <XAxis dataKey="ts" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="score" stroke="#2563eb" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
