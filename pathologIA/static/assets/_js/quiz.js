// Recupera id='question' em quiz.html
const question = document.getElementById('question');
// Recupera a classe 'choice-text' em quiz.html.
// Esta classe recupera o número da alternativa da questão que varia entre 1 a 5
const choices = Array.from(document.getElementsByClassName ('choice-text'));
// Recupera o id do contador do número de questões id="questionCounter" em quiz.html
const questionCounterText = document.getElementById('questionCounter');
// Recupera o id do score que é a pontuação contabilizada do estudante quiz.html
const scoreText = document.getElementById('score');
// Recupera o id da imagem a ser exibida na questão em quiz.html
const image = document.getElementById('image');
// Declaração do objeto currentQuestion que armazena a questão atual a ser respondida
// Ele possui como chave image, question, choice1, choice2, choice3, choice4, choice5, answer e help.
// Possui como valor arquivo de imagem, descrição da question, descrição da alternativa 1, 2, 3, 4 e 5,
// descrição do número da questão e a ajuda.
let currentQuestion = {};
// Declarando a resposta do usuário
let acceptingAnswers = false;
// Declarando a pontuação
let score = 0;
// Declarando contador de questões
let questionCounter = 0;
// Declarando um vetor de perguntas disponíveis
let availableQuestions = [];

// Declarando um array de cinco elementos denominado 'questions'. Cada elemento do array será um objeto.
// Cada objeto é uma questão a ser respondida. Ele será um hash do tipo chave - valor.
// Cada chave é uma alternativa denominada 'choice' e o valor a descrição da alternativa.
let questions =
[ 
{
	image: "img/image1.png",
    question: "Um homem de 29 anos procura atendimento médico por apresentar tosse e febre há 2 dias. Há 2 meses tratou infecção de garganta com cefalexina	por 2 semanas. O seu estado clínico é bom e o médico opta por tratamento domiciliar. Os seguintes tratamentos são recomendados, EXCETO:",
	choice1: "ciprofloxacina + claritromicina.",
    choice2: "moxifloxacina.",
    choice3: "amoxicilina em dose alta + doxiciclina.",
    choice4: "amoxicilina/clavulanato + azitromicina.",
	choice5: "cefuroxima + azitromicina.",
    answer: 1,
    help: "D -> A",
  },
{
	image: "img/image2.png",
	question: "Um homem de 40 anos, alcoolista, procura atendimento	médico com queixa de sudorese noturna, fadiga e anorexia há 10 dias, acrescidos de febre e tosse com expectoração abundante e fétida há 2 dias. Está hemodinamicamente estável, aparentando falta de cuidados, emagrecido e febril. Através da tomografia computadorizada de tórax qual conduta mais adequada?:",
	choice1: "iniciar vancomicina e uma cefalosporina com espectro para pseudomonas.",
	choice2: "iniciar ceftriaxona e clindamicina.",
	choice3: "ceftriaxona e vancomicina e locar dreno pleural para drenagem contínua.",
	choice4: "sustar antibióticos até realização de broncoscopia com aspirado do conteúdo da cavitação pulmonar, na	tentativa de se estabelecer a etiologia do processo.",
	choice5: "iniciar clindamicina e programar punção diagnóstica e esvaziadora do abscesso pulmonar por meio de videotoracoscopia.",
	answer: 2,
	help: "B -> B",
},
{
	image: "img/image3.png",
	question: "Um homem de 60 anos, tabagista, em uso de glimepirida, enalapril e hidroclorotiazida procura o pronto-socorro com queixa de dor precordial em aperto, irradiada para o braço	esquerdo, que se iniciou após forte emoção, há 1 hora. Está ansioso, com sudorese fria, pulso = 64 bat/min,	PA = 120 × 80 mmHg, com ausculta cardíaca e pulmonar normais. São colhidos exames laboratoriais e é medicado com morfina. A partir do que o ECG mostra, a conduta mais adequada a seguir é:",
	choice1: "betabloqueador, clopidogrel, inibidor da ECA, estatina e enoxaparina 40 mg.",
	choice2: "ácido acetilsalicílico, betabloqueador, clopidogrel, estatina	e alteplase.",
	choice3: "ácido acetilsalicílico, betabloqueador e enoxaparina 1 mg/kg.",
	choice4: "oxigênio em dose baixa, estatina e alteplase.",
	choice5: "clopidogrel, betabloqueador, estatina e estreptoquinase.",
	answer: 3,
	help: "D -> C",
},
{
	image: "img/image4.png",
	question: "Observe a radiografia de abdome apresentada abaixo e marque o que ela sugere:",
	choice1: "alça sentinela.",
	choice2: "pneumoperitônio (sinal de Rigler).",
	choice3: "sinal do empilhamento de moedas.",
	choice4: "sinais de líquido livre e sofrimento de alças intestinais.",
	choice5: "obstrução intestinal em alça fechada.",
	answer: 4,
	help: "D -> D",
},
{
	image: "img/image5.png",
	question: "Paciente de 7 anos, sexo masculino com dificuldade escolar e perda auditiva há 6 meses. De acordo com os achados de RM apresentados, qual o diagnóstico mais provavel?",
	choice1: "Esclerose múltipla.",
	choice2: "Doença de Pelizaeus Merzbacher.",
	choice3: "Encefalomielite disseminada aguda.",
	choice4: "Doença de Canavan.",
	choice5: "Adrenoleucodistrofia",
	answer: 5,
	help: "B -> E",
},
];

