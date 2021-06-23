import matplotlib.pyplot as plt
from random import randint
v = []
for c in range(0, 50):
    n = randint(0, 32)
    v.append(n)
plt.boxplot(v)
plt.title("Boxplot")
plt.show()
