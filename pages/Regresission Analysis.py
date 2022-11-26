#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:01:32 2022

@author: olgavyrvich
"""


import streamlit as st
import pickle
import pandas as pd
from PIL import Image


st.write("""
# Loan Prediction App
This app predicts approved or not approved house loan!
""")
st.write('---')

model = pickle.load(open('/Users/olgavyrvich/DataScience1/loan4.pkl', 'rb'))


image = Image.open('home-loan2.jpeg')
st.image(image, '')  


st.sidebar.header('Input Parameters')
def user_input_features():
    Gender = st.sidebar.selectbox('Gender: Female 0, Male 1',('1','0'))
    Married = st.sidebar.selectbox('Married: No 0, Yes 1',('1','0'))
    Dependents = st.sidebar.selectbox('Dependents',('0','1','2','3'))
    Education = st.sidebar.selectbox('Education: Graduate 0, Not Graduate 1',('1','0'))
    Self_Employed = st.sidebar.selectbox('Self_Employed: No 0, Yes 1',('1','0'))
    ApplicantIncome = st.sidebar.slider('ApplicantIncome', 150,81000,5403)
    CoapplicantIncome = st.sidebar.slider('CoapplicantIncome', 0,41667,1621)
    LoanAmount = st.sidebar.slider('LoanAmount', 9000,700000,146000) / 1000
    Loan_Amount_Term = st.sidebar.slider('Loan_Amount_Term', 12,480,342)
    Credit_History = st.sidebar.selectbox('Credit_History: No 0, Yes 1',('0', '1'))
    Property_Area = st.sidebar.selectbox('Property_Area: Rural 0, Semiurban 1, Urban 2',('0','1','2'))
    data = {'Gender':Gender,
            'Married': Married,
            'Dependents': Dependents,
            'Education': Education,
            'Self_Employed': Self_Employed,
            'ApplicantIncome': ApplicantIncome,
            'CoapplicantIncome': CoapplicantIncome,
            'LoanAmount': LoanAmount,
            'Loan_Amount_Term':Loan_Amount_Term,
            'Credit_History':Credit_History,
            'Property_Area':Property_Area,
            }
    features = pd.DataFrame(data, index=[0])
    return features



user_data = user_input_features()
st.header('Loan Data')
st.write(user_data)



prediction = model.predict(user_data)
st.subheader('Prediction')
if prediction[0] == 1:
    st.subheader("Approved!")
else:
    st.subheader("Not approved :(")


