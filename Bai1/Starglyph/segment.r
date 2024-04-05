segment_data = read.csv("../data/segment.data", sep=" ", header=FALSE)
names(segment_data) <- c("sepal_length", "sepal_width", "petal_length", "petal_width", "species")
# print(segment_data)

ggplot(segment_data) +
  geom_serialaxes_glyph(
    mapping = aes(petal_length, petal_width, colour = species),
    serialaxes.data = iris_data,
    axes.layout = "radial", 
    axes.sequence = colnames(segment_data)[-5],
    show.axes = TRUE
  )