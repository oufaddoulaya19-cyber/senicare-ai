const API_BASE = "http://127.0.0.1:8000";

const statusEl = document.getElementById("status");
const registerBtn = document.getElementById("registerBtn");

function setStatus(msg) {
  statusEl.textContent = msg;
  statusEl.classList.remove("hidden");
}

registerBtn.addEventListener("click", register);

async function register() {
  statusEl.classList.add("hidden");

  const data = {
    nom: document.getElementById("nom").value.trim(),
    prenom: document.getElementById("prenom").value.trim(),
    age: parseInt(document.getElementById("age").value, 10),
    email: document.getElementById("email").value.trim(),
    password: document.getElementById("password").value,
    maladies: document.getElementById("maladies").value.trim(),
    allergies: document.getElementById("allergies").value.trim(),
    adresse: document.getElementById("adresse").value.trim(),
    emergency_phone: document.getElementById("emergency").value.trim(),
  };

  if (!data.nom || !data.prenom || !data.email || !data.password || !data.age) {
    setStatus("Veuillez remplir les champs obligatoires.");
    return;
  }

  try {
    const res = await fetch(`${API_BASE}/auth/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const json = await res.json();

    if (!res.ok || json.error) {
      setStatus(json.error || "Erreur lors de l'inscription.");
      return;
    }

    alert("Compte créé avec succès. Veuillez vous connecter.");
    window.location.href = "login.html";

  } catch (e) {
    setStatus("Impossible de joindre le serveur backend.");
  }
}
