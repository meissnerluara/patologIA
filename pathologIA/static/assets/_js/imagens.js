function previewImage() {
    var imagem = document.querySelector('input[name=Upload_Image]').files[0];
    var preview = document.querySelector('img');
    var reader = new FileReader();
    reader.onloadend = function() {
        preview.src = reader.result;
    }
    if (imagem) {
        reader.readAsDataURL(imagem);
    } else {
        preview.src = "";
    }
}