library(ggplot2)
library(ggmulti)

# names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
# V1, V2, V3, V4, V5

iris_data = read.csv("../data/iris.data", sep=",", header=FALSE)
names(iris_data) <- c("sepal_length", "sepal_width", "petal_length", "petal_width", "species")
# print(iris_data)

ggplot(iris_data) +
  geom_serialaxes_glyph(
    mapping = aes(petal_length, petal_width, colour = species),
    serialaxes.data = iris_data,
    axes.layout = "radial", 
    axes.sequence = colnames(iris_data)[-5],
    show.axes = TRUE
  ) 