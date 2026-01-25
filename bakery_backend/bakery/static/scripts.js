document.addEventListener("DOMContentLoaded", () => {

  const searchBar = document.getElementById("searchBar");

  if (searchBar) {
    searchBar.addEventListener("keyup", () => {
      const searchValue = searchBar.value.toLowerCase();
      const cakeCards = document.querySelectorAll(".cake-card");

      let found = false;

      cakeCards.forEach(card => {
        const nameElement = card.querySelector("h3");
        const originalText = nameElement.innerText;
        const cakeName = originalText.toLowerCase();

        // Reset previous highlight
        nameElement.innerHTML = originalText;

        if (cakeName.includes(searchValue)) {
          card.style.display = "block";
          found = true;

          // 🔥 HIGHLIGHT MATCH IN YELLOW
          if (searchValue !== "") {
            const regex = new RegExp(`(${searchValue})`, "gi");
            nameElement.innerHTML = originalText.replace(
              regex,
              `<span style="background: yellow;">$1</span>`
            );
          }
        } else {
          card.style.display = "none";
        }
      });

      // ✅ Show "No results found"
      let noResult = document.getElementById("noResult");

      if (!found) {
        if (!noResult) {
          noResult = document.createElement("h3");
          noResult.id = "noResult";
          noResult.style.color = "red";
          noResult.style.textAlign = "center";
          noResult.innerText = "❌ No results found";
          document.getElementById("cakeGrid").appendChild(noResult);
        }
      } else if (noResult) {
        noResult.remove();
      }
    });
  }

  // ===== LOGIN ALERT =====
  window.loginAlert = () => {
    alert("Login / Contact feature coming soon!");
  };

  // ===== NEWSLETTER SUBSCRIPTION =====
  window.subscribe = () => {
    const emailInput = document.getElementById("newsletterEmail");
    const email = emailInput.value.trim();

    if (!email) {
      alert("Enter an email!");
      return;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
      alert("Invalid email!");
      return;
    }

    alert(`Thank you! ${email} subscribed successfully.`);
    emailInput.value = "";
  };

});
