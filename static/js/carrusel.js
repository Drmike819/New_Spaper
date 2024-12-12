document.addEventListener("DOMContentLoaded", () => {
    // Iterar sobre todos los carruseles
    let allCarousels = document.querySelectorAll('.container_carru');
    
    allCarousels.forEach(carousel => {
        // Obtener el ID único del carrusel
        let articleId = carousel.id.split('-')[1];

        // Obtener las imágenes y los indicadores del carrusel específico
        let items = carousel.querySelectorAll('.carousel-item');  // Selección más precisa
        let indicators = carousel.querySelectorAll('.indicator'); // Selección más precisa
        let currentIndex = 0;  // Índice de la imagen visible actualmente

        // Actualiza las imágenes y los indicadores
        function updateCarousel() {
            // Elimina las clases de la imagen anterior
            items.forEach((item, index) => {
                item.classList.remove('img_center', 'img_left', 'img_rigth');
            });

            // Añade las clases correctas a las imágenes según el índice actual
            items[currentIndex].classList.add('img_center');
            items[(currentIndex - 1 + items.length) % items.length].classList.add('img_left');
            items[(currentIndex + 1) % items.length].classList.add('img_rigth');

            // Actualiza los indicadores
            indicators.forEach((indicator, index) => {
                if (index === currentIndex) {
                    indicator.classList.add('active');
                } else {
                    indicator.classList.remove('active');
                }
            });
        }

        // Event listeners para los botones de navegación
        document.getElementById(`arrowrigth-${articleId}`).addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % items.length;  // Avanza al siguiente
            updateCarousel();
        });

        document.getElementById(`arrowleft-${articleId}`).addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + items.length) % items.length;  // Retrocede al anterior
            updateCarousel();
        });

        // Event listeners para los indicadores
        indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => {
                currentIndex = index;
                updateCarousel();
            });
        });

        // Inicializa el carrusel con la primera imagen visible
        updateCarousel();
    });
});
