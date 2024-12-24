// indica que el el codigo entrara en funcion cuando el documento este cargado completamente
document.addEventListener('DOMContentLoaded', function() {
   // obtiene las cookies que almecena la pagina actualmente
    const cookies = document.cookie.split('; ');
    // busca la cookies dark_mode
    const darkModeCookie = cookies.find(cookie => cookie.startsWith('dark_mode='));
    // verifica si las cookie se encontro
    if (darkModeCookie) {
        // obtiene el valor de la cookie
        const isDarkMode = darkModeCookie.split('=')[1] === 'true';
        // verifica el valor de la cookie TRUE
        if (isDarkMode) {
            // agrega la clase dark-mode al documento html
            document.body.classList.add('dark-mode');
            // cambia el icono de la luna a sol
            document.getElementById('modoJH').innerHTML = '🌞';
        } else {
            // valor por defecto del icono
            document.getElementById('modoJH').innerHTML = '🌙'; 
        }
    } else {
        // valor por defecto del icono
        document.getElementById('modoJH').innerHTML = '🌙';
    }

    // obtiene el boton de modo oscuro
    const toggleButton = document.getElementById('modoJH');
    // agrega la accion del boton del modo oscuro
    if (toggleButton) {
        // agrega la accion de click al boton
        toggleButton.addEventListener('click', () => {
            // cambia el modo oscuro o modo normal por cada click
            document.body.classList.toggle('dark-mode');

            // verifica si el modo oscuro esta activado
            const isDarkMode = document.body.classList.contains('dark-mode');
            if (isDarkMode) {
                // si esta activado el icono es el del sol
                toggleButton.innerHTML = '🌞';
            // de lo contrario se muestra el modo predeterminado
            } else {
                toggleButton.innerHTML = '🌙';
            }
            // guarda el estado del modo oscuro en una cookie e indica la duracion de la cookie
            document.cookie = `dark_mode=${isDarkMode}; path=/; max-age=31536000`;
        });
    }
});
