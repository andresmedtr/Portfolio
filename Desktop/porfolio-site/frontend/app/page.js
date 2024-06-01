"use client";

import Image from "next/image";

export default function Home() {
  const response = fetch("http://127.0.0.1:5000/projects")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Parse the JSON response
    })
    .then((data) => {
      // Handle the data received from the backend
      console.log(data);
    })
    .catch((error) => {
      // Handle any errors that occur during the fetch operation
      console.error("Fetch error:", error);
    });
  return (
    <main className="">
      <h1>TEST</h1>
    </main>
  );
}
