$(document).ready(function () {
    var previousDropdown = null;

    $('.dropdown-submenu a.dropdown-item').on("click", function (e) {
        var currentDropdown = $(this).next('ul');

        if (previousDropdown && previousDropdown[0] !== currentDropdown[0]) {
            previousDropdown.hide();
        }

        currentDropdown.toggle();
        e.stopPropagation();

        previousDropdown = currentDropdown;
    });

});


var prevScrollPos = window.pageYOffset;
window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollPos > currentScrollPos) {
        document.querySelector(".navbar").style.top = "0";
    } else {
        document.querySelector(".navbar").style.top = "-80px";
    }
    prevScrollPos = currentScrollPos;
};




