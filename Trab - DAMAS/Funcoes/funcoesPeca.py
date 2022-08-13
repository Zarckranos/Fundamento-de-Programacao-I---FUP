class FuncoesPeca:
	def verEntradaPeca(self, matriz, jogada, lista, jogador):
		for i in range(10):
			if jogada[0] == lista[i]:
				v1 = i
			if jogada[4] == lista[i]:
				v2 = i
		if jogador == "C":
			if (int(jogada[1]) - int(jogada[5]) == -1) and abs(v1 - v2) == 1:
				return "Mover"
			else:
				return "Erro"
		else:
			if (int(jogada[1]) - int(jogada[5]) == 1) and abs(v1 - v2) == 1:
				return "Mover"
			else:
				return "Erro"

	def comer_Peca(self, jogada, peca, jogador, matriz, lista):
		for i in range(10):
			if jogada[0] == lista[i]:
				v1 = i
			if jogada[4] == lista[i]:
				v2 = i
		if jogador == "C":
			matriz[int(jogada[1])][v1] = " "
			matriz[int(jogada[5])][v2] = "o"
			#Movendo para baixo
			if int(jogada[5]) > int(jogada[1]):
				#Movendo para direita
				if v2 > v1:
					matriz[int(jogada[1])+1][v1+1] = " "
				else:
					matriz[int(jogada[1])+1][v1-1] = " "
			else:
				if v2 > v1:
					matriz[int(jogada[1])-1][v1+1] = " "
				else:
					matriz[int(jogada[1])-1][v1-1] = " "
		else:
			matriz[int(jogada[1])][v1] = " "
			matriz[int(jogada[5])][v2] = "@"
			#Movendo para baixo
			if int(jogada[5]) > int(jogada[1]):
				#Movendo para direita
				if v2 > v1:
					matriz[int(jogada[1])+1][v1+1] = " "
				else:
					matriz[int(jogada[1])+1][v1-1] = " "
			else:
				if v2 > v1:
					matriz[int(jogada[1])-1][v1+1] = " "
				else:
					matriz[int(jogada[1])-1][v1-1] = " "