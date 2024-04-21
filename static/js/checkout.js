document.addEventListener("DOMContentLoaded", function() {
    // Function to display cart items from local storage
    const displayCartItems = function() {
        const cartItemsTable = document.getElementById("cart-items-table");
        const totalItemsCount = document.getElementById("total-items-count");
        const totalPrice = document.getElementById("total-price");

        cartItemsTable.innerHTML = ""; // Clear previous content

        const cartItems = JSON.parse(localStorage.getItem("cartItems")) || [];
        let totalItems = 0;
        let totalPriceValue = 0;

        cartItems.forEach(function(item) {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${item.productType} - ${item.flavor} - ${item.size}</td>
                <td>${item.quantity}</td>
                <td>${item.totalPrice ? '$' + item.totalPrice.toFixed(2) : 'N/A'}</td>
            `;
            cartItemsTable.appendChild(row);

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
        // Optionally, you can redirect to the home page after clearing the cart
        window.location.href = "/thankyou/";
    };

    // Add event listener to "Submit Order" button. Maybe going to delete this.
    const submitOrderBtn = document.getElementById("submit-order-btn");
    submitOrderBtn.addEventListener("click", function(event) {
        clearCart();
    });
});
