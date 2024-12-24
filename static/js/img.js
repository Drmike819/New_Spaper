// creacionde la funcion para agregar una imagen
function addImageForm() {
    // busca  y cl;ona el formulario de la imagen
    var newForm = document.querySelector('.image-form').cloneNode(true);
    // limpia el compo del formulario clonado
    newForm.querySelector('input[type="file"]').value = '';
    // limpia el campo del formulario clonado
    newForm.querySelector('input[type="checkbox"]').checked = false;
    // inserta el formulario clonado en el documento
    document.querySelector('form').insertBefore(newForm, document.querySelector('button[onclick="addImageForm()"]'));
}