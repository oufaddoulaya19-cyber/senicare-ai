const addRxBtn   = document.getElementById("addRxBtn");
const rxFile    = document.getElementById("rxFile");
const rxModal   = document.getElementById("rxModal");
const rxPreview = document.getElementById("rxPreview");
const rxHint    = document.getElementById("rxHint");
const closeModal= document.getElementById("closeModal");

console.log("OCR OK:", addRxBtn, rxFile, rxModal);

// OPEN FILE PICKER
addRxBtn.addEventListener("click", (e) => {
  e.preventDefault();        // 🚨 bloque submit
  e.stopPropagation();       // 🚨 bloque bubbling
  rxFile.click();
});

// FILE SELECTED
rxFile.addEventListener("change", () => {
  const file = rxFile.files[0];
  if (!file) return;

  console.log("FILE:", file.name);

  // Show modal
  rxModal.classList.remove("hidden");
  rxModal.classList.add("flex");

  // Preview
  rxPreview.src = URL.createObjectURL(file);
  rxPreview.classList.remove("hidden");
  rxHint.textContent = file.name;
});

// CLOSE MODAL
closeModal.addEventListener("click", () => {
  rxModal.classList.add("hidden");
  rxModal.classList.remove("flex");
  rxPreview.src = "";
  rxPreview.classList.add("hidden");
  rxFile.value = "";
});
