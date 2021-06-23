import matplotlib.pyplot as plt
x = [1, 2, 4, 5, 6]
y = [1.5, 1, 2, 2, 3]
titulo = "Gráfico com pontos"
eixox = "Eixo X"
eixoy = "Eixo Y"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="Meus pontos", color="k")
plt.plot(x, y, color="g", linestyle="-.")
plt.legend()
#plt.show()
plt.savefig("figura_teste_01.pdf")
