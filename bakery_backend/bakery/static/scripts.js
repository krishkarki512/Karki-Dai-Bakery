document.addEventListener("DOMContentLoaded", () => {

  const cakeGrid = document.getElementById("cakeGrid");

  // Hardcoded cakes
  const cakes = [
    {
      "id": 1,
      "name": "Orange Mille Crepes",
      "price": "115.00",
      "image": "https://media.istockphoto.com/id/1311664961/photo/matcha-mille-crepe-cake.webp"
    },
    {
      "id": 2,
      "name": "Tiramisu",
      "price": "200.00",
      "image": "https://imgs.search.brave.com/0dvC-7uChNkXD9dh6U8ZOsMspceqq908CC7j7URwIcc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTU0/OTQ3MzgxL3Bob3Rv/L3doaXRlLXBsYXRl/LW9mLWZyZWVmb3Jt/LX"
    },
    {
      "id": 3,
      "name": "Cheese Cake",
      "price": "150.00",
      "image": "https://imgs.search.brave.com/30JmH4KqQbmJIw4DbRMFWHI4R2yx_o8WnTlcm81x9F8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzAxLzcxLzMyLzUz/LzM2MF9GXzE3MTMy/NTM4NV9pZXlRdGNa/QXhzQWtiT0NRZEN6/b1"
    }
  ];

  // Render cakes
  cakeGrid.innerHTML = "";
  cakes.forEach(cake => {
    const div = document.createElement("div");
    div.className = "cake-card";
    div.innerHTML = `
      <img src="${cake.image}" alt="${cake.name}">
      <h3>${cake.name}</h3>
      <p>₹${cake.price}</p>
    `;
    cakeGrid.appendChild(div);
  });

  // Login alert
  window.loginAlert = () => alert("Login / Contact feature coming soon!");

  // Newsletter subscription
  window.subscribe = () => {
    const email = document.getElementById("newsletterEmail").value.trim();
    if (!email) return alert("Please enter an email address");
    alert(`${email} subscribed successfully!`);
    document.getElementById("newsletterEmail").value = "";
  };

});
