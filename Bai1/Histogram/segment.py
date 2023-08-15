import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/segment.data", sep=" ", header=None)
plt.figure(figsize=(10, 7))
# print(data)

# Class 0
# x = data[0]
# plt.hist(x)  # bins=20
# plt.title("0")
# plt.xlabel("Value of 0")


# Class 1
x = data[1]
plt.hist(x)  # bins=20
plt.title("1")
plt.xlabel("Value of 1")

plt.ylabel("Count")
plt.show()
