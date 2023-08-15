import plotly.express as px
import pandas as pd

dimension = []
names = []
for i in range(0, 19):
    dimension.append('A' + str(i))
    names.append('A' + str(i))

names.append('Class')

df = pd.read_csv("../data/segment.data", sep=' ', names=names)
print(df)
fig = px.scatter_matrix(df, dimensions=dimension, color="Class", title="Scatter matrix of segment data set")
fig.show()
