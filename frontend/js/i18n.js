const DEFAULT_LANGUAGE = "en";
const SUPPORTED_LANGUAGES = ["en", "uk"];

const I18N = {
    en: {
        "app.name": "Price Tracker",
        "lang.en": "English",
        "lang.uk": "Українська",
        "nav.addProduct": "Add product",
        "nav.tracked": "Tracked items",
        "nav.logout": "Log out",
        "home.title": "Price Tracker",
        "home.description": "Track prices on Rozetka and get notified when they change",
        "home.findProduct.title": "Find product",
        "home.findProduct.description": "Search by name or link",
        "home.myProducts.title": "My products",
        "home.myProducts.description": "Your tracked list",
        "auth.login.title": "Sign in",
        "auth.login.subtitle": "Sign in to your account",
        "auth.login.email": "Email",
        "auth.login.password": "Password",
        "auth.login.emailPlaceholder": "you@example.com",
        "auth.login.passwordPlaceholder": "••••••",
        "auth.login.button": "Sign in",
        "auth.login.loading": "Signing in...",
        "auth.login.noAccount": "No account?",
        "auth.login.registerLink": "Sign up",
        "auth.register.title": "Sign up",
        "auth.register.subtitle": "Create your account",
        "auth.register.name": "Name",
        "auth.register.email": "Email",
        "auth.register.password": "Password",
        "auth.register.namePlaceholder": "John",
        "auth.register.emailPlaceholder": "you@gmail.com",
        "auth.register.passwordPlaceholder": "••••••",
        "auth.register.button": "Sign up",
        "auth.register.loading": "Creating account...",
        "auth.register.hasAccount": "Already have an account?",
        "auth.register.loginLink": "Sign in",
        "search.title": "Add product",
        "search.subtitle": "Find a product by name or paste a Rozetka link",
        "search.tab.search": "Search by name",
        "search.tab.link": "By link",
        "search.search.placeholder": "For example: Playstation",
        "search.search.button": "Search",
        "search.search.help": "If the product is not found, add it by a direct Rozetka link",
        "search.link.placeholder": "https://rozetka.com.ua/ua/.../p123456/",
        "search.link.button": "Add",
        "search.loading": "Searching for products...",
        "search.noResults": "Nothing found",
        "search.follow": "Track",
        "search.adding": "Adding...",
        "search.added": "Added",
        "search.alreadyTracked": "Already tracked",
        "search.error": "Error",
        "search.link.success": "Product added to tracked items",
        "tracked.title": "My products",
        "tracked.subtitle": "Products you are tracking",
        "tracked.empty": "You are not tracking any products yet",
        "tracked.findButton": "Find product",
        "tracked.details": "Details",
        "tracked.remove": "Remove",
        "tracked.loading": "Loading...",
        "product.title": "Product",
        "product.loading": "Loading...",
        "product.added": "Added",
        "product.open": "Open on Rozetka",
        "product.remove": "Remove from tracked",
        "product.history": "Price history",
        "product.notEnoughData": "Not enough data for chart",
        "product.error": "Error loading",
        "product.addedOn": "Added: {date}",
        "common.loading": "Loading...",
        "common.error": "Error",
    },
    uk: {
        "app.name": "Price Tracker",
        "lang.en": "English",
        "lang.uk": "Українська",
        "nav.addProduct": "Додати товар",
        "nav.tracked": "Мої товари",
        "nav.logout": "Вийти",
        "home.title": "Price Tracker",
        "home.description": "Відстежуйте ціни на товари з Розетки та дізнавайтесь про зміни",
        "home.findProduct.title": "Знайти товар",
        "home.findProduct.description": "Пошук за назвою або посиланням",
        "home.myProducts.title": "Мої товари",
        "home.myProducts.description": "Список товарів, що відстежуються",
        "auth.login.title": "Увійти",
        "auth.login.subtitle": "Увійдіть до свого облікового запису",
        "auth.login.email": "Email",
        "auth.login.password": "Пароль",
        "auth.login.emailPlaceholder": "you@example.com",
        "auth.login.passwordPlaceholder": "••••••",
        "auth.login.button": "Увійти",
        "auth.login.loading": "Входимо...",
        "auth.login.noAccount": "Немає облікового запису?",
        "auth.login.registerLink": "Зареєструватись",
        "auth.register.title": "Реєстрація",
        "auth.register.subtitle": "Створіть обліковий запис",
        "auth.register.name": "Ім'я",
        "auth.register.email": "Email",
        "auth.register.password": "Пароль",
        "auth.register.namePlaceholder": "Іван",
        "auth.register.emailPlaceholder": "you@gmail.com",
        "auth.register.passwordPlaceholder": "••••••",
        "auth.register.button": "Зареєструватись",
        "auth.register.loading": "Створюємо обліковий запис...",
        "auth.register.hasAccount": "Вже є обліковий запис?",
        "auth.register.loginLink": "Увійти",
        "search.title": "Додати товар",
        "search.subtitle": "Знайдіть товар за назвою або вставте посилання з Розетки",
        "search.tab.search": "Пошук за назвою",
        "search.tab.link": "За посиланням",
        "search.search.placeholder": "Наприклад: Playstation",
        "search.search.button": "Знайти",
        "search.search.help": "Якщо товар не знайдено, додайте його за прямим посиланням з Rozetka",
        "search.link.placeholder": "https://rozetka.com.ua/ua/.../p123456/",
        "search.link.button": "Додати",
        "search.loading": "Шукаємо товари...",
        "search.noResults": "Нічого не знайдено",
        "search.follow": "Слідкувати",
        "search.adding": "Додаємо...",
        "search.added": "Додано",
        "search.alreadyTracked": "Вже відстежується",
        "search.error": "Помилка",
        "search.link.success": "Товар доданий до відстежуваних",
        "tracked.title": "Мої товари",
        "tracked.subtitle": "Товари, які ви відстежуєте",
        "tracked.empty": "Ви ще не відстежуєте жодного товару",
        "tracked.findButton": "Знайти товар",
        "tracked.details": "Докладніше",
        "tracked.remove": "Видалити",
        "tracked.loading": "Завантажуємо...",
        "product.title": "Товар",
        "product.loading": "Завантажуємо...",
        "product.added": "Доданий",
        "product.open": "Відкрити на Rozetka",
        "product.remove": "Видалити з відстежуваних",
        "product.history": "Історія цін",
        "product.notEnoughData": "Недостатньо даних для графіка",
        "product.error": "Помилка завантаження",
        "product.addedOn": "Доданий: {date}",
        "common.loading": "Завантажуємо...",
        "common.error": "Помилка",
    },
};

