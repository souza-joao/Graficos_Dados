import matplotlib.pyplot as plt
x = [1, 2, 4]
y = [2, 4, 10]

# título
plt.title('Meu primeiro gráfico com python.')

# Eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.plot(x, y)
plt.show()
