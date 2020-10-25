document.addEventListener("DOMContentLoaded", () => {
    var navbutton = document.getElementById("navbutton");
    var clicked = false;
    function navClick()
    {
        document.querySelector(".menu").className="menu act";
        clicked = true;
    }
    function navHide()
    {
        document.querySelector(".menu").className="menu";
        clicked = false;
    }
    navbutton.addEventListener("touchstart", () => 
    {
        if(clicked)
        {
            navHide();
        }
        else{
            navClick();
        }
    });

});