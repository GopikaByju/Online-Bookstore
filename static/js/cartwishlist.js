document.addEventListener("DOMContentLoaded", function () {
    // Add to Cart
    document.querySelectorAll(".add-to-cart").forEach(button => {
        button.addEventListener("click", function () {
            let bookId = this.getAttribute("data-id");

          fetch(`/add-to-cart/${bookId}/`, {
    method: "POST",
    headers: {
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",

    },
    body: JSON.stringify({ book_id: bookId })
})
            .then(response => response.json())
            .then(data => {
                // If the cart quantity exceeds 10, show out of stock message
                if (data.status === "Out of stock (You cannot add more than 10 items)") {
                    document.getElementById("message").innerHTML = `<p style="color: red;">${data.status}</p>`;
                } else if (data.status === "Book added to cart") {
                    document.getElementById("message").innerHTML = `<p style="color: green;">${data.status}</p>`;
                    document.getElementById("stock-count").innerText = `Remaining Stock: ${data.remaining_stock}`;
                } else {
                    document.getElementById("message").innerHTML = `<p style="color: red;">Error adding to cart. Please try again.</p>`;
                }
            })
            .catch(error => {
                console.error("Error:", error);
                document.getElementById("message").innerHTML = `<p style="color: red;">There was an error. Please try again later.</p>`;
            });
        });
    });

    // Add to Wishlist
    document.querySelectorAll(".add-to-wishlist").forEach(button => {
        button.addEventListener("click", function () {
            let bookId = this.getAttribute("data-id");

            fetch(`/add-to-wishlist/${bookId}/`, {
    method: "POST",
    headers: {
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
    },
    body: JSON.stringify({ book_id: bookId })
})

            .then(response => response.json())
            .then(data => {
                document.getElementById("message").innerHTML = `<p style="color: orange;">${data.status}</p>`;
            })
            .catch(error => console.error("Error:", error));
        });
    });
});
