# Faz a importação da biblioteca matplotlib e adiciona um alias (apelido) para um objeto
# Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def exibirGrafico():
    # Definição dos grupos e valores
    trabalhos = ['Engenheiro', 'Professor', 'Desenvolvendor','Médico','Designer']
    valores = [8500, 4000, 9000, 12000, 5000]

    # Configura um gráfico de barras, onde recebe os grupos, valores
    # E opcionalmente as cores
    plt.bar(trabalhos, valores, color=['blue', 'brown', 'purple','gold','pink'])

    # Define o título do gráfico
    plt.title('Média Salarial por Profissão (R$)')

    # Define o título do eixo X
    plt.xlabel('trabalhos')

    # Define o título do eixo Y
    plt.ylabel('Valores')

    # Cria o gráfico
    plt.show()

    # Salva dentro do arquivo de imagem
    plt.savefig('chart.png')
   