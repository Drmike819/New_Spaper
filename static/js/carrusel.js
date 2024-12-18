document.addEventListener("DOMContentLoaded", () => {
    let allCarousels = document.querySelectorAll('.container_carru');
    
    allCarousels.forEach(carousel => {
        let articleId = carousel.id.split('-')[1];
        let items = carousel.querySelectorAll('.carousel-item');
        let currentIndex = 0;

        // Si solo hay una imagen, céntrala y termina
        if (items.length === 1) {
            items[0].classList.add('img_center_single');
            return;
        }

        // Marcar imágenes adicionales si hay más de 3
        if (items.length > 3) {
            items.forEach((item, index) => {
                if (index >= 3) {
                    item.classList.add('additional');
                }
            });
        }

        // Función para actualizar las clases del carrusel
        function updateCarousel() {
            items.forEach((item, index) => {
                // Quitar clases existentes
                item.classList.remove('img_center', 'img_left', 'img_rigth', 'additional');

                // Añadir clases según el índice
                if (index === currentIndex) {
                    item.classList.add('img_center');
                } else if (index === (currentIndex - 1 + items.length) % items.length) {
                    item.classList.add('img_left');
                } else if (index === (currentIndex + 1) % items.length) {
                    item.classList.add('img_rigth');
                } else {
                    item.classList.add('additional'); // Otras imágenes quedan escondidas
                }
            });
        }

        // Navegación del carrusel
        document.getElementById(`arrowrigth-${articleId}`).addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % items.length;
            updateCarousel();
        });

        document.getElementById(`arrowleft-${articleId}`).addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + items.length) % items.length;
            updateCarousel();
        });

        // Inicializar carrusel
        updateCarousel();
    });
});
