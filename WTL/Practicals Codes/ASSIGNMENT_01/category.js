// category.js

const data = {
  breads: {
    title: "Breads",
    desc: "Fresh & warm breads baked everyday.",
    items: [
      { name: "Garlic Bread", price: "₹129", img: "https://plus.unsplash.com/premium_photo-1711752902734-a36167479983?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Z2FybGljJTIwYnJlYWR8ZW58MHx8MHx8fDA%3D" },
      { name: "Sourdough", price: "₹149", img: "https://images.unsplash.com/photo-1686154596696-d6f594a98af9?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" },
      { name: "Whole Wheat Bread", price: "₹99", img: "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8d2hvbGUlMjB3aGVhdCUyMGJyZWFkfGVufDB8fDB8fHww" },
      { name: "Multigrain Bread", price: "₹119", img: "https://plus.unsplash.com/premium_photo-1667806841164-cf286c7dc582?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bXVsdGlncmFpbiUyMGJyZWFkfGVufDB8fDB8fHww" },
      { name: "Focaccia", price: "₹200", img: "https://plus.unsplash.com/premium_photo-1700326967443-e08175e6975c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzJ8fGZvY2NhY2lhfGVufDB8fDB8fHww" }
    ]
  },

  cakes: {
    title: "Cakes",
    desc: "Premium layered cakes with rich flavours.",
    items: [
      { name: "Chocolate Truffle Cake", price: "₹549", img: "https://images.unsplash.com/photo-1594223801958-db8561d7009a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzZ8fGNob2Nsb2F0ZSUyMHRydWZmbGUlMjBjYWtlfGVufDB8fDB8fHww" },
      { name: "Red Velvet Cake", price: "₹599", img: "https://plus.unsplash.com/premium_photo-1713920189815-876dbdf5f56e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cmVkJTIwdmVsdmV0JTIwY2FrZXxlbnwwfHwwfHx8MA%3D%3D" },
      { name: "Butterscotch Cake", price: "₹499", img: "https://images.unsplash.com/photo-1619867994225-724b17475220?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGJ1dHRlcnNjb3RjaCUyMGNha2V8ZW58MHx8MHx8fDA%3D" },
      { name: "Black Forest Cake", price: "₹549", img: "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1000&q=80" }
    ]
  },

  donuts: {
    title: "Donuts",
    desc: "Soft donuts with premium glaze.",
    items: [
      { name: "Chocolate Glaze Donut", price: "₹149", img: "https://images.unsplash.com/photo-1551024601-bec78aea704b?auto=format&fit=crop&w=1000&q=80" },
      { name: "Strawberry Frost Donut", price: "₹159", img: "https://images.unsplash.com/photo-1551106652-a5bcf4b29ab6?auto=format&fit=crop&w=1000&q=80" },
      { name: "Caramel Crunch Donut", price: "₹169", img: "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?auto=format&fit=crop&w=1000&q=80" }
    ]
  },

  brownies: {
    title: "Brownies",
    desc: "Soft donuts with premium glaze.",
    items: [
      { name: "S’mores Brownies ", price: "₹149", img: "https://media.istockphoto.com/id/1223831981/photo/smore-brownie.webp?a=1&b=1&s=612x612&w=0&k=20&c=CEdDu0TCMnauwM3T-lLtILBShhwWOckDE04dvKB3da0=" },
      { name: "Walnut Brownies", price: "₹159", img: "https://images.pexels.com/photos/33813613/pexels-photo-33813613.jpeg" },
      { name: "Caramel Crunch Brownies", price: "₹169", img: "https://images.pexels.com/photos/31745180/pexels-photo-31745180.jpeg" }
    ]
  }
};


function getCategoryType() {
  const params = new URLSearchParams(window.location.search);
  return params.get("type");
}

function renderCategory(type) {
  const category = data[type];

  const titleEl = document.getElementById("catTitle");
  const descEl = document.getElementById("catDesc");
  const grid = document.getElementById("itemsGrid");

  if (!category) {
    titleEl.textContent = "Category Not Found";
    descEl.textContent = "Please go back and select a valid product category.";
    grid.innerHTML = "";
    return;
  }

  titleEl.textContent = category.title;
  descEl.textContent = category.desc;

  grid.innerHTML = category.items.map(item => `
    <div class="card">
      <img src="${item.img}" alt="${item.name}">
      <h4>${item.name}</h4>
      <p>Freshly baked with premium ingredients.</p>
      <div class="price">${item.price}</div>
      <a class="btn primary" style="margin-top:12px; width:100%;" href="products.html#order">Order Online</a>
    </div>
  `).join("");
}

const type = getCategoryType();
renderCategory(type);
