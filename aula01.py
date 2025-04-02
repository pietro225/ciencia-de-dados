# Faz a importação da biblioteca matplotlib e adiciona um alias (apelido) para um objeto
# Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def exibirGrafico():
    # Definição dos grupos e valores
    grupos = ['A', 'B', 'C']
    valores = [23, 38, 12]

    # Configura um gráfico de barras, onde recebe os grupos, valores
    # E opcionalmente as cores
    plt.bar(grupos, valores, color=['red', 'blue', 'grey'])

    # Define o título do gráfico
    plt.title('Gráfico de Barras Simples')

    # Define o título do eixo X
    plt.xlabel('Grupos')

    # Define o título do eixo Y
    plt.ylabel('Valores')

    # Cria o gráfico
    plt.show()

    # Salva dentro do arquivo de imagem
    plt.savefig('chart.png')

#titulo eixo x