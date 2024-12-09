document.addEventListener('DOMContentLoaded', function() {
    // Comprobar si el modo oscuro está guardado en las cookies
    const cookies = document.cookie.split('; ');
    const darkModeCookie = cookies.find(cookie => cookie.startsWith('dark_mode='));

    if (darkModeCookie) {
        const isDarkMode = darkModeCookie.split('=')[1] === 'true';
        if (isDarkMode) {
            document.body.classList.add('dark-mode');
        }
    }

    // Alternar el modo oscuro cuando el botón es clickeado
    const toggleButton = document.getElementById('modoJH');
    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');

            // Guardar la preferencia en las cookies
            const isDarkMode = document.body.classList.contains('dark-mode');
            document.cookie = `dark_mode=${isDarkMode}; path=/; max-age=31536000`; // Expira en 1 año
        });
    }
});