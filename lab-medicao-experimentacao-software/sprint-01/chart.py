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
    filtered_data = [item for item in data if item is not None]

    counter = Counter(filtered_data)
    languages, counts = zip(*counter.items())
    plt.bar(languages, counts)

    plt.title(title)
    plt.xlabel(label)
    plt.ylabel('Contagem')

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()