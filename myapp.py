# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:18:33 2021

@author: eagle
"""

import plotly.express as px
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle


def L3predict(loginid,decision,time):
    l3_model=pickle.load(open("l3_mlr.pkl","rb"))
    prediction=l3_model.predict([[decision,loginid,time]])
    if prediction==0:
        pred="Bad"
    elif prediction==1:
        pred="Excellent"
    elif prediction==2:
        pred="Good"
    else:
        pred="Normal"
    return pred
def L2predict(loginid,decision,time):
    l2_model=pickle.load(open("l2_mlr.pkl","rb"))
    prediction=l2_model.predict([[decision,loginid,time]])
    if prediction==0:
        pred="Bad"
    elif prediction==1:
        pred="Excellent"
    elif prediction==2:
        pred="Good"
    else:
        pred="Normal"
    return pred


def main():
    l2=pd.read_csv("C://Data//l2_operator.csv")
    l3=pd.read_csv("C://Data//L3_operator.csv")
    l2_loginId=l2["L2LoginID"].unique().tolist()
    l3_loginId=l3["L3LoginID"].unique().tolist()
    
    
    
    
    st.title("Airport Security Analytics")
    operator=st.sidebar.radio("Select Operator",("L2 operator","L3 operator") )
    
    if operator=="L2 operator":
        st.write("L2 operator performance")
        L2LoginId=st.selectbox("L2 Login ID", l2_loginId)
        
        df=l2.loc[l2["L2LoginID"]==L2LoginId,]
        
        fiq=px.scatter(df,x="L2Decision",y="timesecs1",size="timesecs1",color="L2Decision")
        fiq.update_layout(width=800)
        st.write(fiq)
        
        L2Decision_selection=st.selectbox("L2 Decision", l2["L2Decision"].unique().tolist())
        if L2Decision_selection=="Time out":
            decision=2
        elif L2Decision_selection=="Accept":
            decision=0
        else:
            decision=1
        L2Time=st.number_input("Time in secs")
        if st.button("Predict"):
            result=L2predict(L2LoginId,decision,L2Time)
            st.write("Performance of operator is: "+result)
            
            
        
    else:
        st.write("L3 Operator performance")
        L3LoginID=st.selectbox("L3 Login IDs", l3_loginId)
        
        df=l3.loc[l3["L3LoginID"]==L3LoginID,["timesecs2","L3Decision"]]
        
        fiq=px.scatter(df,x="L3Decision",y="timesecs2",size="timesecs2",color="L3Decision")
        fiq.update_layout(width=800)
        st.write(fiq)
        L3Decision_select=st.selectbox("L3 Decision",l3["L3Decision"].unique().tolist())
        if L3Decision_select=="Time out":
            decision=2
        elif L3Decision_select=="Reject":
            decision=1
        else:
            decision=0
        L3Time=st.number_input("Time in secs")
        L3_predict=st.button("Predict")
        if L3_predict:
            result=L3predict(L3LoginID,decision,L3Time)
            st.write("Performance of operator is:"+result)
        
    
if __name__=='__main__':
    main()


    
    
