// Script para previsoes com o modelo

// Função para previsões com o modelo
async function model_makePrediction(fname) {
	
	let image = undefined;
	
	image = $('#selected-image').get(0);
	
	// Pré-processamento da imagem
	let tensor = tf.fromPixels(image).resizeNearestNeighbor([96,96]).toFloat().div(tf.scalar(255.0)).expandDims();

	// Previsões
	let predictions = await model.predict(tensor).data();

	// Coleta as previsões
	let top5 = Array.from(predictions).map(function (p, i) { return {probability: p, className: TARGET_CLASSES[i] };
		}).sort(function (a, b) {return b.probability - a.probability;		
		}).slice(0, 3);
		
	// Adiciona o nome do arquivo à lista de previsões
	$("#prediction-list").append(`<li class="w3-text-blue fname-font" style="list-style-type:none;">
	${fname}</li>`);
	
	top5.forEach(function (p) {
	
		$("#prediction-list").append(`<li style="list-style-type:none;">${p.className}: ${p.probability.toFixed(3)}</li>`);
	
		
	});
	
	// Adiciona um espaço após prever cada imagem
	$("#prediction-list").append(`<br>`);
		
}

// Função para evitar problemas com o delay do modelo
function model_delay() {
	
	return new Promise(resolve => setTimeout(resolve, 200));
}

// Função para sync do carregamento do modelo
async function model_delayedLog(item, dataURL) {
	
	await model_delay();
	
	$("#selected-image").attr("src", dataURL);
	$("#displayed-image").attr("src", dataURL); 
	
}

// Função para processar o modelo
async function model_processArray(array) {
	
	for(var item of fileList) {
		
		let reader = new FileReader();
		
		let file = undefined;
	
		reader.onload = async function () {
			
			let dataURL = reader.result;
			
			await model_delayedLog(item, dataURL);
			
			var fname = file.name;
			
			$("#prediction-list").empty();
			
			await model_makePrediction(fname);
		}
		
		file = item;
			
		reader.readAsDataURL(file);
	}
}













