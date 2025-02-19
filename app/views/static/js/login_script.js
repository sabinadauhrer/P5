document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("loginForm").addEventListener("submit", function(event) {
        let username = document.getElementById("username").value.trim();
        let password = document.getElementById("password").value.trim();
        let errorMessage = document.getElementById("error-message");

        if (username === "" || password === "") {
            event.preventDefault();
            errorMessage.textContent = "Bitte gib Login-Daten an.";
            errorMessage.style.display = "block";
        } else {
            errorMessage.style.display = "none";
            // Das Formular wird gesendet und die Weiterleitung erfolgt
        }
    });

    // Passwort-Anzeige ein-/ausschalten
    document.getElementById("togglePassword").addEventListener("click", function() {
        let passwordField = document.getElementById("password");

        if (passwordField.type === "password") {
            passwordField.type = "text";
            this.classList.replace("fa-eye", "fa-eye-slash");
        } else {
            passwordField.type = "password";
            this.classList.replace("fa-eye-slash", "fa-eye");
        }
    });
});