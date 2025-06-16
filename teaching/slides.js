   document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".slide"); // Get all slides dynamically
    let currentSlideIndex = 0; // Start from first slide

    function goToSlide(index) {
        if (index >= 0 && index < slides.length) {
            slides[index].scrollIntoView({ behavior: "smooth" });
            currentSlideIndex = index;
        }
    }

    function nextSlide() {
        if (currentSlideIndex < slides.length - 1) {
            goToSlide(currentSlideIndex + 1);
        }
    }

    function prevSlide() {
        if (currentSlideIndex > 0) {
            goToSlide(currentSlideIndex - 1);
        }
    }

// Fix: Ensure keyboard event fires properly
    window.addEventListener("keydown", (event) => {
        if (event.key === "ArrowRight") {
            event.preventDefault(); // Prevent scrolling right
            nextSlide();
        }
        if (event.key === "ArrowLeft") {
            event.preventDefault(); // Prevent scrolling left
            prevSlide();
        }
    });

    // Example: Attach to buttons
    document.getElementById("next").addEventListener("click", nextSlide);
    document.getElementById("prev").addEventListener("click", prevSlide);
});

function toggleImage(imgElement, alternateSrc) {
    let currentSrc = imgElement.src;
    let originalSrc = imgElement.getAttribute("data-original"); // Store original src

    if (!originalSrc) {
        imgElement.setAttribute("data-original", currentSrc); // Save the first src
        originalSrc = currentSrc;
    }

    // Swap between original and alternate image
    imgElement.src = (currentSrc === originalSrc) ? alternateSrc : originalSrc;
}
