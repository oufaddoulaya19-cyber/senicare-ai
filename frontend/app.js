const API = "http://127.0.0.1:8000";

async function sendMessage() {
  const msg = document.getElementById("message").value;
  const responseBox = document.getElementById("response");

  if (!msg.trim()) {
    responseBox.innerText = "Écris un message.";
    return;
  }

  try {
    const res = await fetch(`${API}/chat/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: msg
      })
    });

    if (!res.ok) {
      throw new Error("Backend error");
    }

    const data = await res.json();
    responseBox.innerText = data.response;

  } catch (err) {
    console.error(err);
    responseBox.innerText = "Erreur : backend indisponible.";
  }
}
