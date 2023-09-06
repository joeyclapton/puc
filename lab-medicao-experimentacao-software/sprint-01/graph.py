import matplotlib.pyplot as plt
import numpy as np

def gen_box_plot(data, title, label):
    median = np.median(data)

    plt.boxplot(data, vert=False, whis=[30, 85])
    plt.title(title)
    plt.xlabel(label)

    plt.scatter([median], [1], color='blue', marker='o', label='Mediana')
    plt.text(median, 1, f'Mediana: {median}', color='yellow',
             verticalalignment='bottom', horizontalalignment='left')

    plt.yticks([])
    plt.grid(True)
    plt.legend()
    plt.show()