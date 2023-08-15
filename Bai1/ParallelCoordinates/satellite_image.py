import matplotlib.pyplot as plt
import pandas as pd
from pandas import plotting

df = pd.read_csv("../data/sat.trn", sep=' ', header=None)
print(df)
plotting.parallel_coordinates(df, df.columns[36], colormap='gist_rainbow')
plt.show()
