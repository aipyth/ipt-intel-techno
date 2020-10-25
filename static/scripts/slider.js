document.addEventListener("DOMContentLoaded", () => {
    let slides = document.querySelectorAll(".karusel-content .karusel-item");
    let currentSlide = 0;
    const nextButton = document.querySelector("a.next-control");
    const prevButton = document.querySelector("a.prev-control");
    
    var counts =  document.getElementById("counts");
    for (let index = 0; index < slides.length; index++) {
        counts.appendChild(document.createElement("span"));
    }
    var selected = counts.firstElementChild;
    selected.className = "this"
    

    function nextSlide()
    {
        slides[currentSlide].className = "karusel-item";
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].className = "karusel-item aktiv";
        selected.className = ""
        if (selected.nextElementSibling != null) {
            selected = selected.nextElementSibling
            selected.className = "this"
        }
        else {
            selected = counts.firstElementChild
            selected.className = "this"
        }
    }
    function prevSlide()
    {
        slides[currentSlide].className = "karusel-item";
        currentSlide = (currentSlide - 1) % slides.length;
        if(currentSlide == -1)
        {
            currentSlide = slides.length - 1;
        }
        slides[currentSlide].className = "karusel-item aktiv";
        selected.className = ""
        if (selected.previousElementSibling != null) {
            selected = selected.previousElementSibling
            selected.className = "this"
        }
        else {
            selected = counts.lastElementChild
            selected.className = "this"
        }
    }
    nextButton.addEventListener("click", () => 
    {
        nextSlide()
    });
    prevButton.addEventListener("click", () => 
    {
        prevSlide()
    });
});