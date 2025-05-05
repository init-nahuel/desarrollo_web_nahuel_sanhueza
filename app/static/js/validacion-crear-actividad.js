// Auxiliary functions

const showConfirmation = (submitButton, divElement, visibility) => {
  divElement.style = visibility ? "visibility: visible" : "visibility: hidden";
  submitButton.style = visibility
    ? "visibility: hidden"
    : "visibility: visible";
};

const removeAlert = (elementId) => {
  const pNode = document.getElementById(elementId);
  if (pNode) {
    pNode.remove();
  }
};

// Validation Functions

const validateProductoPhotos = (productFilesElement) => {
  removeAlert("alertProductFiles");

  const checkFilesValidation =
    productFilesElement.files.length >= 1 &&
    productFilesElement.files.length <= 5;

  if (!checkFilesValidation) {
    const alertProductFiles = document.createElement("p");
    alertProductFiles.id = "alertProductFiles";
    alertProductFiles.innerText = "Porfavor seleccione 1 a 5 fotos";
    alertProductFiles.style = "color: var(--bs-warning-text-emphasis)";
    productFilesElement.parentElement.appendChild(alertProductFiles);

    return false;
  }

  return true;
};

const validateObligatoryInput = (inputElement) => {
  removeAlert("alertObligatoryInput");

  if (!inputElement.value) {
    const alertObligatoryInput = document.createElement("p");
    alertObligatoryInput.id = "alertObligatoryInput";
    alertObligatoryInput.innerText = "Porfavor complete este campo";
    alertObligatoryInput.style = "color: var(--bs-warning-text-emphasis)";
    inputElement.parentElement.appendChild(alertObligatoryInput);

    return false;
  }

  return true;
};

const validatePhone = (inputPhoneElement) => {
  removeAlert("alertPhone");

  const phoneRegex = /^(\+569|9)\s?\d{8}$/;

  if (!phoneRegex.test(inputPhoneElement.value)) {
    const alertPhone = document.createElement("p");
    alertPhone.id = "alertPhone";
    alertPhone.innerText = "Porfavor ingrese un número de teléfono válido";
    alertPhone.style = "color: var(--bs-warning-text-emphasis)";
    inputPhoneElement.parentElement.appendChild(alertPhone);

    return false;
  }

  return true;
};

const validateEmail = (inputEmailElement) => {
  removeAlert("alertEmail");

  const emailRegex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;

  if (!emailRegex.test(inputEmailElement.value)) {
    const alertEmail = document.createElement("p");
    alertEmail.id = "alertEmail";
    alertEmail.innerText = "Porfavor ingrese un email válido";
    alertEmail.style = "color: var(--bs-warning-text-emphasis)";
    inputEmailElement.parentElement.appendChild(alertEmail);

    return false;
  }

  return true;
};

const validateTema = (selectTemaElement, temaInput) => {
  removeAlert("alertTema");

  if (selectTemaElement.value === "otro" && !temaInput.value) {
    const alertTema = document.createElement("p");
    alertTema.id = "alertTema";
    alertTema.innerText = "Porfavor escriba un tema";
    alertTema.style = "color: var(--bs-warning-text-emphasis)";
    selectTemaElement.parentElement.appendChild(alertTema);

    return false;
  }

  return true;
};

// Handling function form

const handleFormSubmit = (event) => {
  // DOM Elements

  const actividadFilesInput = document.getElementById("inputFotos");

  const selectRegion = document.getElementById("selectRegion");
  const selectComuna = document.getElementById("selectComuna");

  const organizadorInputName = document.getElementById("nombreOrganizador");
  const organizadorInputEmail = document.getElementById("emailOrganizador");
  const organizadorInputPhone = document.getElementById("telefonoOrganizador");
  const divConfirmation = document.getElementById("confirmarAgregarActividad");

  const diaHoraInicioInput = document.getElementById("diaHoraInicio");
  const temaInput = document.getElementById("tema");

  const selectTema = document.getElementById("selectTema");

  let isValid =
    validateObligatoryInput(selectRegion) &&
    validateObligatoryInput(selectComuna) &&
    validateObligatoryInput(organizadorInputName) &&
    validateObligatoryInput(organizadorInputEmail) &&
    validateEmail(organizadorInputEmail) &&
    validatePhone(organizadorInputPhone) &&
    validateObligatoryInput(diaHoraInicioInput) &&
    validateObligatoryInput(selectTema) &&
    validateTema(selectTema, temaInput) &&
    validateProductoPhotos(actividadFilesInput);

  if (!isValid) {
    showConfirmation(submitFormButton, divConfirmation, false);
    event.preventDefault();
  } else {
    showConfirmation(submitFormButton, divConfirmation, true);

    event.preventDefault();
  }
};

const handleConfirmation = (event) => {
  const confirmationMessage = document.getElementById("confirmationMessage");
  const askMessage = document.getElementById("confirmarAgregarActividad");
  askMessage.style = "visibility: hidden";
  confirmationMessage.style = "visibility: visible;";
};

// DOM Elements
const submitFormButton = document.getElementById("agregarActividad");
const confirmationButton = document.getElementById("agregarActividadSubmit");
const denyButton = document.getElementById("denyAgregarActividadSubmit");
const volverButton = document.getElementById("volverInicioButton");

// Event Listener

submitFormButton.addEventListener("click", handleFormSubmit);
confirmationButton.addEventListener("click", handleConfirmation);
denyButton.addEventListener("click", () => {
  const divConfirmation = document.getElementById("confirmarAgregarActividad");
  showConfirmation(submitFormButton, divConfirmation, false);
});
volverButton.addEventListener("click", () => {
  window.location.href = "home.html";
});
