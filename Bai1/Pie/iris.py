import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/iris.data", header=None)
ax = plt.subplots(1, 1, figsize=(10, 8))
data[data.columns[4]].value_counts().sort_index().plot.pie(autopct='%1.1f%%')
plt.title("Tỉ lệ % các loài hoa")
plt.ylabel("")
plt.show()
