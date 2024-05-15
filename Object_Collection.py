import pandas as pd
import numpy as np

class MatrixObj:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.pixel_vals = self.csv_file.to_numpy(dtype=np.uint8)