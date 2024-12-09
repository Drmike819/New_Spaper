function addImageForm() {
    var newForm = document.querySelector('.image-form').cloneNode(true);
    newForm.querySelector('input[type="file"]').value = '';
    newForm.querySelector('input[type="checkbox"]').checked = false;
    document.querySelector('form').insertBefore(newForm, document.querySelector('button[onclick="addImageForm()"]'));
}