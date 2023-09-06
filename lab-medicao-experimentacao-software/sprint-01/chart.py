from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def box_plot(data, title, label):
    median = np.median(data)

    plt.boxplot(data, vert=False, whis=[30, 85])
    plt.title(title)
    plt.xlabel(label)

    plt.scatter([median], [1], color='blue', marker='o', label='Mediana')
    plt.text(median, 1, f'Mediana: {median}', color='red',
             verticalalignment='bottom', horizontalalignment='left')

    plt.yticks([])
    plt.grid(True)
    plt.legend()
    plt.show()

def bar(data, title, label):
    # Remova os valores None do array
    filtered_data = [item for item in data if item is not None]

    # Use Counter para contar as ocorrências de cada elemento
    counter = Counter(filtered_data)

    # Separe as chaves (linguagens) e os valores (contagens) do contador
    languages, counts = zip(*counter.items())

    # Crie um gráfico de barras
    plt.bar(languages, counts)

    # Configure o título e os rótulos dos eixos
    plt.title(title)
    plt.xlabel(label)
    plt.ylabel('Contagem')

    # Rotacione os rótulos do eixo x para melhor legibilidade
    plt.xticks(rotation=45)

    # Exiba o gráfico
    plt.tight_layout()
    plt.show()