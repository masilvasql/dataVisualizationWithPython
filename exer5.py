import matplotlib.pyplot as plt

x =[1, 3, 5, 7, 9]
y =[2, 3,7,10,8]


title = 'Scatter Plot: Gráfico de dispersão'
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

plt.title(title)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.scatter(x, y, label = 'Dados', color="g", marker='.', s=100)
plt.plot(x,y, color ='k' ,linestyle= ':')
plt.legend()

plt.show()