from collections import Counter
from time import time
import csv

import matplotlib.pyplot as plt


def csv_reader(file_obj):
    """
    Read a csv file
    :return: list 404 pages, count of pages
    """
    reader = csv.reader(file_obj)
    error = list()
    for row in reader:
        error.append(row[1])

    cnt = Counter(error)
    types_er = []
    count_er = []
    for k, v in cnt.items():
        types_er.append(k + ' ({})'.format(v))
        count_er.append(v)
    return types_er, count_er


def plot(x, y):
    fig, ax = plt.subplots()

    ax.bar(x[1:], y[1:])
    ax.set_title(x[0])
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure

    plt.show()
    # plt.savefig('{}.png'.format(str(time())))


if __name__ == '__main__':
    csv_path = '../file_input/https_tdlider-spb.ru_new24.12-03.02.csv'
    with open(csv_path, "r") as f_obj:
        x, y = csv_reader(f_obj)

    plot(x, y)
