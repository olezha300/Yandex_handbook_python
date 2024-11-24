import numpy as np


def stairs(array: np):
    matrix = np.zeros((len(array), len(array)), dtype='int')
    for i in range(len(array)):
        matrix[i] = np.roll(array, i)
    return matrix


print(stairs(np.arange(3)))
