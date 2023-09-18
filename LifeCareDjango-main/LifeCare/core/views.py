from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
	return render(request, 'index.html')

def faqs(request):
	pre_fre = '''
		<body>
			<section class="content-faq">
				<div><h1>PREGUNTAS FRECUENTES</h1></div>
				<details>
					<summary>
						<h2>Básicas p/cualquier Centro Médico:</h2>
					</summary>
					<section class="answer-1">
						<details>
							<summary>
								1) ¿Tengo que registrarme para reservar un turno?
							</summary>
							<div>
								<p>Sí, hay que registrarse con usuario y contraseña.</p>
							</div>
						</details>
						<details>
							<summary>
								2) ¿Puedo cancelar, si tengo algún inconveniente?
							</summary>
							<div>
								<p>Sí, puede cancelar y reprogramar para otra fecha disponible.</p>
							</div>
						</details>
						<details>
							<summary>
								3) ¿Qué documentación debo llevar cuando asista al turno?
							</summary>
							<div>
								<p>Cuando hace la reserva y se le concede el turno (según disponibilidad), se le envía en forma automática un mensaje al correo electrónico que suministró al momento de registrarse como usuario.</p>
							</div>
						</details>
						<details>
							<summary>
								4) ¿Debo asistir en ayunas al turno solicitado?
							</summary>
							<div>
								<p>Según la clase de turno que solicitó, el especialista le estará informando por email, en qué condiciones debe asistir al turno solicitado.</p>
							</div>
						</details>
					</section>
				</details>
				<details>
					<summary>
						<h2>Lo que se puede hacer y no se puede hacer en Lifecare...</h2>
					</summary>
					<section class="answer-2">
						<details>
							<summary>
								1) ¿Se puede fumar en la recepción/sala de espera?
							</summary>
							<div>
								<p>No, está prohibido por ley fumar en cualquier lugar dentro de Lifecare.</p>
							</div>
						</details>
						<details>
							<summary>
								2) ¿Puedo usar el celular en la sala de espera?
							</summary>
							<div>
								<p>No, no se permite el uso de aparatos con radiofrecuencia, dentro de Lifecare, sólo por el simple hecho de que producen interrupciones en instrumentos de medición muy precisos que son utilizados para estudios de los pacientes.</p>
							</div>
						</details>
						<details>
							<summary>
								3) ¿Puedo llevar una mascota en el horario de visita para ver a un familiar internado?
							</summary>
							<div>
								<p>No, no se permite el ingreso de ninguna especia ni de tamaño de mascotas en general. Por una cuestión bacterio-virósica.</p>
							</div>
						</details>
						<details>
							<summary>
								4) ¿Puedo quedarme a cuidar a un familiar internado fuera del horario de visitas?
							</summary>
							<div>
								<p>No en la habitación, pero sí puede quedarse en el hall/sala de espera de Lifecare, si es que hay sillones disponibles.</p>
							</div>
						</details>
					</section>
				</details>
				<details>
					<summary>
						<h2>Lo que tiene y no tiene Lifecare...</h2>
					</summary>
					<section class="answer-3">
						<details>
							<summary>
								1) ¿Tienen para hacer análisis de sangre, hiv, adn, etc.?
							</summary>
							<div>
								<p>Sí, tenemos p/realizar todos esos tests y análisis.</p>
							</div>
						</details>
						<details>
							<summary>
								2) ¿Cuentan con máquina para Resonancia Magnética?
							</summary>
							<div>
								<p>No, poseemos aparatología p/Resonancias Magnéticas.</p>
							</div>
						</details>
						<details>
							<summary>
								3) ¿Cuentan con camas para internación de urgencia?
							</summary>
							<div>
								<p>Sí, según disponibilidad diaria.</p>
							</div>
						</details>
						<details>
							<summary>
								4) ¿Tienen sala para cirujía?
							</summary>
							<div>
								<p>Sí, sólo cirujía básica y menor. Si la operación es de alta complejidad, se deriva (según disponibilidad) al sanatorio especializado más próximo de la zona.</p>
							</div>
						</details>
					</section>
				</details>
			</section>
			<style>
				h1{text-align: center;}

				.answer-1 details{background: lightcyan;}
				.answer-1 details div{background: lightgreen;}

				.answer-2 details{background: lightgoldenrodyellow;}
				.answer-2 details div{background: lightsalmon;}

				.answer-3 details{background: lightsteelblue;}
				.answer-3 details div{background: lightpink;}

				details{
					background:#f2f2f2; padding: .5rem; border-radius: 6px;
					margin: .5rem; cursor: pointer;
				}

				summary{list-style: none;}
				details[open] summary ~ *{animation: sweep 1.8s ease-in-out;}

				summary::before{content: '+'; padding-right: 1rem;}

				.content-faq > details[open] > summary::before{content: '-';}
				
				.answer-1 > details[open] summary::before{content: '-';}
				.answer-2 > details[open] summary::before{content: '-';}
				.answer-3 > details[open] summary::before{content: '-';}

				@keyframes sweep{
					from{opacity: 0; margin-top: -10px;}
					to{opacity: 1; margin-top: 0;}
				}
			</style>
		</body>'''
	return HttpResponse(pre_fre)

