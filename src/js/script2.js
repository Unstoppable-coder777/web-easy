window.addEventListener("DOMContentLoaded", (event) => {
  // Navbar shrink function
  var navbarShrink = function () {
    const navbarCollapsible = document.body.querySelector("#mainNav");
    if (!navbarCollapsible) {
      return;
    }
    if (window.scrollY === 0) {
      navbarCollapsible.classList.remove("navbar-shrink");
    } else {
      navbarCollapsible.classList.add("navbar-shrink");
    }
  };

  // Shrink the navbar
  navbarShrink();

  // Shrink the navbar when page is scrolled
  document.addEventListener("scroll", navbarShrink);

  // Activate Bootstrap scrollspy on the main nav element
  const mainNav = document.body.querySelector("#mainNav");
  if (mainNav) {
    new bootstrap.ScrollSpy(document.body, {
      target: "#mainNav",
      offset: 74,
    });
  }
});

let dt = document.querySelector(".navbar-brand");
let dt2 = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", () => {
  sp = window.scrollY;
  dt.classList.add("nv-color");
  if (sp == 0) {
    dt.classList.remove("nv-color");
    dt2[0].classList.remove("nv-color");
    dt2[1].classList.remove("nv-color");
    dt2[2].classList.remove("nv-color");
    dt2[3].classList.remove("nv-color");
  }
  if (sp > 2) {
    dt.classList.add("nv-color");
    dt2[0].classList.add("nv-color");
    dt2[1].classList.add("nv-color");
    dt2[2].classList.add("nv-color");
    dt2[3].classList.add("nv-color");
  }
});
