import numpy as np
import pandas as pd
from vega_datasets import data as vds
from bokeh.io import output_file, show, reset_output
from bokeh.plotting import figure
from bokeh.models import HoverTool

x = np.arange(10)
y = np.random.rand(10)
output_file('teste.html')
linha = figure(plot_width=500, plot_height=325, title='Title plot', x_axis_label='x', y_axis_label='y')
linha.line(x,y)
show(linha)