import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D # unnecessary for version 3.2.0 or higher
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.stats import norm
from time import perf_counter
from random import randint

ARRAY_LEN = 10 ** 6

def np_arr_perf():
    a1 = np.random.randint(1, 100, size = ARRAY_LEN)
    a2 = np.random.randint(1, 100, size = ARRAY_LEN)
    start = perf_counter()
    np.multiply(a1, a2)
    return perf_counter() - start

def default_arr_perf():
    a1 = [randint(1, 100) for _ in range(ARRAY_LEN)]
    a2 = [randint(1, 100) for _ in range(ARRAY_LEN)]
    start = perf_counter()
    [a1[i] * a2[i] for i in range(ARRAY_LEN)]
    return perf_counter() -  start

def histogram_from_data():
    columns = ['ph']
    df = pd.read_csv('data2.csv', usecols=columns).fillna(0)
    _, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_xlabel('ph')
    ax1.set_ylabel('count')
    ax2.set_xlabel('ph')
    ax2.set_ylabel('count')
    ax1.set_title('default histogram')
    ax2.set_title('normalized histogram')
    ax1.hist(df.ph)
    ax2.hist(df.ph, density=True)
    mean, std = norm.fit(df.ph)
    x = np.linspace(df.ph.min(), df.ph.max())
    ax2.plot(x, norm.pdf(x, mean, std))
    plt.show()

def plot_3d():
    x = np.linspace(-2 * np.pi, 2 * np.pi)
    y = np.sin(x) * np.cos(x)
    z = np.sin(x) * np.cos(x)
    fig = plt.figure()
    ax = fig.add_subplot(projection =  '3d')
    ax.plot(x, y, z)
    plt.show()

def animated_plot():
    def animate(i):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 300)
        y = np.sin(x * i)
        ax.clear()
        return ax.plot(x, y)
    fig, ax = plt.subplots()
    animation = FuncAnimation(fig, animate, frames= np.linspace(-2 * np.pi, 2 * np.pi, 30), interval = 10, repeat = False)
    animation.save('sin_animation.gif', writer=PillowWriter(fps=30))
    

# Задание 1
# print('Default array performance:', default_arr_perf())
# print('Numpy array perfomance:', np_arr_perf())
# Задание 2
# histogram_from_data()
# Задание 3
# plot_3d() 
# Доп. задание
# animated_plot() # gif saved to current directory



