document.addEventListener("DOMContentLoaded", () => {
  const menuItems = document.querySelectorAll(".menu > li");
  const overlay = document.createElement("div");
  overlay.classList.add("overlay");
  document.body.appendChild(overlay);

  menuItems.forEach(item => {
    const link = item.querySelector("a");
    const submenu = item.querySelector(".submenu");

    // Exibição momentânea (hover)
    item.addEventListener("mouseenter", () => {
      if (submenu) {
        submenu.style.display = "block";
        overlay.style.display = "block";
        item.classList.add("active");
      }
    });

    item.addEventListener("mouseleave", () => {
      if (submenu && !item.classList.contains("fixed")) {
        submenu.style.display = "none";
        overlay.style.display = "none";
        item.classList.remove("active");
      }
    });

    // Exibição fixa (clique)
    link.addEventListener("click", (e) => {
      if (submenu) {
        e.preventDefault();
        const isFixed = item.classList.contains("fixed");

        // Fecha todos os outros menus fixos
        menuItems.forEach(i => {
          i.classList.remove("fixed", "active");
          const sm = i.querySelector(".submenu");
          if (sm) sm.style.display = "none";
        });

        if (!isFixed) {
          item.classList.add("fixed", "active");
          submenu.style.display = "block";
          overlay.style.display = "block";
        } else {
          overlay.style.display = "none";
        }
      }
      // Se não tem submenu, deixa o link funcionar normalmente!
    });
  });

  // Clicar fora fecha o menu fixo
  overlay.addEventListener("click", () => {
    menuItems.forEach(i => {
      i.classList.remove("fixed", "active");
      const sm = i.querySelector(".submenu");
      if (sm) sm.style.display = "none";
    });
    overlay.style.display = "none";
  });
});