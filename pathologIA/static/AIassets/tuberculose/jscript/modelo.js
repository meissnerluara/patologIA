// Script para carregar o modelo assim que inicializar a página

// Função para  obter o ID no momento do clique no botão
function simulateClick(tabID) {
	
	document.getElementById(tabID).click();
}

// Carrega o modelo

let model;

(async function () {
	
	model = await tf.loadModel('../modelos/model.json');
	$('.progress-bar').hide();

})();


// Faz previsões na imagem
$("#predict-button").click(async function () {
	
	let image = undefined;
	
	image = $('#selected-image').get(0);
	
	// Pré-processamento da imagem
	let tensor = tf.fromPixels(image).resizeNearestNeighbor([96,96]).toFloat().div(tf.scalar(255.0)).expandDims();
	
	// Faz previsões com o modelo
	let predictions = await model.predict(tensor).data();

	// Coleta as previsões
	let top5 = Array.from(predictions).map(function (p, i) { return {probability: p, className: TARGET_CLASSES[i] };
		}).sort(function (a, b) {return b.probability - a.probability;	
		}).slice(0, 3);
	
		
		$("#prediction-list").append(`<li class="w3-text-blue fname-font" style="list-style-type:none;">${file_name}</li>`);
		
		top5.forEach(function (p) {
		
			$("#prediction-list").append(`<li style="list-style-type:none;">${p.className}: ${p.probability.toFixed(3)}</li>`);
		
			
		});
	
	
});


// Leitura das imagens para previsão em batch
$("#image-selector").change(async function () {
	
	fileList = $("#image-selector").prop('files');
	model_processArray(fileList);
	
});





