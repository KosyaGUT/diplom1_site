function checkFormlog() {
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const submitButton = document.getElementById("submitButton");

    // Проверка, все ли условия выполнены и пароль не короче 6 символов
    if (email !== "" && password.length >= 6) {
        submitButton.disabled = false;
        submitButton.classList.remove("disabled-button");
        submitButton.classList.add("active-button");
    } else {
        submitButton.disabled = true;
        submitButton.classList.remove("active-button");
        submitButton.classList.add("disabled-button");
    }
}

// Применяем функцию на изменение полей ввода и чекбоксов
document.getElementById("email").addEventListener("input", checkFormlog);
document.getElementById("password").addEventListener("input", checkFormlog);


