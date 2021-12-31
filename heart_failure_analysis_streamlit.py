# Project Title: Heart Failure Data Analysis
# Authors: Brandon OBriant, Izabella Doser, Artin Ghafooripour, Konstantinos Paparrizos, Kalven Navarrete, Aviv Michael, Ryan Heiling
# Date: 12/30/2021
# Problem Statement: What are the effects and causes of heart failure and how do they correlate with each other?
# Project Description: In order to find relationships between possible effects and causes of heart failure multiple charts and graphs were made to visualize any possible relationships.
# Data Description: Data from the medical archive at the University of California Irvine

# import data with Python Pandas, by import the module first
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from heart_failure_analysis_functions import *

###########################################
########  Imported Functions To Use #######
###########################################


# remove_rows_with_zeros_from_column(dataframe, column)

# corr_heatmap(dataframe)

# boxchart(dataframe, y_axis)

# plotly_strip_function(dataframe, x_axis, y_axis, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title)

# plotly_scatter_function(dataframe, x_axis, y_axis, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title)


#####################################
########    Import Data    ##########
#####################################

heart_failure_rawdata_df = pd.read_csv("./data/heart.csv")
heart_failure_df = heart_failure_rawdata_df.copy()


#####################################
########    Clean Data    ##########
#####################################

# remove rows with zero for Cholesterol
heart_failure_df = remove_rows_with_zeros_from_column(heart_failure_df, 'Cholesterol')


###############################################################
########    Streamlit Top Page Introduction          ##########
###############################################################
st.title('Heart Failure Data Analysis')
with st.expander("Project Details"):
    st.markdown('- **Team**: Maroon 5')
    #st.pyplot(heatmap(heart_failure_df))
    st.markdown('- **Authors**: Brandon OBriant, Izabella Doser, Artin Ghafooripour, Konstantinos Paparrizos, Kalven Navarrete, Aviv Michael, Ryan Heiling')
    st.markdown('- **Date**: 12/30/2021')
    st.markdown(' - **Problem Statement**: What are the effects and causes of heart failure and how do they correlate with each other?')
    st.markdown('- **Project Description**: In order to find relationships between possible effects and causes of heart failure multiple charts and graphs were made to visualize any possible relationships.')
    st.markdown('- **Data Description**: Data from the medical archive at the University of California Irvine')


########################################
########    Data Description  ##########
########################################

st.header('Data Description')
st.write('The data is sourced from the medical records of the University of California Irvine and contains 12 different recorded values per patient. These values include age(years), sex(male/female), chest pain type(TA, ATA, NAP, ASY), resting blood pressure(mm Hg), cholesterol(mm dl), fasting blood sugar(if FastingBS>120 mg/dl, else 0), resting ECG(Normal, ST, LVH), max heart rate(BMP), exercise-induced angina(yes/no), oldpeak(value measuring depression), slope of the peak exercise ST segment(up, down, flat), and if they have heart disease (true/false).')
with st.expander("Source"):
    st.markdown('The data above was sourced from the medical records of the University of California Irvine and features data collected from 5 separate locations')
    st.markdown('- **Cleveland**: 303 observations')
    st.markdown('- **Hungarian**: 294 observations')
    st.markdown('- **Switzerland**: 123 observations')
    st.markdown('- **Long Beach VA**: 200 observations')
    st.markdown('- **Stalog (heart)*: 270 observations')


########################################
########   Data Stats Tables  ##########
########################################

# create dataframe with only heart disease
hf_with_events = heart_failure_df.loc[heart_failure_df.HeartDisease == 1]
hf_with_events_stats = hf_with_events.drop('HeartDisease',axis=1).describe()

# create dataframe with no heart disease
hf_with_no_events = heart_failure_df.loc[heart_failure_df.HeartDisease == 0]
hf_with_no_events_stats = hf_with_no_events.drop('HeartDisease',axis=1).describe()

