import { useEffect, useState } from "react";
import { getEvents } from "../lib/api";

export default function EventsFeed({ ticker }: { ticker: string }) {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    getEvents(ticker).then(setEvents);
  }, [ticker]);

  return (
    <div className="bg-white rounded-2xl shadow p-6">
      <h2 className="text-lg font-semibold mb-4">Recent News</h2>
      <ul className="space-y-2">
        {events.map((e: any) => (
          <li key={e.id} className="border-b pb-2">
            <a href={e.url} target="_blank" className="text-blue-600 hover:underline">{e.headline}</a>
            <p className="text-sm text-gray-600">{new Date(e.published_at).toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
