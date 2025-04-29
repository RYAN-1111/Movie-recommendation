// recommend.js
// Protect the page
// if (!localStorage.getItem("token")) {
//     window.location.href = "index.html";
// }

async function getRecommendations() {
    const movieName = document.getElementById("movieName").value;
    const token = localStorage.getItem("token");
    // const token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTc0NTkwNTAwNn0.-q9RiqNuWzFEW6VnjpK6yVfqjoMCmAot8G1KEsdNb8g"

    const response = await fetch(`http://localhost:8000/recommend?movie=${encodeURIComponent(movieName)}`, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    });

    const data = await response.json();

    if (response.ok) {
        console.log("Success:", data);
        displayRecommendations(data.recommended_movies);
    } else {
        alert(data.detail || "Failed to fetch recommendations.");
    }
}
function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html"; // Redirect to login page
}

function displayRecommendations(movies) {
    const container = document.getElementById("recommendations");
    container.innerHTML = "";
    movies.forEach(movie => {
        const card = document.createElement("div");
        card.className = "card";
        card.textContent = movie;
        container.appendChild(card);
    });
}