##########################################################
st.header("Data Tables with Descriptive Statistics")
st.write("The following tables analyze the population in this dataset and how their attributes relate to heart disease. Please use the expanders below to view each of the tables for further analysis.")
st.subheader("Overall Population")
with st.expander("Datatable Stats of with Events"):
    st.table(hf_with_events_stats)
    st.write("This table shows us of 356 patients affected by heart disease.")
with st.expander("Datatable Stats of No Event"):
    st.dataframe(hf_with_no_events_stats)
    st.write("This table shows us......<<ANALYSIS GOES HERE>>")
with st.expander("Datatable Analysis"):
    st.write("When comparing those with and without heart disease, a noticeable increase is seen in those affected in each category. Notably the mean age, Resting blood pressure, Cholesterol, and Fasting blood sugar. A lower max heart rate seen in those with heart disease is very possibly due to each of these factors weakening the heart. It is evident that each of these categories are key factors when predicting a Heart attack.")
##################################################################
st.subheader('Dynamic Chart: Population By Age and Heart Disease or No Heart Disease')

# selection for minimum age for range
min_Range = st.slider("Choose a Minimum Range for Age", min_value=28, max_value=78)
# choose max age for range, the min_range is used as input to restrict age range selection
# i.e. min_value = min_Range result
max_Range = st.slider("Choose a Maximum Range for Age", min_value = min_Range, max_value=78)


# st.expander allows for drop down of table, we are able to use the events dataframe now
with st.expander(f"Table with Events with Age Between {min_Range} yrs and {max_Range} yrs."):
    heart_failure_by_age_with_events_df = hf_with_events[((hf_with_events.Age <= max_Range) & (hf_with_events.Age >= min_Range))]
    st.table(heart_failure_by_age_with_events_df.drop(['Age','HeartDisease'],axis=1).describe())
    st.write("This table allows for filtering of data between user-specified age ranges. This is specifically to view the patients with heart disease")
# This st.expander allows for drop down of table, we are able to use the no_events dataframe now
with st.expander(f"Table with No Events with Age Between {min_Range} yrs and {max_Range} yrs."):
    heart_failure_by_age_with_no_events_df = hf_with_no_events[((hf_with_no_events.Age <= max_Range) & (hf_with_no_events.Age >= min_Range))]
    st.table(heart_failure_by_age_with_no_events_df.drop(['Age','HeartDisease'],axis=1).describe())
    st.write("This table allows for filtering of data between user-specified age ranges. This is specifically to view the patients without heart disease")
with st.expander("Datatable Analysis"):
    st.write("The ability to filter statistics by age is crucial because age is one of the chief variables in determining not only heart disease, but countless other physical illnesses. The deterioration of the body as age goes on leads to many sytems in the body becoming weaker, all eventually steering towards weaker organs and a weaker heart. In our dataset, we can see that mean factors all increase as max age increases, which leads to the obvious conclusion that an older person has an exponentially higher chance for heart disease than a younger person. A Machine Learning model needs to account for age when considering the chance for heart failure. This is not to say that only seniors can recieve heart disease. Outliers include a 31 year old with heart disease and a 76 year old without heart disease. Filtering the data by age range also allows for careful observation on common healthy heart levels for various age categories. The median cholesterol and max heart rate for each age range can vary greatly, allowing for more precise machine learning for our heart failure predictions. Limitations in the table are the exclusions of string categories such as Chest pain type and Sex. Our model only allows for numerical data so the strings could not be applied.")

########################################
########    heatmap.          ##########
########################################
st.subheader('Heatmap Comparison')
# heart_failure_df
st.plotly_chart(corr_heatmap(heart_failure_df))
st.write("The heatmap tells us the relationship between each numerical variable to each other numerical variable. When a value on the heatmap is between 0 to 1, that shows direct proportionality, whereas a value between -1 to 0 shows inverse proportionality. A value of 0 shows a complete lack of a relationship between the 2 variables, while a value of 1 shows a perfectly proportional relationship between the variables. The heatmap seems to suggest a relatively strong correlation between heart disease to maximum heart rate and to old peak (the relation between exercise and ST depressions.) Specifically, the heatmap suggests that patients with heart disease have a lower maximum heart rate and a higher old peak. There also appears to be a negative correlation between age and maximum heart rate, while there is a posiive correlation between age and heart disease, suggesting that older patients may have a lower maximum heart rate, but that older patients also have a higher chance of heart disease. Lastly, there is a positive correlation between heart disease and fasting blood sugar, as well as heart disease and cholesterol. Therefore, this heatmap suggests that higher fasting blood sugar increases risks of heart disease, as does higher levels of cholesterol.")
st.write("")

