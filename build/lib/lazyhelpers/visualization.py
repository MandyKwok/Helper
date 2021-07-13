import numpy as np

import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib import rcParams

def plot_bar_chart(categories, values, title = '', xlabel = '', ylabel = ''):
    colors = cm.rainbow(np.linspace(0, 1, 10))
    rcParams['figure.figsize'] = 20, 10

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.barh(categories, values, color = colors)