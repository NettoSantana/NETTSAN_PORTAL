/* CAMINHO COMPLETO: C:\Users\vlula\OneDrive\Área de Trabalho\Projetos Backup\NETTSAN_PORTAL\static\js\site.js
   DATA E HORA DO ULTIMO RECODE: 2026-08-10 11:10 -03:00
   MOTIVO DA ALTERACAO: Criar apenas as interacoes essenciais da interface inicial do portal NettSan. */

(() => {
    const navToggle = document.querySelector("[data-nav-toggle]");
    const mainNav = document.querySelector("[data-main-nav]");
    const year = document.querySelector("[data-current-year]");

    if (year) {
        year.textContent = new Date().getFullYear();
    }

    if (!navToggle || !mainNav) {
        return;
    }

    const closeMenu = () => {
        navToggle.setAttribute("aria-expanded", "false");
        mainNav.classList.remove("is-open");
    };

    navToggle.addEventListener("click", () => {
        const isOpen = navToggle.getAttribute("aria-expanded") === "true";
        navToggle.setAttribute("aria-expanded", String(!isOpen));
        mainNav.classList.toggle("is-open", !isOpen);
    });

    mainNav.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", closeMenu);
    });

    window.addEventListener("resize", () => {
        if (window.innerWidth > 920) {
            closeMenu();
        }
    });
})();
