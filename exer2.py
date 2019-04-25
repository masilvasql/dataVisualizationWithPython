import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,3,7,10,8]

title = 'Gráfico de Barras'
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

plt.title(title)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.bar(x, y)
plt.show()