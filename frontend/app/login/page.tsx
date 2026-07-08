"use client";

import { useState } from "react";
import { apiFetch } from "@/lib/api";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function login() {
    const res = await apiFetch("/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });

    localStorage.setItem("token", res.access_token);

    router.push("/dashboard");
  }

  return (
    <div className="flex h-screen items-center justify-center bg-gray-950">
      <div className="bg-gray-900 p-8 rounded-xl w-96">
        <h1 className="text-white text-2xl mb-6">Argyros Login</h1>

        <input
          className="w-full p-2 mb-3"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          className="w-full p-2 mb-3"
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={login}
          className="w-full bg-blue-600 text-white p-2 rounded"
        >
          Login
        </button>
      </div>
    </div>
  );
}