from typing import Container
import dash
import plotly.express as px
import pandas as pd
import pickle

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.tools as tls
import plotly.graph_objs
from matplotlib import pyplot as plt
import seaborn as sns
from plotly.tools import mpl_to_plotly
import os
from app import app
os.getcwd()

# importing data set
file_name20 = './client_app/Invistico_Airline_initial.sav'
Airline = pickle.load(open(file_name20, 'rb'))
Airline2 = pickle.load(open(file_name20, 'rb'))



# data set preprocessing


Airline_sat = Airline



Airline.iloc[:,5] = Airline.iloc[:,5].replace(1,'business')
Airline.iloc[:,5] = Airline.iloc[:,5].replace(2,'eco')
Airline.iloc[:,5] = Airline.iloc[:,5].replace(3,'eco_plus')

Airline.iloc[:,0] = Airline.iloc[:,0].replace(0,'dissatisfied')
Airline.iloc[:,0] = Airline.iloc[:,0].replace(1,'satisfied')

Airline.iloc[:,1] = Airline.iloc[:,1].replace(1,'male')
Airline.iloc[:,1] = Airline.iloc[:,1].replace(2,'female')

Airline.iloc[:,2] = Airline.iloc[:,2].replace(0,'loyel customer')
Airline.iloc[:,2] = Airline.iloc[:,2].replace(1,'disloyel customer')

Airline.iloc[:,4] = Airline.iloc[:,4].replace(1,'business travel')
Airline.iloc[:,4] = Airline.iloc[:,4].replace(2,'personal travel')




dff2 = Airline.groupby(['satisfaction','Class',],as_index=False)[['Online boarding']].count()
dff3 = Airline.groupby(['satisfaction','Customer Type','Class',],as_index=False)[['Online boarding']].count()
dff4 = Airline.groupby(['satisfaction','Gender','Class',],as_index=False)[['Online boarding']].count()
dff5 = Airline.groupby(['satisfaction','Type of Travel','Class',],as_index=False)[['Online boarding']].count()
dff6 = Airline.groupby(['Seat comfort'],as_index=False)[['Online boarding']].count()

print(dff6)




# LAYOUT OF THE PAGE (VISUALIZING CLASSIFICATION)
################################################

layout = html.Div([
    dbc.Container([
    
        ## main topic
        dbc.Row([
            dbc.Col(html.H1(children='Airline Passenger Satisfaction Prediction'), className="mb-2")
        ],className = "main-topic"),
        ## main sub topic
        dbc.Row([
            dbc.Col(html.H6(children='Analysis & Passenger Satisfaction Prediction on US Airline'), className="mb-2")
        ],className = "main-topic"),

        dbc.Row([
                dbc.Col(dbc.Card([html.H4(children="Satisfaction count of each class by Age",className="text-center text-dark bg-white text-nav")
                                  
                                            ], body=True, color="light",className = "card-col-main-row")
                        , className="mt-2 mb-1",
                        )
                ], className="main-row"
                ),

        dbc.Row([
            dbc.Col(
            dcc.Dropdown(id='genre-choice',
                         options=[{'label': 'Business', 'value': 1}, {
                             'label': 'Eco', 'value': 2}, {'label': 'Eco Plus', 'value': 3}],
                value='Action'
                         ),
                         className="drop-down"
            )
        ], className="main-row"),

        dbc.Row([

                dbc.Col(dcc.Graph(id='my-graph'))
 
            ],className="f-card"),

        dbc.Row([
                dbc.Col(dbc.Card([html.H4(children="Satisfied/Dissatisfied Count of each class",className="text-center text-dark bg-white text-nav")
                                  
                                            ], body=True, color="light",className = "card-col-main-row")
                        , className="mt-2 mb-1",
                        )
                ], className="main-row"
                ),
                
        dbc.Row([

                dbc.Col(dcc.Graph(id='my-graph-sat')),

 
 
            ],className="f-card"),

        dbc.Row([
                dbc.Col(dbc.Card([html.H4(children="Satisfied/Dissatisfied Count of each class by their passenger type",className="text-center bg-secondary text-dark text-nav")
                                  
                                            ], body=True, color="bg-secondary",className = "card-col-main-row")
                        , className="mt-2 mb-1 main-row-topic",
                        )
                ], className="main-row"
                ),

        dbc.Row([

                dbc.Col(dcc.Graph(id='my-graph-sat-custype')),

 
 
            ],className="f-card"),
        dbc.Row([
                dbc.Col(dbc.Card([html.H4(children="Satisfied/Dissatisfied Count of each class by their gender",className="text-center text-dark bg-white text-nav")
                                  
                                            ], body=True, color="light",className = "card-col-main-row")
                        , className="mt-2 mb-1",
                        )
                ], className="main-row"
                ),

        dbc.Row([

                dbc.Col(dcc.Graph(id='my-graph-sat-gender')),

 
 
            ],className="f-card"),

        dbc.Row([
                dbc.Col(dbc.Card([html.H4(children="Satisfied/Dissatisfied Count of each class by their type of travel",className="text-center text-dark bg-white text-nav")
                                  
                                            ], body=True, color="light",className = "card-col-main-row")
                        , className="mt-2 mb-1",
                        )
                ], className="main-row"
                ),

        dbc.Row([

                dbc.Col(dcc.Graph(id='my-graph-sat-tot')),

 
 
            ],className="f-card"),


    
],className="container-out")

])


@app.callback([
    Output('my-graph','figure'),
    Output('my-graph-sat','figure'),
    Output('my-graph-sat-custype','figure'),
    Output('my-graph-sat-gender','figure'),
    Output('my-graph-sat-tot','figure')],
    [Input('genre-choice','value')]
)
def interactive_graphs(value_genre):
    print(value_genre)
    
    figx = px.histogram(data_frame=Airline2[Airline2.Class == value_genre], x='Age', y="satisfaction" , color="Age")
    figx.layout.template = 'plotly_dark'

    fig2 = px.bar(data_frame=dff2, x="Class", y="Online boarding",color="Class", facet_col="satisfaction",
                    labels={ # replaces default labels by column name
                "Class": "Class",  "Online boarding": "Number of Passengers"
            }
                    )
    fig2.layout.template = 'plotly_dark'


    fig3 = px.bar(data_frame=dff3, x="Customer Type", y="Online boarding",color="satisfaction", barmode="group",facet_col="Class",
                    labels={ # replaces default labels by column name
                "Customer Type": "Customer Type",  "Online boarding": "Number of Passengers"
            }
                    )
    fig3.layout.template = 'plotly_dark'

    fig4 = px.bar(data_frame=dff4, x="Gender", y="Online boarding",color="satisfaction", barmode="group",facet_col="Class",
                    labels={ # replaces default labels by column name
                "Gender": "Gender",  "Online boarding": "Number of Passengers"
            }
                    )

    fig4.layout.template = 'plotly_dark'


    fig5 = px.bar(data_frame=dff5, x="Type of Travel", y="Online boarding",color="satisfaction", barmode="group",facet_col="Class",
                    labels={ # replaces default labels by column name
                "Type of Travel": "Type of Travel",  "Online boarding": "Number of Passengers"
            }
                    )
    fig5.layout.template = 'plotly_dark'



    return figx,fig2, fig3,fig4,fig5




