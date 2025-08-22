import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api", // backend url
});
const API_BASE =
  (typeof import.meta !== "undefined" && import.meta.env?.VITE_API_URL) ||
  (typeof process !== "undefined" && process.env?.VITE_API_URL) ||
  "http://localhost:8000";

export const api = axios.create({
  baseURL: API_BASE,
  withCredentials: false,
});
export async function getIssuers() {
  const res = await API.get("/issuers");
  return res.data;
}

export async function getScores(ticker: string) {
  const res = await API.get(`/scores/${ticker}`);
  return res.data;
}

export async function getFeatures(ticker: string) {
  const res = await API.get(`/features/${ticker}`);
  return res.data;
}

export async function getEvents(ticker: string) {
  const res = await API.get(`/events/${ticker}`);
  return res.data;
}

export async function getScoreNow(ticker: string) {
  const res = await API.get(`/score-now/${ticker}`);
  return res.data;
}
