import ScoreCard from "../components/ScoreCard";
import TrendChart from "../components/TrendChart";
import FeatureChart from "../components/FeatureChart";
import EventsFeed from "../components/EventsFeed";

export default function Dashboard() {
  return (
    <div className="grid grid-cols-12 gap-6">
      <div className="col-span-12 md:col-span-4">
        <ScoreCard />
      </div>
      <div className="col-span-12 md:col-span-8">
        <TrendChart />
      </div>
      <div className="col-span-12 md:col-span-6">
        <FeatureChart />
      </div>
      <div className="col-span-12 md:col-span-6">
        <EventsFeed />
      </div>
    </div>
  );
}
