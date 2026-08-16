function saveTokens(access_token, refresh_token) {
    localStorage.setItem("access_token", access_token);
    localStorage.setItem("refresh_token", refresh_token);
}

function clearTokens() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
}

function isLoggedIn() {
    return !!localStorage.getItem("access_token");
}

function requireAuth() {
    if (!isLoggedIn()) {
        window.location.href = "/login.html";
    }
}

function logout() {
    clearTokens();
    window.location.href = "/login.html";
}

async function ensureAuth() {
    const token = localStorage.getItem("access_token");
    if (!token) {
        window.location.href = "/login.html";
        return;
    }


    try {
        const payload = JSON.parse(atob(token.split(".")[1]));
        const exp = payload.exp * 1000;
        const now = Date.now();


        if (exp - now < 5 * 60 * 1000) {
            const data = await refreshToken();
            saveTokens(data.access_token, data.refresh_token);
        }
    } catch {
        logout();
    }
}