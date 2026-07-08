"use client";

import { useState } from "react";
import { apiFetch } from "@/lib/api";
import { useRouter } from "next/navigation";

export default function Register() {
  const router = useRouter();

  const [form, setForm] = useState({
    firstname: "",
    lastname: "",
    email: "",
    password: ""
  });

  async function submit() {
    const res = await apiFetch("/auth/register", {
      method: "POST",
      body: JSON.stringify(form),
    });

    localStorage.setItem("token", res.access_token);

    router.push("/dashboard");
  }

  return (
    <div className="flex h-screen items-center justify-center bg-black text-white">
      <div className="bg-gray-900 p-8 rounded w-96">
        <h1 className="text-xl mb-4">Create Account</h1>

        {Object.keys(form).map((key) => (
          <input
            key={key}
            className="w-full p-2 mb-2 text-black"
            placeholder={key}
            onChange={(e) =>
              setForm({ ...form, [key]: e.target.value })
            }
          />
        ))}

        <button
          onClick={submit}
          className="w-full bg-green-600 p-2 mt-2"
        >
          Register
        </button>
      </div>
    </div>
  );
}