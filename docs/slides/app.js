const slides = Array.from(document.querySelectorAll(".slide"));
const prevButton = document.querySelector("#prevSlide");
const nextButton = document.querySelector("#nextSlide");
const overviewToggle = document.querySelector("#overviewToggle");
const overviewClose = document.querySelector("#overviewClose");
const overview = document.querySelector("#overview");
const overviewList = document.querySelector("#overviewList");
const currentSlide = document.querySelector("#currentSlide");
const totalSlides = document.querySelector("#totalSlides");
const progressBar = document.querySelector("#progressBar");

let activeIndex = 0;

function clampSlide(index) {
  return Math.min(Math.max(index, 0), slides.length - 1);
}

function updateHash(index) {
  const nextHash = `#${index + 1}`;
  if (window.location.hash !== nextHash) {
    window.history.replaceState(null, "", nextHash);
  }
}

function showSlide(index, shouldUpdateHash = true) {
  activeIndex = clampSlide(index);
  slides.forEach((slide, slideIndex) => {
    slide.classList.toggle("active", slideIndex === activeIndex);
  });

  currentSlide.textContent = String(activeIndex + 1);
  totalSlides.textContent = String(slides.length);
  progressBar.style.width = `${((activeIndex + 1) / slides.length) * 100}%`;

  Array.from(overviewList.children).forEach((button, buttonIndex) => {
    button.classList.toggle("active", buttonIndex === activeIndex);
  });

  document.title = `${activeIndex + 1}/${slides.length} - ${slides[activeIndex].dataset.title}`;

  if (shouldUpdateHash) {
    updateHash(activeIndex);
  }
}

function nextSlide() {
  showSlide(activeIndex + 1);
}

function previousSlide() {
  showSlide(activeIndex - 1);
}

function toggleOverview(force) {
  const shouldOpen = typeof force === "boolean" ? force : !overview.classList.contains("open");
  overview.classList.toggle("open", shouldOpen);
  overview.setAttribute("aria-hidden", String(!shouldOpen));
}

function buildOverview() {
  slides.forEach((slide, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = `${String(index + 1).padStart(2, "0")} - ${slide.dataset.title}`;
    button.addEventListener("click", () => {
      showSlide(index);
      toggleOverview(false);
    });
    overviewList.appendChild(button);
  });
}

function slideFromHash() {
  const number = Number(window.location.hash.replace("#", ""));
  if (Number.isFinite(number) && number >= 1 && number <= slides.length) {
    return number - 1;
  }
  return 0;
}

prevButton.addEventListener("click", previousSlide);
nextButton.addEventListener("click", nextSlide);
overviewToggle.addEventListener("click", () => toggleOverview());
overviewClose.addEventListener("click", () => toggleOverview(false));

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    toggleOverview(false);
    return;
  }

  if (overview.classList.contains("open")) {
    return;
  }

  if (event.key === "ArrowRight" || event.key === " ") {
    event.preventDefault();
    nextSlide();
  }

  if (event.key === "ArrowLeft") {
    event.preventDefault();
    previousSlide();
  }

  if (event.key === "Home") {
    event.preventDefault();
    showSlide(0);
  }

  if (event.key === "End") {
    event.preventDefault();
    showSlide(slides.length - 1);
  }

  if (event.key.toLowerCase() === "o") {
    event.preventDefault();
    toggleOverview();
  }
});

window.addEventListener("hashchange", () => showSlide(slideFromHash(), false));

buildOverview();
showSlide(slideFromHash());
requestAnimationFrame(() => document.body.classList.add("deck-ready"));
