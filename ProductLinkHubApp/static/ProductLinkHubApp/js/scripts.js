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



// obtiene la lista de link e imagenes para el fondo

const jumbotron = document.querySelector('.jumbotron');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');


// obtiene la lista a traves de la url
fetch('/imagen-fondo/')  // Reemplaza esto con la URL correcta
    .then(response => response.json())
    .then(data => {
        let currentIndex = 0;
        
        function setBackgroundImageAndLink() {
        const currentImageAndLink = data.url_imagenes[currentIndex];
        jumbotron.style.backgroundImage = `url('${currentImageAndLink.imagen}')`;

        jumbotron.addEventListener('click', function (event) {
            if (event.target === jumbotron) {
            window.location.href = currentImageAndLink.enlace;
            }
        });
        }

        function showPreviousImage() {
        currentIndex = (currentIndex - 1 + data.url_imagenes.length) % data.url_imagenes.length;
        setBackgroundImageAndLink();
        }

        function showNextImage() {
        currentIndex = (currentIndex + 1) % data.url_imagenes.length;
        setBackgroundImageAndLink();
        }

        prevButton.addEventListener('click', showPreviousImage);
        nextButton.addEventListener('click', showNextImage);

        function startAutomaticChange() {
        intervalId = setInterval(showNextImage, 5000);
        }

        // Llamar a la función para establecer la imagen de fondo y el enlace inicialmente
        setBackgroundImageAndLink();

        // Iniciar el cambio automático de imágenes
        startAutomaticChange();
        
        
    })
    .catch(error => {
        console.error('Hubo un error:', error);
    });















