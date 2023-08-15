import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/sat.trn", sep=" ", header=None)
plt.figure(figsize=(10, 7))
print(data)

# Class 0
x = data[0]
plt.hist(x)  # bins=20
plt.title("0")
plt.xlabel("Value of 0")

plt.ylabel("Count")
plt.show()
