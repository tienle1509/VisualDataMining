import plotly.express as px
import pandas as pd

df = pd.read_csv("../data/iris.data", sep=',', names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])
print(df)
fig = px.scatter_matrix(df,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species",
    title="Scatter matrix of iris data set")
fig.show()
