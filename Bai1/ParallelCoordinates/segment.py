import matplotlib.pyplot as plt
import pandas as pd
from pandas import plotting

# -------------------------------------------- Segment --------------------------------------------
df = pd.read_csv("../data/segment.data", sep=" ", header=None)
print(df)
plotting.parallel_coordinates(df, 19, colormap='gist_rainbow')
plt.show()
