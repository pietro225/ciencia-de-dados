import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Conjunto de dados exemplo
dados = [120, 150, 170, 160, 180, 200, 210, 190, 220, 250, 240, 230]

# Calcular quartis
quartis = np.percentile(dados, [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')

# Visualização por BoxPlot
plt.boxplot(dados, vert=False)
plt.title('Tabelas de vendas')
plt.xlabel('numero de vendas')
plt.show()
plt.savefig('chart2.png')
