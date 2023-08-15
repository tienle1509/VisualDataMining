import matplotlib.pyplot as plt
import pandas as pd
from pandas import plotting

df = pd.read_csv("../data/iris.data", sep=",", names=['sepal length', 'sepal width', 'petal length', 'petal width', 'species'])
plotting.parallel_coordinates(df, 'species',
                              color=('red', 'blue', 'green'),
                              cols=['sepal width', 'sepal length', 'petal width', 'petal length'])
plt.show()
