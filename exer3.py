import matplotlib.pyplot as plt

x1 =[1, 3, 5, 7, 9]
y1 =[2, 3,7,10,8]

x2 =[2, 4, 6, 8, 10]
y2 =[4, 1, 5, 4, 12]

title = 'Gráfico de Barras'
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

plt.title(title)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.bar(x1, y1, label = 'Grupo 1')
plt.bar(x2, y2, label = 'Grupo 2')
plt.legend()
plt.show()