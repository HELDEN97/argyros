"use client";

import { useEffect, useState } from "react";
import { apiFetch } from "@/lib/api";

export default function Dashboard() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    load();
  }, []);

  async function load() {
    const res = await apiFetch("/dashboard");
    setData(res);
  }

  if (!data) {
    return <div className="p-10">Loading...</div>;
  }

  return (
    <div className="p-10 bg-gray-950 min-h-screen text-white">
      <h1 className="text-3xl font-bold mb-6">Argyros Dashboard</h1>

      <div className="grid grid-cols-3 gap-4">
        <div className="bg-gray-800 p-4 rounded">
          <h2>Income</h2>
          <p>{data.finance.income} €</p>
        </div>

        <div className="bg-gray-800 p-4 rounded">
          <h2>Expense</h2>
          <p>{data.finance.expense} €</p>
        </div>

        <div className="bg-gray-800 p-4 rounded">
          <h2>Savings</h2>
          <p>{data.finance.savings} €</p>
        </div>
      </div>

      <div className="mt-10">
        <h2 className="text-xl mb-4">Goals</h2>

        {data.goals.map((g: any, i: number) => (
          <div key={i} className="bg-gray-800 p-3 mb-2 rounded">
            <p>{g.title}</p>
            <p>{g.progress}%</p>
          </div>
        ))}
      </div>
    </div>
  );
}