document.addEventListener("DOMContentLoaded", function() {
    // Function to display cart items from local storage
    const displayCartItems = function() {
        const cartItemsTable = document.getElementById("cart-items-table");
        const totalItemsCount = document.getElementById("total-items-count");
        const totalPrice = document.getElementById("total-price");

        cartItemsTable.innerHTML = ""; // Clear previous content. This prevents duplication

        const cartItems = JSON.parse(localStorage.getItem("cartItems")) || [];
        console.log(cartItems);
        let totalItems = 0;
        let totalPriceValue = 0;

        cartItems.forEach(function(item) {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${item.productType} - ${item.flavor} - ${item.size}</td>
                <td>${item.quantity}</td>
                <td>${item.totalPrice ? '$' + item.totalPrice.toFixed(2) : 'N/A'}</td>
            `;
            cartItemsTable.appendChild(row); //append the latest row to the checkout table

            totalItems += item.quantity;
            totalPriceValue += item.totalPrice || 0; // Use 0 if totalPrice is not defined
        });

        totalItemsCount.textContent = totalItems;
        totalPrice.textContent = totalPriceValue.toFixed(2);
    };

    // Call displayCartItems when the page loads
    displayCartItems();

    // Function to clear cart items from local storage
    const clearCart = function() {
        localStorage.removeItem("cartItems");
        window.location.href = "/thankyou/";
    };

    const clearLocalCart = function() {
        localStorage.removeItem("cartItems");
        window.location.href = "/checkout/";
    }

    const submitOrderBtn = document.getElementById("submit-order-btn");
    submitOrderBtn.addEventListener("click", function(event) {
        clearCart();
    });

    const clearCartBtn = document.getElementById("clear-cart-btn");
    clearCartBtn.addEventListener("click", function(event) {
        clearLocalCart();
    });
});
