import { useEffect, useState } from "react";
import Header from "./components/Header";
import Filters from "./components/Filters";
import ScoreCard from "./components/ScoreCard";
import TrendChart from "./components/TrendChart";
import FeatureChart from "./components/FeatureChart";
import EventsFeed from "./components/EventsFeed";
import Alerts from "./components/Alerts";
import { getIssuers } from "./lib/api";

export default function App() {
  const [issuer, setIssuer] = useState<string>("AAPL");
  const [issuers, setIssuers] = useState<string[]>([]);

  useEffect(() => {
    getIssuers().then(data => setIssuers(data.map((i: any) => i.ticker)));
  }, []);

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="p-6 grid grid-cols-1 lg:grid-cols-4 gap-6">
        <div className="lg:col-span-1">
          <Filters issuers={issuers} selected={issuer} onChange={setIssuer} />
          <Alerts ticker={issuer} />
        </div>
        <div className="lg:col-span-3 space-y-6">
          <ScoreCard ticker={issuer} />
          <TrendChart ticker={issuer} />
          <FeatureChart ticker={issuer} />
          <EventsFeed ticker={issuer} />
        </div>
      </main>
    </div>
  );
}