//Constants//
// Pontuação para resposta correta
const CORRECT_BONUS = 1;
// Pontuação em caso de uma segunda chance
// const HELP_BONUS = 0.75;
const HELP_BONUS = 0.50;
// Número máximo de questões
const MAX_QUESTIONS = 5;

// Função que inicia a contagem de pontos do questionário
startGame = () => {
	questionCounter = 0;
	score = 0;
	// O array [...questions] representa um número indefinido de questões. Lembrando que 'questions' é
	// um array de objetos do tipo hash.
	availableQuestions = [...questions];
	// Chamada da função getNewQuestion()
	getNewQuestion();
};

// Função getNewQuestion sem parâmetros. O símbolo '=>' é chamado de Arrow Function.
getNewQuestion = () => {
	// Se o array availableQuestions tiver comprimento idêntico a zero
	if(availableQuestions.length === 0 ) {
		// Criando um novo par de chave: valor, onde chave é a string 'mostRecentScore' e valor é o score.
		// score é a pontuação.
		localStorage.setItem('mostRecentScore', score);
		// Abre o histórico de pontuação na página end.html
		return window.location.assign("end.html")
	}

	// Incrementa a variável questionCounter em uma unidade. Ela conta a quantidade de questões.
	questionCounter++;
	// A variavel questionCounterText exibe como texto, o contador de questões e o número máximo de questões do questionário.
	questionCounterText.innerText = `${questionCounter}/${MAX_QUESTIONS}`
	// Math.random () é um método integrado que pode ser usado para gerar números aleatórios em JavaScript. A função retorna um valor entre 0 (inclusivo) e 1 (exclusivo), mas podemos usar outra função chamada Math.floor() para transformar nosso número em um número aleatório inteiro. Este número é multiplicado pelo número de questões armazenadas no array availableQuestions. O resultado deste cálculo será questionIndex ou a variável que armazena o índice de uma questão.
	const questionIndex = Math.floor(Math.random() * availableQuestions.length);
	// O objeto hash currentQuestion recebe a questão armazenada no número do elemento questionIndex do array availableQuestions
	currentQuestion = availableQuestions[questionIndex];
	// O objeto question.innerText recebe a descrição da questão atual
	question.innerText = currentQuestion.question;
	// image.src recebe a imagem contida no objeto currentQuestion
	image.src = currentQuestion.image;
	// O parâmetro choice percorre o array choices resgatando o número da alternativa selecionada como correta
	choices.forEach (choice => {
		// Resgata o número da alternativa marcada como correta
		const number = choice.dataset["number"];
		// Exibe a string 'choice' + o número da questão marcada como correta.
		choice.innerText = currentQuestion["choice" + number];
	});

	availableQuestions.splice(questionIndex, 1);
	acceptingAnswers = true;

};

var classToApply;
var gaveChance = false;

choices.forEach(choice => {
	choice.addEventListener ("click", e => {
		if(!acceptingAnswers) return;

		const selectedChoice = e.target;
		const selectedAnswer = selectedChoice.dataset["number"];

		classToApply = selectedAnswer == currentQuestion.answer ? 'correct' : 'incorrect';       	
        
        selectedChoice.parentElement.classList.add(classToApply);

        setTimeout( () => {
        	selectedChoice.parentElement.classList.remove(classToApply);
        }, 1200);
        
		if (gaveChance === true){
			if (classToApply === 'correct'){
				console.log("0.75")
				incrementScore(HELP_BONUS);
			}
			console.log("escolha",classToApply)
			gaveChance = false;
			setTimeout(() => {
				getNewQuestion()
			},1200);
			return;
		}

        if (classToApply === 'correct'){
			incrementScore(CORRECT_BONUS);
			setTimeout(() => {
				getNewQuestion()
			},1200);
			return;
		}

		console.log("errou!")
		setTimeout(() => {
		alert(currentQuestion.help)
		},100);
		gaveChance = true;
		        
	});	
});
        
incrementScore = num => {
	score += num;
	scoreText.innerText = score;
};

startGame();