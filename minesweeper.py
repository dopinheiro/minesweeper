from random import randint
import string
import os
import time


def gera_tabuleiro():
	table = [['■' for coluna in range(40)] for linha in range(40)]
	return table

def popula_tabuleiro(tabuleiro):
	qtd_minas = int(input('Insira a quantidade de minas: '))
	# qtd_minas = 10
	for i in range(qtd_minas):
		while True:
			x = randint(0,len(tabuleiro)-1)
			y = randint(0,len(tabuleiro)-1)
			if tabuleiro[x][y] == '■':
				tabuleiro[x][y] = mina
				break

	for linha in range(len(tabuleiro)):
		for item in range(len(tabuleiro[linha])):
			dica = 0
			try:

				if tabuleiro[linha][item] != mina:
					# if linha or item == 0:
					# 	pass
					if linha == 0 and item == 0:
						if tabuleiro[linha][item+1] == mina:
							dica+=1
						if tabuleiro[linha+1][item] == mina:
							dica+=1
						if tabuleiro[linha+1][item+1] == mina:
							dica+=1

					elif linha == 0 and item == len(tabuleiro)-1:
						if tabuleiro[linha][item-1] == mina:
							dica+=1
						if tabuleiro[linha+1][item-1] == mina:
							dica+=1
						if tabuleiro[linha+1][item] == mina:
							dica+=1

					elif linha == len(tabuleiro)-1 and item == 0:
						if tabuleiro[linha-1][item] == mina:
							dica+=1
						if tabuleiro[linha-1][item+1] == mina:
							dica+=1
						if tabuleiro[linha][item+1] == mina:
							dica+=1

					elif linha == len(tabuleiro)-1 and item == len(tabuleiro)-1:
						if tabuleiro[linha-1][item-1] == mina:
							dica+=1
						if tabuleiro[linha-1][item] == mina:
							dica+=1
						if tabuleiro[linha][item-1] == mina:
							dica+=1

					elif linha == 0 and item > 0: # TODO: Verificar se não ocorrerá bug devido o tamanho do array
						if tabuleiro[linha][item-1] == mina:
							dica+=1
						if tabuleiro[linha][item+1] == mina:
							dica+=1
						if tabuleiro[linha+1][item-1] == mina:
							dica+=1
						if tabuleiro[linha+1][item] == mina:
							dica+=1
						if tabuleiro[linha+1][item+1] == mina:
							dica+=1

					elif linha > 0 and item == 0: # TODO: Verificar se não ocorrerá bug devido o tamanho do array
						if tabuleiro[linha-1][item] == mina:
							dica+=1
						if tabuleiro[linha-1][item+1] == mina:
							dica+=1
						if tabuleiro[linha][item+1] == mina:
							dica+=1
						if tabuleiro[linha+1][item+1] == mina:
							dica+=1
						if tabuleiro[linha+1][item] == mina:
							dica+=1

					elif linha > 0 and item == len(tabuleiro)-1: # TODO: Verificar se não ocorrerá bug devido o tamanho do array
						if tabuleiro[linha-1][item] == mina:
							dica+=1
						if tabuleiro[linha-1][item-1] == mina:
							dica+=1
						if tabuleiro[linha][item-1] == mina:
							dica+=1
						if tabuleiro[linha+1][item-1] == mina:
							dica+=1
						if tabuleiro[linha+1][item] == mina:
							dica+=1

					elif linha == len(tabuleiro)-1 and item > 0: # TODO: Verificar se não ocorrerá bug devido o tamanho do array
						if tabuleiro[linha][item-1] == mina:
							dica+=1
						if tabuleiro[linha-1][item-1] == mina:
							dica+=1
						if tabuleiro[linha-1][item] == mina:
							dica+=1
						if tabuleiro[linha-1][item+1] == mina:
							dica+=1
						if tabuleiro[linha][item+1] == mina:
							dica+=1


					else:
						if tabuleiro[linha-1][item-1] == mina:
							dica+=1
						if tabuleiro[linha-1][item] == mina:
							dica+=1
						if tabuleiro[linha-1][item+1] == mina:
							dica+=1

						if tabuleiro[linha][item-1] == mina:
							dica+=1
						if tabuleiro[linha][item+1] == mina:
							dica+=1

						if tabuleiro[linha+1][item-1] == mina:
							dica+=1
						if tabuleiro[linha+1][item] == mina:
							dica+=1
						if tabuleiro[linha+1][item+1] == mina:
							dica+=1

					if dica:
						tabuleiro[linha][item] = str(dica)
			

			except IndexError:
				pass
	return tabuleiro


def imprime_tabuleiro(tabuleiro):
	for item in tabuleiro:
		print(" ".join(item))
	input()
	os.system('clear')

mina = '\033[1;31m■\033[0;0m'

while True:
	campo = gera_tabuleiro()
	campo = popula_tabuleiro(campo)
	imprime_tabuleiro(campo)
