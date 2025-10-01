import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('./aula08/desmatamento_prodes.csv')

print(dados)

print(dados)

print('+-+' * 50)

print(dados.corr().round(2))