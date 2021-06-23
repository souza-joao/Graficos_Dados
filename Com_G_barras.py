import matplotlib.pyplot as plt
x1 = [1, 3, 5, 7, 9]
y1 = [2, 4, 10, 6, 14]

x2 = [0, 2, 4, 6, 8] 
y2 = [12, 4, 6, 1, 10]

titulo = "Grafico de Barras."
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")
plt.legend()

plt.show()
