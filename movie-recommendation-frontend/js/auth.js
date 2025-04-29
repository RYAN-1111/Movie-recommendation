// auth.js

const API_BASE_URL = "http://localhost:8000"; // your FastAPI backend

document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");

    if (loginForm) {
        loginForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            const response = await fetch(`${API_BASE_URL}/token`, {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: new URLSearchParams({ username, password })
            });

            const data = await response.json();

            if (response.ok) {
                localStorage.setItem("token", data.access_token);
                window.location.href = "recommend.html"; // Go to recommend page
            } else {
                alert(data.detail || "Login failed");
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;
            const email=document.getElementById("email").value;

            const response = await fetch(`${API_BASE_URL}/register`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username,email,password })
            });

            const data = await response.json();

            if (response.ok) {
                alert("Registered successfully! Please login.");
                window.location.href = "index.html"; // Go to login
            } else {
                alert(data.detail || "Registration failed");
            }
        });
    }
});
