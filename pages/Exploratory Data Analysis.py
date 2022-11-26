#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:55:37 2022

@author: olgavyrvich
"""


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
# Exploratory Data Analysis
### Barplots of the dataset features
""")
st.write('---')

df = pd.read_csv('/Users/olgavyrvich/DataScience1/loan_data_set.csv')

st.write("""
 Around 80% applicants in the dataset are males.
""")

fig1 = plt.figure(figsize=(8, 4))
df['Gender'].value_counts(normalize=True).plot(kind='bar',title='Gender')
st.pyplot(fig1)

st.write("""
Around 65% of the applicants in the dataset are married.
""")

fig2 = plt.figure(figsize=(8, 4))
df['Married'].value_counts(normalize=True).plot(kind='bar',title='Married')
st.pyplot(fig2)



st.write(""" 
Around 15% applicants in the dataset are self employed.
""")

fig3 = plt.figure(figsize=(8, 4))
df['Self_Employed'].value_counts(normalize=True).plot(kind='bar',title='Self_Employed')
st.pyplot(fig3)


st.write(""" 
Around 85% applicants have a credit history.
""")

fig4 = plt.figure(figsize=(8, 4))
df['Credit_History'].value_counts(normalize=True).plot(kind='bar',title='Credit_History')
st.pyplot(fig4)


st.write(""" 
Most of the applicants don’t have any dependents.
""")

st.write("""
Around 80% of the applicants are graduate.
""")
fig5 = plt.figure(figsize=(8, 4))
df['Education'].value_counts(normalize=True).plot(kind='bar',title='Education')
st.pyplot(fig5)

st.write(""" 
Most of the applicants don’t have any dependents.
""")

fig6 = plt.figure(figsize=(8, 4))
df['Dependents'].value_counts(normalize=True).plot(kind='bar',title='Dependents')
st.pyplot(fig6)

st.write(""" 
Most of the applicants are from Semiurban area,
Around 34% f the applicants are from Urban area,
Around 30% f the applicants are from Rural area.
""")

fig7 = plt.figure(figsize=(8, 4))
df['Property_Area'].value_counts(normalize=True).plot(kind='bar',title='Property_Area')
st.pyplot(fig7)
