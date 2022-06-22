from cProfile import label
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def hello_teste():
    print('hello')
    return

def world_teste():
    print('world')
    return

def graph_teste():
    data = pd.read_csv("C:/Users/hugo-/OneDrive/Área de Trabalho/pyscript_project/script/data.txt", sep='\t')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    fig, ax = plt.subplots()
    ax.plot(ages, py_salaries, label='Python')
    ax.plot(ages, js_salaries, label='JavaScript')

    ax.set_title('Median Salary by Age')
    ax.set_xlabel('Age')
    ax.set_ylabel('Salary') 

    '''with plt.style.context('dark_background'):
        fig, ax = plt.subplots()
        ax.plot(xpoints,ypoints)
    '''
    return fig


def px_teste():
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop', color='r-o')
    fig.show()


graph_teste()