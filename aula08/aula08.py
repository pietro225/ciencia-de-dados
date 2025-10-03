import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Faz a leitura do arquivo CSV a partir de uma URL ou Arquivo
dados = pd.read_csv('./aula08/desmatamento_prodes.csv')

print(dados)

# Exibindo a matriz de correlação de pearson
# Fornecendo uma pré-análise dos dados para encontrar
# correlações fortes positivas/negativas ou sem correlação
print(dados.corr().round(2))

# Fazendo análise geral em pares
sns.pairplot(dados)
plt.show()
plt.savefig('./aula08/pairplot.png')

# Fazendo análise individual para correlação forte positiva
# x -> Variável dependente (Mato Grosso)
# y -> Variável descritiva (Rondônia)
sns.lmplot(data=dados, x='mato grosso', y='rondonia')
plt.show()

plt.savefig('./aula08/jointplot-positivo.png')

# Leitura: Conforme aumenta o desmatamento no Mato Grosso
# Aumenta o desmatamento em Rondônia, onde a correlação de ambos é 0,93.
plt.savefig('./aula08/lmplot-positivo.png')

# Fazendo análise individual para correlação forte negativa
# x -> Variável dependente (Referência)
# y -> Variável explicativa (Tocantins)
sns.jointplot(data=dados, x="referencia", y="tocantins", kind='reg')

# Leitura: Conforme passam os anos, a área total desmatada
# no Tocantins, diminui, com uma correlação de -0,74.
plt.savefig('./aula08/jointplot-negativo.png')