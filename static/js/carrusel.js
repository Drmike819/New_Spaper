// indica que el codigo entrara en funcion cuando el documento este cargado completamente
document.addEventListener("DOMContentLoaded", () => {
    // busca todos los carruseles en el documento
    let allCarousels = document.querySelectorAll('.container_carru');
    // recorre todos los carruseles
    allCarousels.forEach(carousel => {
        // obtiene el id del carrusel
        let articleId = carousel.id.split('-')[1];
        // busca todos los items del carrusel
        let items = carousel.querySelectorAll('.carousel-item');
        // inicializa el indice actual
        let currentIndex = 0;

        // Si solo hay una imagen, céntrala y termina
        if (items.length === 1) {
            // verifica si hay una unica imagen y le agrega una clase
            items[0].classList.add('img_center_single');
            return;
        }

        // Marcar imágenes adicionales si hay más de 3
        if (items.length > 3) {
            // recorre los items
            items.forEach((item, index) => {
                // verifica si hay mas de 3
                if (index >= 3) {
                    // si hay mas de 3 le añade la clase additional
                    item.classList.add('additional');
                }
            });
        }

        // Función para actualizar las clases del carrusel
        function updateCarousel() {
            // recorre los items
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
