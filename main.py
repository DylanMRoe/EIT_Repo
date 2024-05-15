from Region_File import Region
from Object_Collection import MatrixObj
from matplotlib import pyplot as plt
import pandas as pd

if __name__ == "__main__":
    csvFile = pd.read_csv("./test_matrix.csv")
    matrix = MatrixObj(csvFile)

    plt.imshow(matrix.pixel_vals, cmap="gray")
    plt.show()
