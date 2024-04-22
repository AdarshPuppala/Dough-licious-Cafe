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
    
   // Function to clear cart items current session
    const clearLocalCart = function() {
        localStorage.removeItem("cartItems");
        window.location.href = "/checkout/";
    }

    const submitOrderBtn = document.getElementById("submit-order-btn");
    submitOrderBtn.addEventListener("click", function(event) {
    event.preventDefault(); // Prevent alert to come twice

    const pickupNameInput = document.getElementById("pickup-name");
    const pickupName = pickupNameInput.value.trim();

    // Check if pickup name is empty
    if (pickupName === "") {
        alert("Please enter a pickup name before submitting.");
        return;
    }

    const creditCardNumberInput = document.getElementById("credit-card-number");
    const creditCardNumber = creditCardNumberInput.value.trim();
    const cvvInput = document.getElementById("cvv");
    const cvv = cvvInput.value.trim();
    const expirationDateInput = document.getElementById("expiration-date");
    const expirationDate = expirationDateInput.value.trim();

    // Credit card number validation
    if (!isValidCreditCardNumber(creditCardNumber)) {
        alert("Please enter a valid 16-digit credit card number.");
        return;
    }

    // CVV validation
    if (!isValidCVV(cvv)) {
        alert("Please enter a valid 3-digit CVV.");
        return;
    }

    // Expiration date validation
    if (!isValidExpirationDate(expirationDate)) {
        alert("Please enter a valid expiration date in the format MM/YY.");
        return;
    }

    clearCart();
});

    const clearCartBtn = document.getElementById("clear-cart-btn");
    clearCartBtn.addEventListener("click", function(event) {
        clearLocalCart();
    });

    // Function to validate credit card number. Using RegEx
    function isValidCreditCardNumber(number) {
        return /^\d{16}$/.test(number);
    }

    // Function to validate CVV. Using RegEx
    function isValidCVV(cvv) {
        return /^\d{3}$/.test(cvv);
    }

    // Function to validate expiration date. Using RegEx
    function isValidExpirationDate(date) {
        return /^\d{2}\/\d{2}$/.test(date);
    }
});