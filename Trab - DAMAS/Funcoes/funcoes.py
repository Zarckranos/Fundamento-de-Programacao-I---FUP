class Funcoes:
	def setTabuleiro(self, matriz):
		for l in range(10):
		    for c in range(10):
		        if (l + c) % 2 == 0:
		            matriz[l][c] = "#"
		for l in range(10):
		    for c in range(10):
		        if l <= 2:
		            if (l + c) % 2 != 0:
		                matriz[l][c] = "o"
		        if l <= 10 and l >= 7:
		            if (l + c) % 2 != 0:
		                matriz[l][c] = "@"
		        if l > 2 and l < 7:
		        	if (l + c) % 2 != 0:
		        		matriz[l][c] = " "

	#Altera o turno dos jogadores
	def oJogador(self, jogador):
		if jogador == "C":
			jogador = "B"
			print(">>Turno do jogador >{}<".format(jogador))
			return jogador
		if jogador == "B":
			jogador = "C"
			print(">>Turno do jogador >{}<".format(jogador))
			return jogador 

	#Printa o tabuleiro
	def tabuleiro(self, matriz, pecasCima ,pecasBaixo):
		print("  A B C D E F G H I J")
		for l in range(10):
			if l == 3 or l == 7:
				if l == 3:
					print(" +-+-+-+-+-+-+-+-+-+-+     Jogador(C): {} peca(s) capturadas".format(pecasBaixo))
				else:
					print(" +-+-+-+-+-+-+-+-+-+-+     Jogador(B): {} peca(s) capturadas".format(pecasCima))
			else:
				print(" +-+-+-+-+-+-+-+-+-+-+")
			print ("{}|".format(l), end="")
			for c in range(10):
				print(matriz[l][c], end="|")
			print(l)	
		print(" +-+-+-+-+-+-+-+-+-+-+")
		print("  A B C D E F G H I J")
		print()

	#Transforma uma peca em dama
	def dama(self, matriz):
		for i in range(10):
			if matriz[0][i] == "@":
				matriz[0][i] = "&"
			if matriz[9][i] == "o":
				matriz[9][i] = "O"

	#mover as pecas do jogador de cima
	def moverJCima(self, peca, jogada, lista, matriz):
		for i in range(10):
			if jogada[0] == lista[i]:
				v1 = i
			if jogada[4] == lista[i]:
				v2 = i
		if peca == "o" or peca == "O":
			if peca == "o":
				matriz[int(jogada[1])][v1] = " "
				matriz[int(jogada[5])][v2] = "o"
				return "Ok"
			#No caso de uma dama
			else:
				matriz[int(jogada[1])][v1] = " "
				matriz[int(jogada[5])][v2] = "O"
				return "Ok"

	#mover as pecas do jogador de baixo
	def moverJBaixo(self, peca, jogada, lista, matriz):
		for i in range(10):
			if jogada[0] == lista[i]:
				v1 = i
			if jogada[4] == lista[i]:
				v2 = i
		if peca == "@" or peca == "&":
			if peca == "@":
				matriz[int(jogada[1])][v1] = " "
				matriz[int(jogada[5])][v2] = "@"
				return "Ok"
			#No caso de uma dama
			else:
				matriz[int(jogada[1])][v1] = " "
				matriz[int(jogada[5])][v2] = "&"
				return "Ok"

	def podeComer(self, matriz, jogador):
		listaI = []
		listaF = []
		if jogador == "C":
			for l in range(10):
				for c in range(10):
					if matriz[l][c] == "o":
						if l > 1 and c > 1:
							#Diagonal superior esquerdo
							if matriz[l-1][c-1] == "@" or matriz[l-1][c-1] == "&":
								if matriz[l-2][c-2] == " ":
									listaI.append([l,c])
									listaF.append([l-2,c-2])

						if l > 1 and c < 8:
							#Diagonal superior direito
							if matriz[l-1][c+1] == "@" or matriz[l-1][c+1] == "&":
								if matriz[l-2][c+2] == " ":
									listaI.append([l,c])
									listaF.append([l-2,c+2])

						if l < 8 and c > 1:
							#Diagonal inferior esquerdo
							if matriz[l+1][c-1] == "@" or matriz[l+1][c-1] == "&":
								if matriz[l+2][c-2] == " ":
									listaI.append([l,c])
									listaF.append([l+2,c-2])

						if l < 8 and c < 8:
							#Diagonal inferior direito
							if matriz[l+1][c+1] == "@" or matriz[l+1][c+1] == "&":
								if matriz[l+2][c+2] == " ":
									listaI.append([l,c])
									listaF.append([l+2,c+2])

					if matriz[l][c] == "O":
						#Diagonal superior esquerdo
						if l > 1 and c > 1:
							w = 1
							if l < c:
								k = l #4, 5 
							else:
								k = c
							while w < k:
								if matriz[l-w][c-w] == "o" or matriz[l-w][c-w] == "O":
									w = 100
								else:
									if matriz[l-w][c-w] == "@" or matriz[l-w][c-w] == "&":
										if matriz[l - w - 1][c - w - 1] == " ":
											listaI.append([l,c])
											listaF.append([l-w-1, c-w-1])
											w = 100
										w = 100
								w = w + 1

						#Diagonal superior direito
						if l > 1 and c < 8:
							w = 1
							if (l + c) > 8:
								while w <= (8-c):
									if matriz[l-w][c+w] == "o" or matriz[l-w][c+w] == "O":
										w = 100
									else:
										if matriz[l-w][c+w] == "@" or matriz[l-w][c+w] == "&":
											if matriz[l-w-1][c+w+1] == " ":
												listaI.append([l,c])
												listaF.append([l-w-1, c+w+1])
												w = 100
											w = 100
									w = w + 1 
							else:
								while w < l - 1:
									if matriz[l-w][c+w] == "o" or matriz[l-w][c+w] == "O":
										w = 100
									else:
										if matriz[l-w][c+w] == "@" or matriz[l-w][c+w] == "&":
											if matriz[l-w-1][c+w+1] == " ":
												listaI.append([l,c])
												listaF.append([l-w-1][c+w+1])
												w = 100
											w = 100
									w = w + 1

						#Diagonal inferior esquerdo
						if l < 8 and c > 1:
							w = 1
							if (l+c) < 10:
								while w <= (c-1):
									if matriz[l+w][c-w] == "o" or matriz[l+w][c-w] == "O":
										w = 100
									else:	
										if matriz[l+w][c-w] == "@" or matriz[l+w][c-w] == "&":
											if matriz[l+w+1][c-w-1] == " ":
												listaI.append([l,c])
												listaF.append([l+w+1, c-w-1])
												w = 100
											w = 100
									w = w + 1
							else:
								while w < (9-l):
									if matriz[l+w][c-w] == "o" or matriz[l+w][c-w] == "O":
										w = 100
									else:	
										if matriz[l+w][c-w] == "@" or matriz[l+w][c-w] == "&":
											if matriz[l+w+1][c-w-1] == " ":
												listaI.append([l,c])
												listaF.append([l+w+1, c-w-1])
												w = 100
											w = 100
									w = w + 1

						#Diagonal inferior direito
						if l < 8 and c <8:
							w = 1
							if (l-c) < 0:
								while w < (9-c):
									if matriz[l+w][c+w] == "o" or matriz[l+w][c+w] == "O":
										w = 100
									else:
										if matriz[l+w][c+w] == "@" or matriz[l+w][c+w] == "&":
											if matriz[l+w+1][c+w+1] == " ":
												listaI.append([l,c])
												listaF.append([l+w+1, c+w+1])
												w = 100
											w = 100
									w = w + 1
							else:
								while w < (9-l):
									if matriz[l+w][c+w] == "o" or matriz[l+w][c+w] == "O":
										w = 100
									else:	
										if matriz[l+w][c+w] == "@" or matriz[l+w][c+w] == "&":
											if matriz[l+w+1][c+w+1] == " ":
												listaI.append([l,c])
												listaF.append([l+w+1, c+w+1])
												w = 100
											w = 100
									w = w + 1

		else:
			for l in range(10):
				for c in range(10):
					if matriz[l][c] == "@":
						if l > 1 and c > 1:
							#Diagonal superior esquerdo
							if matriz[l-1][c-1] == "o" or matriz[l-1][c-1] == "O":
								if matriz[l-2][c-2] == " ":
									listaI.append([l,c])
									listaF.append([l-2,c-2])
									
						if l > 1 and c < 8:
							#Diagonal superior direito
							if matriz[l-1][c+1] == "o" or matriz[l-1][c+1] == "O":
								if matriz[l-2][c+2] == " ":
									listaI.append([l,c])
									listaF.append([l-2,c+2])

						if l < 8 and c > 1:
							#Diagonal inferior esquerdo
							if matriz[l+1][c-1] == "o" or matriz[l+1][c-1] == "O":
								if matriz[l+2][c-2] == " ":
									listaI.append([l,c])
									listaF.append([l+2,c-2])

						if l < 8 and c < 8:
							#Diagonal inferior direito
							if matriz[l+1][c+1] == "o" or matriz[l+1][c+1] == "O":
								if matriz[l+2][c+2] == " ":
									listaI.append([l,c])
									listaF.append([l+2,c+2])

					if matriz[l][c] == "&":				
					#Diagonal superior esquerdo
						if l > 1 and c > 1:
							w = 1
							if l < c:
								k = l
							else:
								k = c
							while w < k:
								if matriz[l-w][c-w] == "@" or matriz[l-w][c-w] == "&":
									w = 100
								else:
									if matriz[l-w][c-w] == "o" or matriz[l-w][c-w] == "O":
										if matriz[l - w - 1][c - w - 1] == " ":
											listaI.append([l,c])
											listaF.append([l-w-1, c-w-1])
											w = 100
										w = 100
								w = w + 1

						#Diagonal superior direito
						if l > 1 and c < 8:
							w = 1
							if (l + c) > 8:
								while w <= (8-c):
									if matriz[l-w][c+w] == "@" or matriz[l-w][c+w] == "&":
										w = 100
									else:
										if matriz[l-w][c+w] == "o" or matriz[l-w][c+w] == "O":
											if matriz[l-w-1][c+w+1] == " ":
												listaI.append([l,c])
												listaF.append([l-w-1, c+w+1])
												w = 100
											w = 100
									w = w + 1 
							else:
								while w < l - 1:
									if matriz[l-w][c+w] == "@" or matriz[l-w][c+w] == "&":
										w = 100
									else:
										if matriz[l-w][c+w] == "o" or matriz[l-w][c+w] == "O":
											if matriz[l-w-1][c+w+1] == " ":
												listaI.append([l,c])
												listaF.append([l-w-1][c+w+1])
												w = 100
											w = 100
									w = w + 1

						#Diagonal inferior esquerdo
						if l < 8 and c > 1:
							w = 1
							if (l+c) < 10:
								while w <= (c-1):
									if matriz[l+w][c-w] == "@" or matriz[l+w][c-w] == "&":
										w = 100
									else:
										if matriz[l+w][c-w] == "o" or matriz[l+w][c-w] == "O":
											if matriz[l+w+1][c-w-1] == " ":
												listaI.append([l,c])
												listaF.append([l+w+1, c-w-1])
												w = 100
											w = 100
									w = w + 1 
							else:
								while w < (9-l):
									if matriz[l+w][c-w] == "@" or matriz[l+w][c-w] == "&":
										w = 100
									else:
										if matriz[l+w][c-w] == "o" or matriz[l+w][c-w] == "O":
											if matriz[l+w+1][c-w-1] == " ":
												listaI.append([l,c])
												listaF.append([l+w+1, c-w-1])
												w = 100
											w = 100
									w = w + 1

						#Diagonal inferior direito
						if l < 8 and c <8:
							w = 1
							if (l-c) < 0:
								while w < (9-c):
									if matriz[l+w][c+w] == "@" or matriz[l+w][c+w] == "&":
										w = 100
									else:
										if matriz[l+w][c+w] == "o" or matriz[l+w][c+w] == "O":
											if matriz[l+w+1][c+w+1] == " ":
												listaI.append([l,c])
												listaF.append([l+w+1, c+w+1])
												w = 100
											w = 100
									w = w + 1
							else:
								while w < (9-l):
									if matriz[l+w][c+w] == "@" or matriz[l+w][c+w] == "&":
										w = 100
									else:
										if matriz[l+w][c+w] == "o" or matriz[l+w][c+w] == "O":
											if matriz[l+w+1][c+w+1] == " ":
												listaI.append([l,c])
												listaF.append([l+w+1, c+w+1])
												w = 100
											w = 100
									w = w + 1				
					
		return listaI, listaF

	#Verifica a entrada
	def verEntrada(self, jogador, matriz, lista, jogada, listaI, listaF, play):
		#Erro: para entrada invalida; Mover: para mover; Comer: para comer
		#Verificando o valor padrao da entrada
		if len(jogada) == 6:
			if jogador == "C":
				#Verificando range
				if jogada[0] not in list(lista) or jogada[4] not in list(lista) or 0 > int(jogada[1]) > 9 or 0 > int(jogada[5]) > 9:
					return "Erro", 0
				else:
					#Alterando o valor string para inteiro
					for i in range(10):
						if jogada[0] == lista[i]:
							v1 = i
						if jogada[4] == lista[i]:
							v2 = i
					#Se a posicao inicial e a peca do jogador e se a final pode ser preenchida
					if matriz[int(jogada[1])][v1] == "o" or matriz[int(jogada[1])][v1] == "O":	
						#vai ser aqui
						if matriz[int(jogada[5])][v2] == " ":
							if len(listaI) > 0:
								#Comparando a entrada com os valores na lista
								if [int(jogada[1]),v1] in listaI:	
									return "Comer", matriz[int(jogada[1])][v1]
								else:
									return "Erro", 1
							else:
								return "Mover", matriz[int(jogada[1])][v1]							
						else:
							return "Erro", 0
					else:
						return "Erro", 0
			#praticamente o espelho do if, com a diferenca do jogador
			else:
				#Verificando range
				if jogada[0] not in list(lista) or jogada[4] not in list(lista) or 0 > int(jogada[1]) > 9 or 0 > int(jogada[5]) > 9:
					return "Erro", 0
				else:
					#Alterando o valor string para inteiro
					for i in range(10):
						if jogada[0] == lista[i]:
							v1 = i
						if jogada[4] == lista[i]:
							v2 = i
					#Se a posicao inicial e a peca do jogador e se a final pode ser preenchida
					if matriz[int(jogada[1])][v1] == "@" or matriz[int(jogada[1])][v1] == "&":	
						#vai ser aqui
						if matriz[int(jogada[5])][v2] == " ":
							if len(listaI) > 0:
								#Comparando a entrada com os valores na lista
								if [int(jogada[1]),v1] in listaI:	
									return "Comer", matriz[int(jogada[1])][v1]
								else:
									return "Erro", 1
							else:
								return "Mover", matriz[int(jogada[1])][v1]					
						else:
							return "Erro", 0
					else:
						return "Erro", 0
		else:
			return "Erro", 0