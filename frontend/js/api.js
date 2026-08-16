const BASE_URL = "/api";

async function register(name, email, password) {
    const res = await fetch(`${BASE_URL}/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
    });
    return handleResponse(res);
}

async function login(email, password) {
    const res = await fetch(`${BASE_URL}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
    });
    return handleResponse(res);
}

async function refreshToken() {
    const refresh_token = localStorage.getItem("refresh_token");
    const res = await fetch(`${BASE_URL}/auth/refresh`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh_token }),
    });
    return handleResponse(res);
}


async function getProducts() {
    const res = await fetchWithAuth(`${BASE_URL}/products/`);
    return handleResponse(res);
}

async function addProduct(href) {
    const res = await fetchWithAuth(`${BASE_URL}/products/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ href }),
    });
    return handleResponse(res);
}

async function getProduct(productId) {
    const res = await fetchWithAuth(`${BASE_URL}/products/${productId}`);
    return handleResponse(res);
}

async function deleteProduct(productId) {
    const res = await fetchWithAuth(`${BASE_URL}/products/${productId}`, {
        method: "DELETE",
    });
    return handleResponse(res);
}

async function searchProducts(text) {
    const res = await fetchWithAuth(`${BASE_URL}/products/search?text=${encodeURIComponent(text)}`);
    return handleResponse(res);
}

async function getPriceHistory(productId) {
    const res = await fetchWithAuth(`${BASE_URL}/products/${productId}/history`);
    return handleResponse(res);
}


async function fetchWithAuth(url, options = {}) {
    const token = localStorage.getItem("access_token");
    return fetch(url, {
        ...options,
        headers: {
            ...options.headers,
            Authorization: `Bearer ${token}`,
        },
    });
}

async function handleResponse(res) {
    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || "Помилка запиту");
    }
    if (res.status === 204) return null;
    return res.json();
}