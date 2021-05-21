function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.getElementById("nav").style.display = "none";
    document.getElementById("small").style.display = "none";
    document.getElementById("larg").style.display = "block";

}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("nav").style.display = "block";
    document.getElementById("small").style.display = "block";
    document.getElementById("larg").style.display = "none";

}
$(document).ready(function() {

    openNav();

});