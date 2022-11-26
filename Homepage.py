#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:34:02 2022

@author: olgavyrvich
"""
import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="",
)

st.sidebar.success("Select a page above.")


st.write("""
# Loan Prediction App
This website analyzes the loan eligibility process (real time) 
based on customer detail provided while filling online application form.
These details are Gender, Marital Status, Education, Number of Dependents, 
Income, Loan Amount, Credit History and others.

The dataset used for this analysis, downloaded from https://www.kaggle.com/code/viditagarwal112/loan-approval-prediction/data 
""")
st.write('---')


st.write("""
# Exploratory Data Analysis
In this section the data is explored barplots visualization methods. 
""")
st.write('---')


st.write("""
# Regression Analysis
In this section you could input details are Gender, Marital Status, Education,
Number of Dependents, Income, Loan Amount, Credit History and others to find the
prediction approved or not approved loan based on a logistic regression model.
""")
st.write('---')