export default function Alerts({ ticker }: { ticker: string }) {
  return (
    <div className="bg-white rounded-2xl shadow p-4">
      <h2 className="font-semibold mb-2">Alerts</h2>
      <p className="text-sm text-gray-600">No alerts for {ticker} yet.</p>
    </div>
  );
}
