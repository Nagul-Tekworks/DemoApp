import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
st.title("Insurance Premium Prediction App")
file=st.file_uploader("Upload your file", type=['CSV'])
def plot(data):
    sns.regplot(x="Age",y="Annual_Premium_Thousands",data=data)
    st.pyplot()



if file:
    data=pd.read_csv(file)
    st.dataframe(data)
    plot(data)
    x=data[['Age']]
    y=data['Annual_Premium_Thousands']
    model=linear_model.LinearRegression()
    model.fit(x,y)

    n=st.number_input("Enter age to predict Annual Premium amount: ")
    result=model.predict([[n]])
    st.write(result)