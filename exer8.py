#box plot

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(15):
    num = random.randint(0,25)
    vetor.append(num)

plt.boxplot(vetor)
plt.title('Box Plot')
plt.show()