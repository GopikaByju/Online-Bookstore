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


//*****************************************************************************
function removeFromCart(itemId) {
    if (confirm("Are you sure you want to remove this item from the cart?")) {
        fetch("{% url 'remove_from_cart' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({
                item_id: itemId
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Item removed from cart!");
                location.reload(); // Refresh the page to update cart
            } else {
                alert("Failed to remove item from cart.");
            }
        })
        .catch(error => console.error('Error:', error));
    }
}
//*******************************************************************************
function changeQuantity(itemId, action) {
    var quantityInput = document.getElementById('quantity-' + itemId);
    var currentQuantity = parseInt(quantityInput.value);

    if (action === 'increase') {
        quantityInput.value = currentQuantity + 1;
    } else if (action === 'decrease' && currentQuantity > 1) {
        quantityInput.value = currentQuantity - 1;
    }
updateCartOnServer(itemId, quantityInput.value);
    // Optionally, send an AJAX request to update the cart on the server
    // Example:
    // updateCartOnServer(itemId, quantityInput.value);
}
//*******************************************************************************



//(function($) {
//
//  "use strict";
//
//  const tabs = document.querySelectorAll('[data-tab-target]')
//  const tabContents = document.querySelectorAll('[data-tab-content]')
//
//  tabs.forEach(tab => {
//    tab.addEventListener('click', () => {
//      const target = document.querySelector(tab.dataset.tabTarget)
//      tabContents.forEach(tabContent => {
//        tabContent.classList.remove('active')
//      })
//      tabs.forEach(tab => {
//        tab.classList.remove('active')
//      })
//      tab.classList.add('active')
//      target.classList.add('active')
//    })
//  });

  // Responsive Navigation with Button

  const hamburger = document.querySelector(".hamburger");
  const navMenu = document.querySelector(".menu-list");

  hamburger.addEventListener("click", mobileMenu);

  function mobileMenu() {
      hamburger.classList.toggle("active");
      navMenu.classList.toggle("responsive");
  }

  const navLink = document.querySelectorAll(".nav-link");

  navLink.forEach(n => n.addEventListener("click", closeMenu));

  function closeMenu() {
      hamburger.classList.remove("active");
      navMenu.classList.remove("responsive");
  }

  var initScrollNav = function() {
    var scroll = $(window).scrollTop();

    if (scroll >= 200) {
      $('#header').addClass("fixed-top");
    }else{
      $('#header').removeClass("fixed-top");
    }
  }

  $(window).scroll(function() {
    initScrollNav();
  });

  $(document).ready(function(){
    initScrollNav();

    Chocolat(document.querySelectorAll('.image-link'), {
        imageSize: 'contain',
        loop: true,
    })

    $('#header-wrap').on('click', '.search-toggle', function(e) {
      var selector = $(this).data('selector');

      $(selector).toggleClass('show').find('.search-input').focus();
      $(this).toggleClass('active');

      e.preventDefault();
    });


    // close when click off of container
    $(document).on('click touchstart', function (e){
      if (!$(e.target).is('.search-toggle, .search-toggle *, #header-wrap, #header-wrap *')) {
        $('.search-toggle').removeClass('active');
        $('#header-wrap').removeClass('show');
      }
    });

    $('.main-slider').slick({
        autoplay: false,
        autoplaySpeed: 4000,
        fade: true,
        dots: true,
        prevArrow: $('.prev'),
        nextArrow: $('.next'),
    });

    $('.product-grid').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        autoplay: false,
        autoplaySpeed: 2000,
        dots: true,
        arrows: false,
        responsive: [
          {
            breakpoint: 1400,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 999,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 660,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
          // You can unslick at a given breakpoint now by adding:
          // settings: "unslick"
          // instead of a settings object
        ]
    });

    AOS.init({
      duration: 1200,
      once: true,
    })

    jQuery('.stellarnav').stellarNav({
      theme: 'plain',
      closingDelay: 250,
      // mobileMode: false,
    });

  }); // End of a document


(jQuery);