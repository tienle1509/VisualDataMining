import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/iris.data", sep=",", names=['sepal length', 'sepal width', 'petal length', 'petal width', 'species'])
plt.figure(figsize=(10, 7))

# sepal length
# x = data["sepal length"]
# plt.hist(x)  # bins=20
# plt.title("Sepal Length")
# plt.xlabel("Sepal_Length")

# sepal width
# x = data["sepal width"]
# plt.hist(x)  # bins=20
# plt.title("Sepal Width")
# plt.xlabel("Sepal_Width")

# petal length
# x = data["petal length"]
# plt.hist(x)  # bins=20
# plt.title("Petal Length")
# plt.xlabel("Petal_Length")

# petal width
x = data["petal width"]
plt.hist(x)  # bins=20
plt.title("Petal Width")
plt.xlabel("Petal_Width")

plt.ylabel("Count")
plt.show()
