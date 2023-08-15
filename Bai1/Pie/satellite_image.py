import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/sat.trn", sep=" ", header=None)
ax = plt.subplots(1, 1, figsize=(10, 8))
# print(data)
# print(data.columns)
data[data.columns[36]].value_counts().sort_index().plot.pie(autopct='%1.1f%%')
plt.title("Biểu đồ pie của tập satellite image")
plt.ylabel("")
plt.show()
