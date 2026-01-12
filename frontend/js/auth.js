const API_BASE = "http://127.0.0.1:8000";

// Helpers
function setSession(user) {
  localStorage.setItem("user_id", user.user_id || user.id || "");
  localStorage.setItem("prenom", user.prenom || user.first_name || "");
  localStorage.setItem("email", user.email || "");
}

function clearSession() {
  localStorage.removeItem("user_id");
  localStorage.removeItem("prenom");
  localStorage.removeItem("email");
}

// Login
const loginForm = document.getElementById("loginForm");
if (loginForm) {
  const status = document.getElementById("status");
  const clearBtn = document.getElementById("clearSession");

  clearBtn?.addEventListener("click", () => {
    clearSession();
    status.textContent = "Session locale effacée.";
  });

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    status.textContent = "Connexion...";

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    try {
      const res = await fetch(`${API_BASE}/auth/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, password })
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.detail || "Login failed");

      // ATTENDU: { user_id, prenom, email }
      setSession(data);

      status.textContent = "OK. Redirection...";
      window.location.href = "chat.html";
    } catch (err) {
      console.error(err);
      status.textContent = "Erreur: email/mot de passe incorrect ou backend indisponible.";
    }
  });
}

// Register
const registerForm = document.getElementById("registerForm");
if (registerForm) {
  const status = document.getElementById("status");

  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    status.textContent = "Création du compte...";

    const prenom = document.getElementById("prenom").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    try {
      const res = await fetch(`${API_BASE}/auth/register`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ prenom, email, password })
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.detail || "Register failed");

      status.textContent = "Compte créé. Redirection vers login...";
      setTimeout(() => window.location.href = "login.html", 700);
    } catch (err) {
      console.error(err);
      status.textContent = "Erreur: impossible de créer le compte.";
    }
  });
}
