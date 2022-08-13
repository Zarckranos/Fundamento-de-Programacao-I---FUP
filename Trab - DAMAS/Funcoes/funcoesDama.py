class FuncoesDama:
	def verEntradaDama(self, jogador, matriz, jogada, lista):
		play = "Erro"
		for i in range(10):
			if jogada[0] == lista[i]:
				v1 = i
			if jogada[4] == lista[i]:
				v2 = i
		if abs(int(jogada[1]) - int(jogada[5])) == (abs(v1 - v2)):
			k = 1
			if jogador == "C":
				if int(jogada[5]) > int(jogada[1]):			
					if v2 > v1:
						while k < (v2 - v1):
							if matriz[int(jogada[1])+k][v1+k] == "o" or matriz[int(jogada[1])+k][v1+k] == "O" or matriz[int(jogada[1])+k][v1+k] == "@" or matriz[int(jogada[1])+k][v1+k] == "&": 
								return play
							k = k + 1	
						return "Mover"
					else:
						while k < (v1 - v2):
							if matriz[int(jogada[1])+k][v1-k] == "o" or matriz[int(jogada[1])+k][v1-k] == "O" or matriz[int(jogada[1])+k][v1-k] == "@" or matriz[int(jogada[1])+k][v1-k] == "&":
								return play
							k = k + 1
						return "Mover"
				else:
					if v2 > v1:
						while k < (v2 - v1):
							if matriz[int(jogada[1])-k][v1+k] == "o" or matriz[int(jogada[1])-k][v1+k] == "O" or matriz[int(jogada[1])-k][v1+k] == "@" or  matriz[int(jogada[1])-k][v1+k] == "&":
								return play
							k = k + 1
						return "Mover"
					else:
						while k < (v1 - v2):
							if matriz[int(jogada[1])-k][v1-k] == "o" or matriz[int(jogada[1])-k][v1-k] == "O" or matriz[int(jogada[1])-k][v1-k] == "@" or matriz[int(jogada[1])-k][v1-k] == "&":
								return play
							k = k + 1
						return "Mover"
			else:
				if int(jogada[5]) > int(jogada[1]):			
					if v2 > v1:
						while k < (v2 - v1):
							if matriz[int(jogada[1])+k][v1+k] == "@" or matriz[int(jogada[1])+k][v1+k] == "&" or matriz[int(jogada[1])+k][v1+k] == "o" or matriz[int(jogada[1])+k][v1+k] == "O": 
								return play
							k = k + 1
						return "Mover"
					else:
						while k < (v1 - v2):
							if matriz[int(jogada[1])+k][v1-k] == "@" or matriz[int(jogada[1])+k][v1-k] == "&"  or matriz[int(jogada[1])+k][v1-k] == "o" or matriz[int(jogada[1])+k][v1-k] == "O":
								return play
							k = k + 1
						return "Mover"
				else:
					if v2 > v1:
						while k < (v2 - v1):
							if matriz[int(jogada[1])-k][v1+k] == "@" or matriz[int(jogada[1])-k][v1+k] == "&" or matriz[int(jogada[1])-k][v1+k] == "o" or matriz[int(jogada[1])-k][v1+k] == "O":
								return play
							k = k + 1
						return "Mover"
					else:
						while k < (v1 - v2):
							if matriz[int(jogada[1])-k][v1-k] == "@" or matriz[int(jogada[1])-k][v1-k] == "&" or matriz[int(jogada[1])-k][v1-k] == "o" or matriz[int(jogada[1])-k][v1-k] == "O":
								return play
							k = k + 1
						return "Mover"
		else:
			return play

	def verificar_Casas(self, listaI, listaF, matriz, jogada, lista):
		indice = []
		listaCasas = []
		for i in range(10):
			if jogada[0] == lista[i]:
				v1 = i
				
		for i in range(len(listaI)):
			if [int(jogada[1]), v1] == listaI[i]:
				indice.append(i)

		for w in range(len(indice)):
			posicao = listaF[indice[w]]
			#Movendo para baixo
			if posicao[0] > listaI[indice[w]][0]:
				#Movendo para direita
				if posicao[1] > listaI[indice[w]][1]:
					#Verificar quais posições pode parar
					if posicao[1] < 10 and posicao[0] < 10:
						#listaF contem o primeiro espaço em branco depois da peça que vai ser comida
						if posicao[0] > posicao[1]:
							limite = 9 - (posicao[0])+1
						else:
							limite = 9 - posicao[1]+1
						for k in range(limite):
							#Com um espaço vazio adiciona ele na listaF
							if matriz[posicao[0]+k][posicao[1]+k] == " ": 
								listaCasas.append([(posicao[0])+k, (posicao[1])+k])
							#No caso de não ser um espaço vazio -> em uma peça, ou seja, ele não pode passar dessa peça
							else:
								break
				else:
					if posicao[0] < 10 and posicao[1] >= 0:
						if posicao[0] + posicao[1] < 10:
							limite = posicao[1] + 1
						else:
							limite = 9 - posicao[0] + 1
						for k in range(limite):
							if matriz[posicao[0]+k][posicao[1]-k] == " ":
								listaCasas.append([posicao[0]+k, posicao[1]-k])
							else:
								break
			else:
				#Movendo para direita
				if posicao[1] > listaI[indice[w]][1]:
					if posicao[0] + posicao[1] < 10:
						limite = posicao[0]+1
					else:
						limite = 9 - posicao[1]+1
					for k in range(limite):
						if matriz[posicao[0]-k][posicao[1]+k] == " ":
							listaCasas.append([posicao[0]-k, posicao[1]+k])
						else:
							break
				else:
					if posicao[0] - posicao[1] < 0:
						limite = posicao[0]+1
					else:
						limite = posicao[1]+1
					for k in range(limite):
						if matriz[posicao[0]-k][posicao[1]-k] == " ":
							listaCasas.append([posicao[0]-k, posicao[1]-k])
						else:
							break
		return listaCasas

	def comer_Dama(self, jogada, jogador, matriz, lista, listaCasas):
		print("")
		k = 1
		for i in range(10):
			if jogada[0] == lista[i]:
				v1 = i
			if jogada[4] == lista[i]:
				v2 = i
		
		if jogador == "C":
			if [int(jogada[5]), v2] in listaCasas:
				matriz[int(jogada[1])][v1] = " "
				matriz[int(jogada[5])][v2] = "O"
				#Movendo para cima
				if int(jogada[1]) > int(jogada[5]):
					#Para esquerda
					if v1 > v2:
						while k < (v1 - v2):
							if matriz[int(jogada[5])+k][v2+k] == "@" or matriz[int(jogada[5])+k][v2+k] == "&": 
								matriz[int(jogada[5])+k][v2+k] = " "
								return "Comer"
							k = k + 1
					#Para direita
					else:
						while k < (v2 - v1):
							if matriz[int(jogada[5])+k][v2-k] == "@" or matriz[int(jogada[5])+k][v2-k] == "&":
								matriz[int(jogada[5])+k][v2-k] = " "
								return "Comer"
							k = k + 1
				#Movendo para baixo
				else:
					#Para esquerda
					if v1 > v2:
						while k < (v1 - v2):
							if matriz[int(jogada[5])-k][v2+k] == "@" or matriz[int(jogada[5])-k][v2+k] == "&":
								matriz[int(jogada[5])-k][v2+k] = " "
								return "Comer"
							k = k + 1
					#Para direita
					else:
						while k < (v2 - v1):
							if matriz[int(jogada[5])-k][v2-k] == "@" or matriz[int(jogada[5])-k][v2-k] == "&":
								matriz[int(jogada[5])-k][v2-k] = " "
								return "Comer"
							k = k + 1
			else:
				return "Erro"

		elif jogador == "B":
			if [int(jogada[5]),v2] in listaCasas:
				matriz[int(jogada[1])][v1] = " "
				matriz[int(jogada[5])][v2] = "&"
				#Movendo para cima
				if int(jogada[1]) > int(jogada[5]):
					#Para esquerda
					if v1 > v2:
						while k < (v1 - v2):
							if matriz[int(jogada[5])+k][v2+k] == "o" or matriz[int(jogada[5])+k][v2+k] == "O": 
								matriz[int(jogada[5])+k][v2+k] = " "
								return "Comer"
							k = k + 1
					#Para direita
					else:
						while k < (v2 - v1):
							if matriz[int(jogada[5])+k][v2-k] == "o" or matriz[int(jogada[5])+k][v2-k] == "O":
								matriz[int(jogada[5])+k][v2-k] = " "
								return "Comer"
							k = k + 1
				#Movendo para baixo
				else:
					#Para esquerda
					if v1 > v2:
						while k < (v1 - v2):
							if matriz[int(jogada[5])-k][v2+k] == "o" or matriz[int(jogada[5])-k][v2+k] == "O":
								matriz[int(jogada[5])-k][v2+k] = " "
								return "Comer"
							k = k + 1
					#Para direita
					else:
						while k < (v2 - v1):
							if matriz[int(jogada[5])-k][v2-k] == "o" or matriz[int(jogada[5])-k][v2-k] == "O":
								matriz[int(jogada[5])-k][v2-k] = " "
								return "Comer"
							k = k + 1
			else:
				return "Erro"