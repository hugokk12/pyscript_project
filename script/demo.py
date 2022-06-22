import pyodide
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def on_click(e):
    left_ul = document.getElementById('left')
    left_ul.innerHTML = 'hello World'

def main():
    button = document.getElementById('button')
    button.addEventListener('click', pyodide.create_proxy(on_click))
