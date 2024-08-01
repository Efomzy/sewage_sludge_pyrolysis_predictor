import streamlit as st
import pickle
import numpy as np
from xgboost import XGBRegressor
XGB1 = pickle.load(open('XGB1.pkl', 'rb'))
XGB2 = pickle.load(open('XGB2.pkl', 'rb'))
XGB3 = pickle.load(open('XGB3.pkl', 'rb'))
XGB6 = pickle.load(open('XGB6.pkl', 'rb'))


st.write('# Sewage Sludge Pyrolysis Predictor')
st.subheader('(Ultimate and Proximate analysis should be in dry basis)')

col1, col2, col3, col4 = st.columns(4)

with col1:
  C = st.number_input("Carbon content (%)", 0.00,50.00)

with col2:
  N = st.number_input("Nitrogen content (%)", 0.00,10.00)
  
with col3:
  VM = st.number_input("Volatile Matter (%)", 0.00,75.00)
  
with col4:
  HR = st.number_input("Heating Rate (°C/min)", 5.00,122.00)
  
  
with col1:
  H = st.number_input("Hydrogen content (%)", 0.00,15.00)

with col2:
  S = st.number_input("Sulfur content (%)", 0.00,20.00)
  
with col3:
  FC = st.number_input("Fixed Carbon (%)", 0.00,25.00)

with col4:
  RT = st.number_input("Residence Time (min)", 10.00,120.00)
  
  
with col1:
  O = st.number_input("Oxygen content (%)", 0.00,40.00)

with col2:
  A = st.number_input("Ash content (%)", 0.00,75.00)
  
with col3:
  MC = st.number_input("Moisture Content (%)", 0.00,81.00)
  
with col4:
  T = st.number_input("Temperature (°C)", 350,1000)
 

if C+H+O+N+S+A >= 85 and C+H+O+N+S+A <= 115 and A+VM+FC >= 85 and A+VM+FC <= 115:

  Biooil1 = XGB1.predict([[C, H, O, N, S, A, VM, FC, MC, HR, RT, T]])
  Syngas2 = XGB2.predict([[C, H, O, N, S, A, VM, FC, MC, HR, RT, T]])
  Biochar3 = XGB3.predict([[C, H, O, N, S, A, VM, FC, MC, HR, RT, T]])
  CO26 = XGB6.predict([[C, H, O, N, S, A, VM, FC, MC, HR, RT, T]])
  Biooil = round(Biooil1[0], 2)
  Syngas = round(Syngas2[0], 2)
  Biochar = round(Biochar3[0], 2)
  CO2 = round(CO26[0], 2)

else:
  
  Biooil = 'error in input data'
  Syngas = 'error in input data'
  Biochar = 'error in input data'
  CO2 = 'error in input data'

if st.button('Click here to predict sludge pyrolysis products'):
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.write('Biooil (wt.%)', Biooil)
    
  with col2:
    st.write('Biochar (wt.%)', Biochar)
    
  with col3:
    st.write('Syngas (wt.%)', Syngas)
    
  with col4:
     st.write('CO2 (vol.%)', CO2)
    
