import { Link } from "react-router-dom";
import Header from "./Header";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <Header />
      <nav className="bg-white shadow px-6 py-4 flex gap-6">
        <Link to="/" className="hover:text-blue-600">Dashboard</Link>
        <Link to="/alerts" className="hover:text-blue-600">Alerts</Link>
        <Link to="/settings" className="hover:text-blue-600">Settings</Link>
      </nav>
      <main className="p-6">{children}</main>
    </div>
  );
}
