# importing autompg dataset from bokeh.sampledata.autompg
from bokeh.sampledata.autompg import autompg

# importing columndatasource package from
# bokeh.models module
from bokeh.models import ColumnDataSource

# importing figure and show from
# bokeh.plotting module to plot the figure
from bokeh.plotting import figure, show

# provides data to the glyphs of the plot
source = ColumnDataSource(autompg)

# Creating an empty figure
p = figure(plot_height=600, plot_width=600)

# Creating circular glyphs with points plotted from
# columns taken from auto-mpg dataset
p.circle(x='hp', y='mpg', size=20,
         alpha=0.6, source=autompg,
         legend_label="Blue")

# Creating circular glyphs with points plotted from
# columns taken from auto-mpg dataset  with different colors
p.circle(x='hp', y='displ', size=20,
         alpha=0.6, color="green", source=autompg,
         legend_label="Green")

# Adjusting the label height using legend
p.legend.label_height = 50

# Adjusting the label_width using legend
p.legend.label_width = 50

# Adjusting the glyph width using legend
p.legend.glyph_width = 90

# Adjusting the glyph height using legend
p.legend.glyph_height = 90

# Showing the above plot
show(p)