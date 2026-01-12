const API_BASE = "http://127.0.0.1:8000";

const emailEl = document.getElementById("email");
const passwordEl = document.getElementById("password");
const statusEl = document.getElementById("status");
const loginBtn = document.getElementById("loginBtn");

function setStatus(msg) {
  statusEl.textContent = msg;
  statusEl.classList.remove("hidden");
}

loginBtn.addEventListener("click", login);

async function login() {
  statusEl.classList.add("hidden");

  const email = emailEl.value.trim();
  const password = passwordEl.value;

  if (!email || !password) {
    setStatus("Veuillez saisir votre email et mot de passe.");
    return;
  }

  try {
    const res = await fetch(`${API_BASE}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (!res.ok || data.error) {
      setStatus(data.error || "Erreur lors de la connexion.");
      return;
    }

    // ✅ Stocke le user connecté
    localStorage.setItem("user_id", data.user_id);
    localStorage.setItem("prenom", data.prenom);
    localStorage.setItem("email", data.email);

    // ✅ Redirect vers chat
    window.location.href = "chat.html";

  } catch (e) {
    setStatus("Impossible de joindre le serveur backend.");
  }
}
