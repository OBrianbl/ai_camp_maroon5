import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Enter functions below

######################################-Box-############################################################
def boxchart(dataframe, y_axis):
    fig=px.box(dataframe,x = 'Sex', y = y_axis)
    return fig

######################################-Heatmap-############################################################

def corr_heatmap(dataframe):
    fig = px.imshow(dataframe.corr(), text_auto=True)
    return fig

###################################-Data-Pre-Processing-####################################################

def remove_rows_with_zeros_from_column(dataframe, column): #filters data
    dataframe = dataframe.drop(dataframe[dataframe[column] == 0].index)
    return dataframe


#################################-Scatter-Plots-###################################################
def plotly_scatter_function(dataframe, x_axis, y_axis, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title):
    fig = px.scatter(dataframe, x = x_axis, y = y_axis, color = color_labels, template = color_scheme, title = plot_title, labels = {
                     x_axis: x_axis_title,
                     y_axis: y_axis_title,
                     color_labels: color_label_title
    })
    return fig


#################################-Swarm-Plots-###################################################
def plotly_strip_function(dataframe, x_axis, y_axis, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title):
    fig = px.strip(dataframe, x= x_axis, y= y_axis, color= color_labels, template= color_scheme, title= plot_title,  labels={
                     x_axis: x_axis_title,
                     y_axis: y_axis_title,
                     color_labels: color_label_title
                 }  )
    return fig #Is this supposed to be here? It's not within the function.
# out of function