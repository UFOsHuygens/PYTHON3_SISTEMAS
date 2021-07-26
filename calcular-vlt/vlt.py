pergunta = input("Velocidade(1) x Distancia(2) x Tempo(3): ")
if pergunta == "1":
	distancia1 = int(input("Qual a distancia? (m): "))
	tempo1 = int(input("Qual o tempo levado? (s): "))
	velocidade1 = distancia1 / tempo1
	print(f"A velocidade medida é de {velocidade1} m/s")
if pergunta == "2":
	velocidade2 = int(input("Qual a velocidade? (m/s): "))
	tempo2 = int(input("Qual o tempo levado? (s): "))
	distancia2 = velocidade2 * tempo2
	print(f"A distancia medida é de {distancia2} metros")
if pergunta == "3":
	velocidade3 = int(input("Qual a velocidade? (m/s): "))
	distancia3 = int(input("Qual a distancia? (m): "))
	tempo3 = velocidade3 * distancia3
	print(f"O tempo medido é de {tempo3} (s)")