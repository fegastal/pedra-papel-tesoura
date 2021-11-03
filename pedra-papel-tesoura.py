print("Insira pedra, papel ou tesoura")
jogador1 = (input())
print("Insira pedra, papel ou tesoura")
jogador2 = (input())
if ((jogador1 == "pedra") and (jogador2 == "tesoura")) or ((jogador1 == "papel") and (jogador2 == "pedra")) or ((jogador1 == "tesoura") and (jogador2 == "papel")):
	print("O jogador 1 ganhou")
	if ((jogador2 == "pedra") and (jogador1 == "tesoura") or (jogador2 == "papel") and (jogador1 == "pedra") or (jogador2 == "tesoura") and (jogador1 == "papel")):
		print("O jogador 2 ganhou")
else:
	print("Os dois jogadores empataram")