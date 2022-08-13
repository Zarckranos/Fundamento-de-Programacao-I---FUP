#473219 - Matheus do Vale Almeida
#473673 - Mateus Leal Gonçalves

import sys
from Funcoes.funcoes import Funcoes
from Funcoes.funcoesPeca import FuncoesPeca
from Funcoes.funcoesDama import FuncoesDama
#Chamando as classes
funcoes = Funcoes()
funcoesPeca = FuncoesPeca()
funcoesDama = FuncoesDama()

pecasBaixo = 0
pecasCima = 0
M = []
venc = False
lis = ["A","B","C","D","E","F","G","H","I","J"]

for i in range(10):
    lista = [" "]*10
    M.append(lista)

funcoes.setTabuleiro(M)

if len(sys.argv) == 1:
    print(">>USUARIO VS. USUARIO<<")
    print()
else:
    arquivo = open(sys.argv[1],'r')
    lines = arquivo.readlines()
    print(">>MODO OFFLINE<<")
    print()

if len(sys.argv) == 1:
    jogador = input(">>Informe o primeiro jogador(C ou B): ")
else:
    jogador = lines[0].strip("\n")

play = "Erro"
w = 1
#Enquanto nao houver vencendor, continua a jogar
while venc == False:
#Entrada de Jogador inicial é válida?
    if jogador == "C" or jogador == "B":
        funcoes.dama(M)
        funcoes.tabuleiro(M, pecasCima, pecasBaixo)
        print()

        if  len(sys.argv) != 1:
            if w >= len(lines):
                break

        #Enquanto a entrada jogada for falsa mantenha o loop        
        while play != "Ok":
            if len(sys.argv) == 1:
                jogada = input(">>Digite a posicao da jogada: ")
            else:
                if w < len(lines):
                    jogada = lines[w].strip("\n")
                    if (w+1) == len(lines):
                        input("")
                else:
                    break
                w = w + 1

            listaI, listaF = funcoes.podeComer(M, jogador)#Existem peças a serem capturadas?
            play, peca = funcoes.verEntrada(jogador, M, lis, jogada, listaI, listaF, play)
            #play recebendo erro -> Entrada inválida
            if play == "Erro":
                if peca == 0:
                    if len(sys.argv) == 1:
                        print(">>Entrada inválida!")
                        print(">>Ex.: 'B0--C1'")
                        print()
                    else:
                        print("Jogada invalida na linha {} do arquivo de entrada.".format(w))
                        input("Aperte <ENTER> para continuar")
                        print()
                if peca == 1:
                    if len(sys.argv) == 1:
                        print(">>Existe uma captura disponível")
                    else:
                        print("Jogada invalida na linha {} do arquivo de entrada.".format(w))
                        input("Aperte <ENTER> para continuar")
                        print()

            if play == "Mover":
                if peca == "o" or peca == "@":
                    play = funcoesPeca.verEntradaPeca(M, jogada, lis, jogador)
                    if play == "Erro":
                        if len(sys.argv) == 1: 
                            print(">>Entrada invalida!")
                            print()
                        else:
                            print("Jogada invalida na linha {} do arquivo de entrada.".format(w))
                            input("Aperte <ENTER> para continuar")
                            print()
                else:
                    play = funcoesDama.verEntradaDama(jogador, M, jogada, lis)
                    if play == "Erro":
                        if len(sys.argv) == 1: 
                            print(">>Entrada invalida!")
                            print()
                        else:
                            print("Jogada invalida na linha {} do arquivo de entrada.".format(w))
                            input("Aperte <ENTER> para continuar")
                            print()

                         
            if jogador == "C":
                if play == "Comer":
                    if peca == "o" or peca == "O":
                        if peca == "o":
                            funcoesPeca.comer_Peca(jogada, peca, jogador, M, lis)
                            pecasBaixo = pecasBaixo + 1

                            funcoes.dama(M)
                            funcoes.tabuleiro(M, pecasCima, pecasBaixo)
                            print("O jogador ainda possui movimentos")
                        else:
                            listaCasas = funcoesDama.verificar_Casas(listaI, listaF, M, jogada, lis)
                            play = funcoesDama.comer_Dama(jogada, jogador, M, lis, listaCasas)
                            if play == "Comer":
                                pecasBaixo = pecasBaixo + 1
                                
                                funcoes.dama(M)
                                funcoes.tabuleiro(M,pecasCima,pecasBaixo)
                                print(">>O jogador ainda possui movimentos")
                            else:
                                if len(sys.argv) == 1:
                                    print("Entrada inválida")
                                else:
                                    print("Jogada invalida na linha {} do arquivo de entrada.".format(w))
                                    input("Aperte <ENTER> para continuar")
                                    print()
                if play == "Mover":
                    play = funcoes.moverJCima(peca, jogada, lis, M)

            else:
                if play == "Comer":
                    if peca == "@" or peca == "&":
                        if peca == "@":
                            funcoesPeca.comer_Peca(jogada, peca, jogador, M, lis)
                            pecasCima = pecasCima + 1
                            
                            funcoes.dama(M)
                            funcoes.tabuleiro(M, pecasCima, pecasBaixo)
                            print(">>O jogador ainda possui movimentos")
                        else:
                            listaCasas = funcoesDama.verificar_Casas(listaI, listaF, M, jogada, lis)
                            play = funcoesDama.comer_Dama(jogada, jogador, M, lis, listaCasas)
                            if play == "Comer":
                                pecasCima = pecasCima + 1
                                
                                funcoes.dama(M)
                                funcoes.tabuleiro(M, pecasCima, pecasBaixo)
                                print("O jogador ainda possui movimentos")
                            else:
                                if len(sys.argv) == 1:
                                    print("Entrada invalida")
                                else:
                                    print("Jogada invalida na linha {} do arquivo de entrada.".format(w))
                                    input("Aperte <ENTER> para continuar")
                                    print()
                if play == "Mover":    
                    play = funcoes.moverJBaixo(peca, jogada, lis, M)

        jogador = funcoes.oJogador(jogador)
        play = "Erro"

        if pecasBaixo == 15:
            venc = True
            print(">>Jogador <CIMA> vitorioso")
        elif pecasCima == 15:
            venc = True
            print(">>Jogador <BAIXO> vitorioso")
        if len(sys.argv) == 1:
            if venc == True:
                reiniciar = input(">>Gostaria de recomeçar o jogo(S ou N ):")
                if reiniciar == "S":
                    venc = False
                    pecasBaixo = 0
                    pecasCima = 0
                    funcoes.setTabuleiro(M)
                    jogador = input(">>Informe o primeiro jogador(C ou B): ")

    else:
        print(">>Não é um jogador válido. Tente 'C' ou 'B'")
        jogador = input(">>Informe o primeiro jogador(C ou B): ")
        print()
