async function sendReview() {
  const review = document.getElementById("review").value;
  const res = await fetch("/predict", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({review})
  });
  const data = await res.json();
  document.getElementById("result").innerText = "Sentiment: " + data.sentiment;
}
