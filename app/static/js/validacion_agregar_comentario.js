const removeAlert = (elementId) => {
  const alertElement = document.getElementById(elementId);
  if (alertElement) {
    alertElement.remove();
  }
};

const showAlert = (element, alertId, message) => {
  removeAlert(alertId);

  const alertElement = document.createElement("p");
  alertElement.id = alertId;
  alertElement.innerText = message;
  alertElement.style = "color: var(--bs-warning-text-emphasis)";
  element.parentElement.appendChild(alertElement);
};

const validarComentario = () => {
  const nombre = document.getElementById("nombreComentario");
  const comentario = document.getElementById("comentario");

  let isValid = true;

  if (nombre.value.length < 3 || nombre.value.length > 80) {
    showAlert(
      nombre,
      "alertNombreComentario",
      "El nombre debe tener entre 3 y 80 caracteres."
    );
    isValid = false;
  } else {
    removeAlert("alertNombreComentario");
  }

  if (comentario.value.length < 5) {
    showAlert(
      comentario,
      "alertComentario",
      "El comentario debe tener al menos 5 caracteres."
    );
    isValid = false;
  } else {
    removeAlert("alertComentario");
  }

  return isValid;
};

const enviarComentario = async (event) => {
  event.preventDefault();

  if (!validarComentario()) {
    return;
  }

  const form = event.target;
  const formData = new FormData(form);

  const data = {
    nombreComentario: formData.get("nombreComentario"),
    comentario: formData.get("comentario"),
  };

  try {
    const response = await fetch(
      "http://127.0.0.1:5000/post_agregar_comentario",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      }
    );

    if (response.ok) {
      const result = await response.json();
      alert("Comentario enviado exitosamente.");
      form.reset();
    } else {
      console.error("Error al enviar el comentario:", response.statusText);
      alert("Hubo un error al enviar el comentario.", response.statusText);
    }
  } catch (error) {
    console.error("Error de red:", error);
    alert("Hubo un error de red.");
  }
};

const agregarComentarioForm = document.getElementById("agregarComentarioForm");
agregarComentarioForm.addEventListener("submit", enviarComentario);
