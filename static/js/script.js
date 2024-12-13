document.addEventListener('DOMContentLoaded', function() {
    // Comprobar si el modo oscuro está guardado en las cookies
    const cookies = document.cookie.split('; ');
    const darkModeCookie = cookies.find(cookie => cookie.startsWith('dark_mode='));

    // Establecer el estado inicial del modo oscuro y el icono del botón
    if (darkModeCookie) {
        const isDarkMode = darkModeCookie.split('=')[1] === 'true';
        if (isDarkMode) {
            document.body.classList.add('dark-mode');
            document.getElementById('modoJH').innerHTML = '🌞';  // Cambiar el icono a sol
        } else {
            document.getElementById('modoJH').innerHTML = '🌙';  // Cambiar el icono a luna
        }
    } else {
        // Si no hay cookie, establecer el icono por defecto (luna) y no activar el modo oscuro
        document.getElementById('modoJH').innerHTML = '🌙';  // Luna
    }

    // Alternar el modo oscuro y el icono cuando el botón es clickeado
    const toggleButton = document.getElementById('modoJH');
    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');

            // Cambiar el icono según el modo
            const isDarkMode = document.body.classList.contains('dark-mode');
            if (isDarkMode) {
                toggleButton.innerHTML = '🌞';  // Sol para modo oscuro
            } else {
                toggleButton.innerHTML = '🌙';  // Luna para modo claro
            }

            // Guardar la preferencia en las cookies
            document.cookie = `dark_mode=${isDarkMode}; path=/; max-age=31536000`; // Expira en 1 año
        });
    }
});
