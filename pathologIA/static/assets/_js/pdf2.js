function previewPdf() {
  var arqpdf = document.querySelector('input[name=cIdArtigo]').files[0];
  var preview = document.querySelector('pdf');
  var reader = new FileReader();
  reader.onloadend = function() {
      preview.src = reader.result;
  }
  if (arqpdf) {
      reader.readAsDataURL(arqpdf);
  } else {
      preview.src = "";
  }
}