from pprint import pprint as print
from random import random 
import matplotlib.pyplot as plt

def show_matrix(matrix):
    plt.figure

if __name__ == "__main__":
    matrix = [[0 for x in range(10)]for _ in range(10)]
    for i in range(10):
        for j in range(10):
            matrix[i][j] = i if random() < 0.5 else 0 
    print(matrix)
    show_matrix(matrix)