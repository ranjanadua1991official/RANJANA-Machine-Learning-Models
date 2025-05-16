# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 09:04:56 2025

@author: dell
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/dell/OneDrive/Desktop/SQL/trained_model.sav','rb'))

#Creating a function for diabetic prediction

def diabetes_prediction(input_data):
    
    
    input_data=np.asarray(input_data)
    input_data_reshape=input_data.reshape(1,-1)
    predictor=loaded_model.predict(input_data_reshape)
    print(predictor)
    if (predictor==1):
      return 'The person is diabetic'
    else:
      return 'The person is non-diabetic'
      
def main():
    #Giving a title
     
    st.title('Diabetic Prediction app')
    
    #Getting the input data from user
    
    Pregnancies=st.text_input('No. of Pregnancies')
    Glucose=st.text_input('No. of Glucose')
    BloodPressure =st.text_input('No. of Blood Pressure')
    SkinThickness=st.text_input('No. of SkinThickness')
    Insulin=st.text_input('No. of Insulin')
    BMI=st.text_input('No. of BMI')
    DiabetesPedigreeFunction=st.text_input('No. of DiabetesPedigreeFunction')
    Age=st.text_input('No. of Age')
  
    #Code for prediction
    
    diagonsis=''
    
    #Creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
       diagonsis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    st.success(diagonsis)
        
if __name__ == '__main__':
    main()