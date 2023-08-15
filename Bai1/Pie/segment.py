import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/segment.data", sep=" ", header=None)
ax = plt.subplots(1, 1, figsize=(10, 8))
# print(data)
data[data.columns[19]].value_counts().sort_index().plot.pie(autopct='%1.1f%%')
plt.title("Biểu đồ pie của tập segment")
plt.ylabel("")
plt.show()
