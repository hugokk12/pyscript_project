from cProfile import label
from matplotlib import widgets
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, CheckButtons
import numpy as np 
import pandas as pd
from pyodide.http import open_url


def hello_teste():
    print('hello')
    return

def world_teste():
    print('world')
    return

def graph_teste():
    '''matplotlib.rcParams['font.sans-serif'] = "Oswald"
    matplotlib.rcParams['font.family'] = "Oswald"'''
    url_content = open_url("https://raw.githubusercontent.com/hugokk12/pyscript_project/master/script/data.txt")
    data = pd.read_csv(url_content, sep='\t')
    #print(data)
    ages = data['Age']

    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']
    
    
    fig, ax = plt.subplots(facecolor=('#030202'),figsize=(10, 8))
    ax.plot(ages, py_salaries, label='Python')
    ax.plot(ages, js_salaries, label='JavaScript')

    ax.set_title('Median Salary by Age', fontsize=30, color='#ca982b')
    ax.set_xlabel('Age', color='#ca982b', fontsize=15)
    ax.tick_params(axis='x', colors='#ca982b')
    ax.tick_params(axis='y', colors='#ca982b')
    ax.set_facecolor("grey")
    ax.set_ylabel('Salary', color='#ca982b', fontsize=15) 
    ax.legend(['Python', 'Javascript'], loc='lower right')

    '''with plt.style.context('dark_background'):
        fig, ax = plt.subplots()
        ax.plot(xpoints,ypoints)
    '''
    ax.grid()
    
    return fig


def px_teste():
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop', color='r-o')
    fig.show()

def dados():
    import altair as alt
    from vega_datasets import data

    df = data.movies.url
    pts = alt.selection(type="single", encodings=['x'])

    rect = alt.Chart(df).mark_bar().encode(
        alt.X('IMDB_Rating:Q', bin=True),
        alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
        color=alt.condition(pts, 'Rotten_Tomatoes_Rating:Q', alt.value('lightgray'))
    )

    circ = rect.mark_point().encode(
        alt.ColorValue('lightgray'),
        alt.Size(
            'count()',
            legend=alt.Legend(title='Number of Movies Selected')
        )
    ).transform_filter(
        pts
    )

    text = alt.Chart(df).mark_text().encode(
        y=alt.Y('row_number:O', axis=None),
    ).transform_window(
        row_number='row_number()'
    ).transform_filter(
        pts
    ).transform_window(
        rank='rank(row_number)'
    ).transform_filter(
        alt.datum.rank < 20
    )

    return rect
