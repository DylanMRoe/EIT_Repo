import pandas as pd
import numpy as np

class MatrixObj:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.matrix = self.csv_file.to_numpy(dtype=np.uint8)

    def __init__(self, size, fill):
        self.size = size
        self.fill = fill
        self.matrix = self.matrix_gen()


    def matrix_gen(self):
        construct_array = []

        if self.fill:
            array_fill = np.ones(self.size)

        else:
            array_fill = np.zeros(self.size)

        for i in range(self.size):
            construct_array.append(array_fill)

        return np.array(construct_array)
    