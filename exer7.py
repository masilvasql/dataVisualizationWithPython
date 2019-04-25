# Crescimento da populaçao brasileira de 1980 - 2016
# dados retirados do DataSus
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = [] #ano
y = [] #poulação

#range = cria uma lista de 0 ao tamanho final
#len = pega o tamanho
for i in range(len (dados)):
	if(i != 0):
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))

plt.bar(x,y, color='#3498db')
plt.plot(x,y, color='#2c3e50', linestyle= '--')
plt.title('Crescimento da População Brasileira de 1980 - 2016')
plt.xlabel("Ano")
plt.ylabel("População * 100.000.000")
plt.savefig("grafPop.png")
plt.show()
