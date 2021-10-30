#importing libraries
import os
import numpy as np
import flask
import pickle
import pandas as pd
import seaborn as sns
from flask import Flask, render_template, request
from csv import writer

#creating instance of the class
app=Flask(__name__)


#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


@app.route('/result',methods = ['POST'])


def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        print(to_predict_list)
        
        to_predict_go = [(to_predict_list)]

        
        loaded_model = pickle.load(open("Invistico_Airline_Classification_DecisionTree.pkl","rb"))
        result = loaded_model.predict(to_predict_go)[0]
        
        print(to_predict_go)
        print(result)
        
        to_predict_list.insert(0,result)
        default_value = 1
        to_predict_list.insert(21,default_value)
        to_predict_list.insert(22,default_value)
        print(to_predict_list)
        
        #Map_satisfaction = {1:'satisfied',0:'dissatisfied'}
        #to_predict_list[0] = to_predict_list[0].map(Map_satisfaction)
        
        if to_predict_list[0]==1:
            to_predict_list[0]='satisfied'
        else:
            to_predict_list[0]='dissatisfied'
            
        if to_predict_list[1]==1:
            to_predict_list[1]='Male'
        else:
            to_predict_list[1]='Female'
        
        if to_predict_list[2]==0:
            to_predict_list[2]='Loyal Customer'
        else:
            to_predict_list[2]='disloyal Customer'
            
        if to_predict_list[4]==1:
            to_predict_list[4]='Business travel'
        else:
            to_predict_list[4]='Personal Travel'
            
        if to_predict_list[5]==1:
            to_predict_list[5]='Business'
        elif to_predict_list[5]==2:
            to_predict_list[5]='Eco'
        else:
            to_predict_list[5]='Eco Plus'   

          


    with open('Invistico_Airline.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow(to_predict_list)
        f.close()
        
        print(to_predict_list)
        
        #Get the file
        Airline = pd.read_csv('Invistico_Airline.csv')
        
        #mapping categorical data
        #satisfied and dissatisfide
        Map_satisfaction = {'satisfied':1,'dissatisfied':0}
        Airline['satisfaction'] = Airline['satisfaction'].map(Map_satisfaction)

        #male and female
        Map_Gender = {"Male":1,"Female":2}
        Airline["Gender"]=Airline["Gender"].map(Map_Gender)

        #Loyal and disloyal
        Map_CustomerType = {"Loyal Customer":0,"disloyal Customer":1}
        Airline['Customer Type']= Airline['Customer Type'].map(Map_CustomerType)

        #Business travel and personal travel
        Map_BusinessTravel = {'Business travel':1,"Personal Travel":2}
        Airline['Type of Travel']=Airline['Type of Travel'].map(Map_BusinessTravel)

        #Business and Eco and Eco plus
        Map_class = {'Business':1,'Eco':2,'Eco Plus':3}
        Airline['Class']=Airline['Class'].map(Map_class)
        
        #There is 393 null values in Arrival Delay in Minutes so drop these rows or replace the values
        Airline['Arrival Delay in Minutes']=Airline['Arrival Delay in Minutes'].fillna(Airline['Arrival Delay in Minutes'].mean())

        #save intial data
        pickle.dump(Airline, open("Invistico_Airline_initial.sav","wb"))
        
        if result==1:
           prediction='Satisfied'
        else:
            prediction='Non-Satisfied'

        return render_template("result.html",prediction=prediction)

