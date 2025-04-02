import matplotlib.pyplot as plt

#imortar a biblioteca pandas
import pandas as pd 

def exibirGrafico():
    #criar o dataframe
    df = pd.DataFrame({
        "meses": ['jan', 'fev', 'mar', 'abr','mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'],
        "temperaturas": [29, 31, 30, 28, 27, 25, 21, 24, 27, 28, 29, 33]
    })

    # Redimensionando o grafico
    plt.figure(figsize=[10.0, 5.0])

    # Criação do grafico
    plt.plot(df['meses'], df['temperaturas'],color="red")

    # Definição dos titulos
    plt.title("temperatura media ao longo do tempo")
    plt.xlabel("Meses")
    plt.ylabel("temperatura")

    # Exibindo o grafico
    plt.show()
    plt.savefig('chart2.png')

    # Exibe no console dados estatísticos
    print(f'temperaturas: \n{df['temperaturas'].describe()}')
    