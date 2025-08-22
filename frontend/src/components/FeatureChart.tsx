import { useEffect, useState } from "react";
import { getFeatures } from "../lib/api";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function FeatureChart({ ticker }: { ticker: string }) {
  const [data, setData] = useState([]);

  useEffect(() => {
    getFeatures(ticker).then(res => {
      const formatted = Object.entries(res.shap).map(([name, val]) => ({ name, value: val }));
      setData(formatted);
    });
  }, [ticker]);

  return (
    <div className="bg-white rounded-2xl shadow p-6 h-80">
      <h2 className="text-lg font-semibold mb-4">Feature Importance</h2>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="value" fill="#16a34a" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
