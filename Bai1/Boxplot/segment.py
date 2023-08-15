import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/segment.data", sep=" ", header=None)
plt.figure(figsize=(10, 7))
print(data.columns)

new_data = data[data.columns]
new_data.boxplot()
plt.show()
