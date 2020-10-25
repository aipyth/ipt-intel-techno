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

    setInterval(nextSlide, 5000)

    //swiping for phones

    class Swipe {
        constructor(element) {
            this.xDown = null;
            this.yDown = null;
            this.element = typeof(element) === 'string' ? document.querySelector(element) : element;
    
            this.element.addEventListener('touchstart', function(evt) {
                this.xDown = evt.touches[0].clientX;
                this.yDown = evt.touches[0].clientY;
            }.bind(this), false);
    
        }
    
        onLeft(callback) {
            this.onLeft = callback;
    
            return this;
        }
    
        onRight(callback) {
            this.onRight = callback;
    
            return this;
        }
    
        onUp(callback) {
            this.onUp = callback;
    
            return this;
        }
    
        onDown(callback) {
            this.onDown = callback;
    
            return this;
        }
    
        handleTouchMove(evt) {
            if ( ! this.xDown || ! this.yDown ) {
                return;
            }
    
            var xUp = evt.touches[0].clientX;
            var yUp = evt.touches[0].clientY;
    
            this.xDiff = this.xDown - xUp;
            this.yDiff = this.yDown - yUp;
    
            if ( Math.abs( this.xDiff ) > Math.abs( this.yDiff ) ) { // Most significant.
                if ( this.xDiff > 0 ) {
                    this.onLeft();
                } else {
                    this.onRight();
                }
            } else {
                if ( this.yDiff > 0 ) {
                    this.onUp();
                } else {
                    this.onDown();
                }
            }
    
            // Reset values.
            this.xDown = null;
            this.yDown = null;
        }
    
        run() {
            this.element.addEventListener('touchmove', function(evt) {
                this.handleTouchMove(evt).bind(this);
            }.bind(this), false);
        }
    }

    var swiper = new Swipe(document.querySelectorAll(".karusel"));
    swiper.onLeft(nextSlide);
    swiper.onRight(prevSlide);
});