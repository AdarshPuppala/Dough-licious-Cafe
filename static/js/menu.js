// This function scrolls to the desire menu
function scrollToMenu(sectionId) {
    var section = document.getElementById(sectionId);
    if (section) {
      window.scrollTo({
        top: section.offsetTop,
        behavior: 'smooth'
      });
    }
  }

// This function adds item to local storage
const addToCart = function(item) {
    let cartItems = JSON.parse(localStorage.getItem("cartItems")) || [];
    cartItems.push(item);
    localStorage.setItem("cartItems", JSON.stringify(cartItems));
};

document.addEventListener("DOMContentLoaded", function() {
    // Add event listener to all "Add to Cart" buttons
    const addToCartBtns = document.querySelectorAll(".add-to-cart-btn");
    addToCartBtns.forEach(function(btn) {
        btn.addEventListener("click", function(event) {  
            // Retrieve selected item details
            const cardBody = btn.closest(".menu-card-body");

            const flavorSelect = cardBody.querySelector(".flavor-select");
            const selectedFlavor = flavorSelect.value;

            const sizeSelect = cardBody.querySelector(".size-select");
            const selectedSize = sizeSelect.value;

            const quantityInput = cardBody.querySelector(".quantity-control input");
            const quantity = parseInt(quantityInput.value);

            // Retrieve price data associated with the selected item
            const pricesData = cardBody.parentElement.dataset.prices.replace(/'/g, '"');

            const prices = JSON.parse(pricesData);

            const price = prices[selectedSize];

            let totalPrice; // Define totalPrice here

            // Check if the price is valid
            totalPrice = price * quantity;
            
            // Check if the menu item is a latte
            let productType = "";
            const menuCardTitle = cardBody.querySelector(".menu-card-title");
            if (menuCardTitle.innerText.trim() === "Latte") {
                productType = "Latte";
            } else if(menuCardTitle.innerText.trim() === "Macchiato") {
                productType = "Macchiato";
            } else if(menuCardTitle.innerText.trim() === "Cappuccino"){
                productType = "Cappuccino"
            } else if(menuCardTitle.innerText.trim() === "Espresso Shot") { 
                productType = "Espresso"
            } else if(menuCardTitle.innerText.trim() === "Original Glaze") { 
                productType = "Original Glaze"
            } else if(menuCardTitle.innerText.trim() === "Strawberry Glaze") { 
                productType = "Strawberry Glaze"
            } else if(menuCardTitle.innerText.trim() === "Vanilla Glaze") { 
                productType = "Vanilla Glaze"
            } else if(menuCardTitle.innerText.trim() === "Chocolate Glaze") { 
                productType = "Chocolate Glaze"
            } else if(menuCardTitle.innerText.trim() === "Boston Cream"){
                productType = "Boston Cream"
            } else if(menuCardTitle.innerText.trim() === "Jelly"){
                productType = "Jelly"
            } else if(menuCardTitle.innerText.trim() === "Maple Bacon"){
                productType = "Maple Bacon"
            } else if(menuCardTitle.innerText.trim() === "S'more"){
                productType = "S'more"
            } else if(menuCardTitle.innerText.trim() === "Cruller"){
                productType = "Cruller"
            } else if(menuCardTitle.innerText.trim() === "Peanut Butter and Jelly"){
                productType = "Peanut Butter and Jelly"
            } else if(menuCardTitle.innerText.trim() === "Blueberry Cake"){
                productType = "Blueberry Cake"
            } 

            // Create item object
            const item = {
                productType: productType,
                flavor: selectedFlavor,
                size: selectedSize,
                quantity: quantity,
                totalPrice: totalPrice
            };

            console.log(item);
            // Add item to local storage
            addToCart(item);

            const popup = document.createElement("div");
            popup.textContent = "Added to Cart 🛒 🥳";
            popup.classList.add("popup-message");
            document.body.appendChild(popup);

            popup.style.display = "block";

            // Hide the popup after 2 seconds
            setTimeout(() => {
                popup.style.display = "none";
            }, 2000);
        });
    });
});
