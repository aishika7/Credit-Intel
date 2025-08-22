interface Props {
  issuers: string[];
  selected: string;
  onChange: (ticker: string) => void;
}

export default function Filters({ issuers, selected, onChange }: Props) {
  return (
    <div className="bg-white rounded-2xl shadow p-4 mb-6">
      <h2 className="font-semibold mb-2">Select Issuer</h2>
      <select
        className="w-full border rounded p-2"
        value={selected}
        onChange={(e) => onChange(e.target.value)}
      >
        {issuers.map((ticker) => (
          <option key={ticker} value={ticker}>
            {ticker}
          </option>
        ))}
      </select>
    </div>
  );
}
