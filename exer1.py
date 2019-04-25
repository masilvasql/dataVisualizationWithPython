import matplotlib.pyplot as plt

x=[1,2,5]
y=[2,3,7]

plt.title("Meu Primeiro Gráfico com Python")

#eixos

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x, y)
plt.show()