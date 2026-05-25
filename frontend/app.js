const productsContainer = document.getElementById("products-container");

loadSuggestions();

async function loadProducts() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/v1/products/"
        );

        const products = await response.json();

        renderProducts(products);

    } catch (error) {

        console.error("API Error:", error);
    }
}

function renderProducts(products) {

    productsContainer.innerHTML = "";

    products.forEach(product => {

        const card = document.createElement("div");

        card.classList.add("product-card");

        card.innerHTML = `
            <h3 class="product-title">${product.name}</h3>

            <p class="product-price">
                €${product.price}
            </p>

            <button class="buy-btn">
                Add to Cart
            </button>
        `;

        productsContainer.appendChild(card);
    });
}

async function askAI() {

    const input = document.getElementById("aiInput");

    const userMessage = input.value;

    saveQuery(userMessage);

    if (!userMessage) {
        return;
    }

    try {

        const response = await fetch(
            "http://localhost:9000/chat",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: userMessage
                })
            }
        );

        const data = await response.json();

        renderProducts(data.products);

    } catch (error) {

        console.error(error);

        alert("Error connecting to AI backend.");
    }
}

function renderProducts(products) {

    const container =
        document.getElementById("products-container");

    const countElement =
        document.getElementById("productCount");

    container.innerHTML = "";

    // UPDATE COUNT
    countElement.innerHTML =
        `Showing ${products.length} products`;

    if (products.length === 0) {

        container.innerHTML =
            "<p>No products found.</p>";

        return;
    }

    products.forEach(product => {

        const productCard = `
            <div class="product-card">

                <h3>${product.name}</h3>

                <p><strong>Brand:</strong> ${product.brand}</p>

                <p><strong>Category:</strong> ${product.category}</p>

                <p><strong>Price:</strong> €${product.price}</p>

                <p><strong>Rating:</strong> ⭐ ${product.rating}</p>

                <p><strong>Stock:</strong> ${product.stock}</p>

                <p>${product.description}</p>

            </div>
        `;

        container.innerHTML += productCard;
    });
}

function saveQuery(query) {

    let queries =
        JSON.parse(localStorage.getItem("ai_queries"))
        || [];

    // avoid duplicates
    if (!queries.includes(query)) {

        queries.push(query);

        localStorage.setItem(
            "ai_queries",
            JSON.stringify(queries)
        );
    }
}

function loadSuggestions() {

    const datalist =
        document.getElementById("querySuggestions");

    if (!datalist) {
        return;
    }

    let queries =
        JSON.parse(localStorage.getItem("ai_queries"))
        || [];

    datalist.innerHTML = "";

    queries.forEach(query => {

        const option =
            document.createElement("option");

        option.value = query;

        datalist.appendChild(option);
    });
}

loadProducts();
