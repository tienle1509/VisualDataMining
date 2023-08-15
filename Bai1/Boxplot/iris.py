import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/iris.data", sep=",", names=["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"])
plt.figure(figsize=(10, 7))

new_data = data[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
# print(new_data.head())
new_data.boxplot()
plt.show()