function getLanguage() {
    const stored = localStorage.getItem("lang");
    return SUPPORTED_LANGUAGES.includes(stored) ? stored : DEFAULT_LANGUAGE;
}

function t(key, params = {}) {
    const lang = getLanguage();
    const fallback = I18N[DEFAULT_LANGUAGE][key] ?? key;
    const template = I18N[lang]?.[key] ?? fallback;

    return Object.entries(params).reduce((value, [name, replacement]) => {
        return value.replaceAll(`{${name}}`, String(replacement));
    }, template);
}

function setLanguage(lang) {
    const normalized = SUPPORTED_LANGUAGES.includes(lang) ? lang : DEFAULT_LANGUAGE;
    localStorage.setItem("lang", normalized);
    applyTranslations();
    window.dispatchEvent(new CustomEvent("languagechange", { detail: { lang: normalized } }));
}

function bindLanguageSwitches(root = document) {
    root.querySelectorAll("[data-lang-switch]").forEach((select) => {
        select.value = getLanguage();

        if (select.dataset.bound === "1") return;

        select.addEventListener("change", (event) => {
            setLanguage(event.target.value);
        });
        select.dataset.bound = "1";
    });
}

function applyTranslations(root = document) {
    const lang = getLanguage();
    document.documentElement.lang = lang;

    root.querySelectorAll("[data-i18n]").forEach((element) => {
        element.textContent = t(element.dataset.i18n);
    });

    root.querySelectorAll("[data-i18n-placeholder]").forEach((element) => {
        element.placeholder = t(element.dataset.i18nPlaceholder);
    });

    root.querySelectorAll("[data-i18n-title]").forEach((element) => {
        element.title = t(element.dataset.i18nTitle);
    });

    bindLanguageSwitches(root);
}

document.addEventListener("DOMContentLoaded", () => {
    applyTranslations();
});

window.t = t;
window.setLanguage = setLanguage;
window.getLanguage = getLanguage;
window.applyTranslations = applyTranslations;
