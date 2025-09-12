import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Criação de um dataset fictício
np.random.seed(42)

dados = pd.DataFrame({
    "Orcamento Campanha": np.random.randint(1000, 5000, size=100),
    "Visualizacoes Anuncio": np.random.randint(2000, 200000, size=100),
    "Vendas": np.random.randint(10, 10000, size=100),
    "Cliques": np.random.randint(100, 20000, size=100)
})

# Visualizar a correlação entre cada variável
print(dados.corr().round(4))

# Pairplot: Visualizar todas as relações
sns.pairplot(dados)
plt.show()
plt.savefig('pairplot7.png')

# Jointplot: Explorar a relação entre duas variáveis específicas
sns.jointplot(x='Visualizacoes_Anuncio', y='Vendas', data=dados, kind='reg')
plt.show()
plt.savefig('jointplot7.png')

# lmplot: Visualizar a linha de regressão
sns.lmplot(x='Visualizacoes_Anuncio', y='Vendas', data=dados)
plt.show()
plt.savefig('lmplot7.png')
