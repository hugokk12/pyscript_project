from unicodedata import category
import seaborn as sns
import pandas as pd
import pandas_bokeh as pdb

def load_diamonds():
    pd.set_option('plotting.backend','pandas_bokeh')
    pdb.output_file('bokeh_test.html')
    #pandas_bokeh.output_notebook()
    diamonds = sns.load_dataset('diamonds')
    p = diamonds.plot_bokeh(kind='scatter', x ='carat', y='price', category='cut')
    pdb.show(p)
load_diamonds()

