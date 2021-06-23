import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines() 
#O readlines()método retorna uma lista contendo cada linha do arquivo como um item de lista
x = []
y = []

for c in range(0, len(dados)):
    if c != 0:
        linhas = dados[c].split(";")
        x.append(int(linhas[0]))
        y.append(int(linhas[1]))

plt.title("Crescimento da População Brasileira")
plt.xlabel("Anos")
plt.ylabel("População x 100'000'000")
plt.bar(x, y, color="#C0C0C0")
plt.plot(x, y, color="k", linestyle="-.")

plt.show()