###########################################
########    streamlit box   ##########
###########################################


st.subheader("Boxchart Representation of Age/Chest Pain to Cholesterol/Resting ECG")
row0_1, row0_2 = st.columns((1,3))
with row0_1:
    y_option = st.radio('Pick one for y-axis', ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak'])
with row0_2:   
    st.plotly_chart(boxchart(heart_failure_df, y_option)) #change y_axis to y_option
    st.write("Our graph shows data gathered by hospital facilities in diffrent regions. Our graph plots all of the usable data to show corralation between Age, Sex, Cholesterol, and RestingBP.We wanted to show the corralation because we want to be able to use this data to predicte heart attacks.Anyone viewing the chart can see that people with high cholesterol and of older age are way more likly to have heart failure then a younger person with significantly lower/lesser amounts of cholesterol. You can see by average where one lies for a liklyhood of heartfaluire based on their on all these factors")
st.write("")
###########################################
########    streamlit scatter    ##########
###########################################

#plotly_scatter_function(dataframe, x_axis, y_axis, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title)
#dataframe: heart_failure_df
st.subheader('Scatter Plots')

x_option = st.selectbox('Pick one for x-axis', ['Age', 'ChestPainType'])
y_option = st.selectbox('Pick one for y-axis', ['Cholesterol', 'RestingECG'])

# 1: if -> Age vs Cholest
# 2: elif -> Age vs RestingECG
# 3: elif -> ChestPain vs Cholest
# 4: elif -> ChestPain vs RestingECG
color_labels='HeartDisease' 
color_scheme = "ggplot2"

if x_option == 'Age' and y_option == 'Cholesterol':
    plot_title= "Age Vs. Cholesterol"
    x_axis_title= 'Age'
    y_axis_title= 'Cholesterol'
    color_label_title= 'Heart Disease (0 is no and 1 is yes)'
    st.plotly_chart(plotly_scatter_function(heart_failure_df, x_option, y_option, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("This scatter plot above illustrates the relationship between a patient's age, cholesterol levels, and whether or not they have heart disease. Patients over the age of 50  often having a higher cholesterol level, being put at risk for developing or having heart disease compared to those who are younger and share similar cholesterol levels. Besides the few outliers, the plot suggests that higher risks of heart disease are connected to cholesterol levels, which tend to rise as we age, seen with the increase of confirmed cases among the older patients. Overall, older patients are more at risk of developing heart diseases than their younger counterparts.")
    st.write("")
elif x_option == 'Age' and y_option == 'RestingECG' :
    plot_title= 'Age and RestingECG'
    x_axis_title= 'Age'
    y_axis_title= 'RestingECG'
    color_label_title= 'Heart Disease (0 is no and 1 is yes)'
    st.plotly_chart(plotly_scatter_function(heart_failure_df, x_option, y_option, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("This scatter plot above illustrates the relationship between a patient's age, RestingECG, and whether or not they have heart disease. Patients with LVH and Normal resting ECGs are less likely to have heart disease, whereas those with ST resting EGC's have a higher chance of developing or having a heart disease. However, age also seems to correlate with the differing ECGs, with patients over their 50s being more susceptible to heart disease and those under 50 having less of a risk. Overall those with LVH and normal resting EGC's are less prone to having heart disease, whereas those with ST have a higher risk. ")
    st.write("")
elif x_option == 'ChestPainType' and y_option == 'Cholesterol':
    plot_title= 'Chest Pain Type in correlation to Cholesterol'
    x_axis_title= 'ChestPainType'
    y_axis_title= 'Cholesterol'
    color_label_title= 'Heart Disease (0 is no and 1 is yes)'
    st.plotly_chart(plotly_scatter_function(heart_failure_df, x_option, y_option, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("This scatter plot above illustrates the relationship between a patient's chest pain type, cholesterol levels, and whether or not they have heart disease. Patients who experience chest pains such as ATA, NAP, and TA are less likely to have some form of heart disease, the plot suggesting that those who do experience it, to be at lower risk. At the same time, those who experience ASY chest pains often have higher cholesterol and face having heart disease or being at risk. Overall those who experience ASY are more likely to have heart disease than those who get chest pains such as ATA, NAP, and TA.")
    st.write("")
elif x_option == 'ChestPainType' and y_option == 'RestingECG' :
    plot_title= 'Chest Pain Type and RestingECG'
    x_axis_title= 'ChestPainType'
    y_axis_title= 'RestingECG'
    color_label_title= 'Heart Disease (0 is no and 1 is yes)'
    st.plotly_chart(plotly_scatter_function(heart_failure_df, x_option, y_option, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("This scatter plot above illustrates the relationship between a patient's Chest Pain Type, RestingECG, and whether or not they have heart disease. Patients who experience chest pains such as ATA, NAP, and TA are less likely to have some form of heart disease, the plot suggesting that those who do experience it are at lower risk. Those with an LVH (resting ECG) and an ASY Chest Pain Type are at a higher risk than those with an average ECG or other chest pain type. Overall those who have LVH and ASY Chest Pain types are more at risk for developing a Heart Disease.")
    st.write("")
    
#elif x_option ==  and y_option == :
    #plot_title= ""
    #x_axis_title= ''
    #y_axis_title= ''
    #color_label_title= 'Heart Disease (0 is no and 1 is yes)'
    #st.plotly_chart(plotly_scatter_function(heart_failure_df, x_option, y_option, color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    #st.write("The Scatter plot tells us")
    #st.write("")



###########################################
########   streamlit swarm       ##########
###########################################

st.subheader('Swarm Plot')
# Chest pain type to Cholesterol levels to heart disease swarm plot
# drop code blow

x_option = st.selectbox('Pick one', ['ChestPainType', 'Sex', 'ST_Slope'])
y_option = st.selectbox('Pick one', ['Cholesterol', 'RestingECG', 'MaxHR', 'Oldpeak', 'Age'])

# 1: if -> Age vs Cholest
# 2: elif -> Age vs RestingECG
# 3: elif -> ChestPain vs Cholest
# 4: elif -> ChestPain vs RestingECG

color_labels='HeartDisease'
color_scheme = "seaborn"
color_label_title= 'Heart Disease (0 is no and 1 is yes)'

if x_option == 'ChestPainType' and y_option == 'Cholesterol':
    plot_title= 'Chest Pain Type, Cholesterol, and Heart Disease'
    x_axis_title= 'Chest Pain Type'
    y_axis_title= 'Cholesterol'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us the relationship between a patient's chest pain type, their cholesterol levels, and whether or not they have heart disease. Patients who experience ATA, TA, and NAP type chest pain seem to more frequently not have heart disease, suggesting that people who experience ATA, TA, and NAP type chest pain are at a lower risk of developing heart disease. Patients who experience ASY type chest pain seem to more frequently have heart disease, suggesting that people who experience ASY type chest pain are at a higher risk of developing heart disease. Except for a few outliers, the different types of chest pain that patients experience does not seem to be connected to increased or decreased cholesterol levels, suggesting that chest pain type and cholesterol levels do not have much of a connection. Patients who have heart disease appear to on average have slightly higher cholesterol levels than patients who do not have heart disease, implying that people who have higher cholesterol levels are at a slightly higher risk of developing heart disease than people who have lower cholesterol levels.")
    st.write("") 
elif x_option == 'ChestPainType' and y_option == 'RestingECG':
    plot_title= 'Chest Pain Type, Resting Electrocardiogram, and Heart Disease'
    x_axis_title= 'Chest Pain Type'
    y_axis_title= 'Resting Electrocardiogram'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us")
    st.write("")
elif x_option == 'ChestPainType' and y_option == 'MaxHR':
    plot_title= 'Chest Pain Type, Maximum Heart Rate, and Heart Disease'
    x_axis_title= 'Chest Pain Type'
    y_axis_title= 'Maximum Heart Rate'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us the relationship between a patient's chest pain type, their maximum heart rate, and whether or not they have heart disease. Patients who experience ATA, TA, and NAP type chest pain seem to more frequently not have heart disease, suggesting that people who experience ATA, TA, and NAP type chest pain are at a lower risk of developing heart disease. Patients who experience ASY type chest pain seem to more frequently have heart disease, suggesting that people who experience ASY type chest pain are at a higher risk of developing heart disease. Patients with ATA, TA, and NAP type chest pain also appear to on average have a higher maximum heart rate than patients experiencing ASY type chest pain. Additionally, patients with heart disease appear to typically have a lower maximum heart rate than patients without heart disease, suggesting that people with a lower maximum heart rate are more at risk of developing heart disease. Overall, both ASY type chest pain and a lower maximum heart rate appear to be risk factors for heart disease.")
    st.write("")
elif x_option == 'ChestPainType' and y_option == 'Oldpeak':
    plot_title= 'Chest Pain Type, Oldpeak, and Heart Disease'
    x_axis_title= 'Chest Pain Type'
    y_axis_title= 'Oldpeak'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us the relationship between a patient's chest pain type, their oldpeak, and whether or not they have heart disease. Patients who experience ATA, TA, and NAP type chest pain seem to more frequently not have heart disease, suggesting that people who experience ATA, TA, and NAP type chest pain are at a lower risk of developing heart disease. Patients who experience ASY type chest pain seem to more frequently have heart disease, suggesting that people who experience ASY type chest pain are at a higher risk of developing heart disease. Patients with ATA, TA, and NAP type chest pain typically appear to have an oldpeak ranging from 0 to 3, while patients experiencing ASY Type Chest pain to on average have an oldpeak ranging from -2 to 6. Additionally, patients with heart disease often appear to have much higher or lower oldpeaks than patients without heart disease, suggesting that people with an abnormally high or low oldpeak are more likely to develop heart disease. Overall, both ASY type chest pain and an abnormally high or low oldpeak appear to be risk factors for heart disease.")
    st.write("")
elif x_option == 'ChestPainType' and y_option == 'Age':
    plot_title= 'Chest Pain Type, Age, and Heart Disease'
    x_axis_title= 'Chest Pain Type'
    y_axis_title= 'Age'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us the relationship between a patient's chest pain type, their age whether or not they have heart disease. Patients who experience ATA, TA, and NAP type chest pain seem to more frequently not have heart disease, suggesting that people who experience ATA, TA, and NAP type chest pain are at a lower risk of developing heart disease. Patients who experience ASY type chest pain seem to more frequently have heart disease, suggesting that people who experience ASY type chest pain are at a higher risk of developing heart disease. Generally, the age of patients does not appear to impact the type of chest pain they experience. However, a significant majority of older patients have heart disease, while only some of the younger patients have heart disease, suggesting that the older someone is, the more likely they are to develop heart disease. Overall, both ASY type chest pain and old age appear to be risk factors for heart disease.")
    st.write("")
elif x_option == 'Sex' and y_option == 'Cholesterol':
    plot_title= 'Sex, Cholesterol, and Heart Disease'
    x_axis_title= 'Sex'
    y_axis_title= 'Cholesterol'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us the relationship between a patient's sex, their cholesterol levels, and whether or not they have heart disease. More than half of the male patients appear to have heart disease, while only a small amount of the female patients have heart disease, suggesting that males are more likely to develop heart disease. Additionally, patients with heart disease appear to on average have slightly higher cholesterol levels than people without heart disease, suggesting that people with higher cholesterol levels are at risk of developing heart disease. Overall, higher cholesterol levels appear to be a risk factor for heart disease, and males also need to be more wary about developing heart disease than females.")
    st.write("")
elif x_option == 'Sex' and y_option == 'RestingECG':
    plot_title= 'Sex, Resting Electrocardiogram, and Heart Disease'
    x_axis_title= 'Sex'
    y_axis_title= 'Resting Electrocardiogram'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us")
    st.write("")
elif x_option == 'Sex' and y_option == 'MaxHR':
    plot_title= 'Sex, Maximum Heart Rate, and Heart Disease'
    x_axis_title= 'Sex'
    y_axis_title= 'MaxHR'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us the relationship between a patient's sex, their maximum heart rate, and whether or not they have heart disease. More than half of the male patients appear to have heart disease, while only a small amount of the female patients have heart disease, suggesting that males are more likely to develop heart disease. Additionally, patients with heart disease on average appear to have a lower maximum heart rate than patients without heart disease, suggesting that people with low maximum heart rates are more at risk of developing heart disease. Overall, a low maximum heart rate appears to be a risk factor for heart disease, and males also need to be more wary about developing heart disease than females.")
    st.write("")
elif x_option == 'Sex' and y_option == 'Oldpeak':
    plot_title= 'Sex, Oldpeak, and Heart Disease'
    x_axis_title= 'Sex'
    y_axis_title= 'Oldpeak'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us the relationship between a patient's sex, their oldpeak, and whether or not they have heart disease. More than half of the male patients appear to have heart disease, while only a small amount of the female patients have heart disease, suggesting that males are more likely to develop heart disease. Male patients also appear to typically have larger or smaller oldpeaks than female patients, with the oldpeaks of male patients ranging from 6 to -2, while the oldpeaks of female patients only really range from 4 to 0. Patients with heart disease often appear to have much higher or lower oldpeaks than patients without heart disease, suggesting that people with an abnormally high or low oldpeak are more likely to develop heart disease. Overall, an abnormally large or small oldpeak appears to be a risk factor for heart disease, and males need to be more wary of developing heart disease than females.")
    st.write("")
elif x_option == 'Sex' and y_option == 'Age':
    plot_title= 'Sex, Age, and Heart Disease'
    x_axis_title= 'Sex'
    y_axis_title= 'Age'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us the relationship between a patient's sex, their age, and whether or not they have heart disease. More than half of the male patients appear to have heart disease, while only a small amount of the female patients have heart disease, suggesting that males are more likely to develop heart disease. Additionally, patients with heart disease on average are older than people without heart disease, suggesting that older people are more at risk of developing heart disease. Overall, older age is a risk factor for heart disease, and males need to be more wary about developing heart disease than females.")
    st.write("")
elif x_option == 'ST_Slope' and y_option == 'Cholesterol':
    plot_title= 'ST Slope, Cholesterol, and Heart Disease'
    x_axis_title= 'ST Slope'
    y_axis_title= 'Cholesterol'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us the relationship between a patient's ST slope, their cholesterol levels, and whether or not they have heart disease.")
    st.write("")
elif x_option == 'ST_Slope' and y_option == 'RestingECG':
    plot_title= 'ST Slope, Resting Electrocardiogram, and Heart Disease'
    x_axis_title= 'ST Slope'
    y_axis_title= 'Resting Electrocardiogram'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us")
    st.write("")
elif x_option == 'ST_Slope' and y_option == 'MaxHR':
    plot_title= 'ST Slope, Maximum Heart Rate, and Heart Disease'
    x_axis_title= 'ST Slope'
    y_axis_title= 'MaxHR'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us")
    st.write("")
elif x_option == 'ST_Slope' and y_option == 'Oldpeak':
    plot_title= 'ST Slope, Oldpeak, and Heart Disease'
    x_axis_title= 'ST Slope'
    y_axis_title= 'Oldpeak'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us")
    st.write("")
elif x_option == 'ST_Slope' and y_option == 'Age':
    plot_title= 'ST Slope, Age, and Heart Disease'
    x_axis_title= 'ST Slope'
    y_axis_title= 'Age'
    st.plotly_chart(plotly_strip_function(heart_failure_df, x_option , y_option , color_labels, color_scheme, plot_title, x_axis_title, y_axis_title, color_label_title))
    st.write("The strip plot tells us")
    st.write("")