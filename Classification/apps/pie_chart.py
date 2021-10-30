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


dff6 = Airline.groupby(['Seat comfort'],as_index=False)[['Online boarding']].count()
dff7 = Airline.groupby(['Inflight wifi service'],as_index=False)[['Online boarding']].count()
dff8 = Airline.groupby(['Inflight entertainment'],as_index=False)[['Online boarding']].count()
dff9 = Airline.groupby(['Online support'],as_index=False)[['Online boarding']].count()
dff10 = Airline.groupby(['Ease of Online booking'],as_index=False)[['Online boarding']].count()
dff11 = Airline.groupby(['Online boarding'],as_index=False)[['Online boarding']].count()
dff12 = Airline.groupby(['Leg room service'],as_index=False)[['Online boarding']].count()
dff13 = Airline.groupby(['Cleanliness'],as_index=False)[['Online boarding']].count()
dff14 = Airline.groupby(['Food and drink'],as_index=False)[['Online boarding']].count()





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

                dbc.Col(dcc.Graph(id='my-graph-sat-Seat-comfort-pie'),width=4),
                dbc.Col(dcc.Graph(id='my-graph-sat-Inflight'),width=4),
                dbc.Col(dcc.Graph(id='my-graph-sat-Inflight-entertainment'),width=4),

 
 
            ],className="f-card"),

        dbc.Row([
                dbc.Col(dbc.Card([html.H4(children="Satisfaction count of each class by Age",className="text-center text-dark bg-white text-nav")
                                  
                                            ], body=True, color="light",className = "card-col-main-row")
                        , className="mt-2 mb-1",
                        )
                ], className="main-row"
                ),




        dbc.Row([

                dbc.Col(dcc.Graph(id='my-graph-sat-Online-support'),width=4),
                dbc.Col(dcc.Graph(id='my-graph-sat-Ease-of-Online-booking'),width=4),
                dbc.Col(dcc.Graph(id='my-graph-sat-Online-boarding'),width=4),

 
 
            ],className="f-card"),

        dbc.Row([
                dbc.Col(dbc.Card([html.H4(children="Satisfaction count of each class by Age",className="text-center text-dark bg-white text-nav")
                                  
                                            ], body=True, color="light",className = "card-col-main-row")
                        , className="mt-2 mb-1",
                        )
                ], className="main-row"
                ),



        dbc.Row([

                dbc.Col(dcc.Graph(id='my-graph-sat-Leg-room-service'),width=4),
                dbc.Col(dcc.Graph(id='my-graph-sat-Cleanliness'),width=4),
                dbc.Col(dcc.Graph(id='my-graph-sat-Food-and-drink'),width=4),

 
 
            ],className="f-card"),




    
],className="container-out")

])

@app.callback([
    Output('my-graph-sat-Seat-comfort-pie','figure'),
    Output('my-graph-sat-Inflight','figure'),
    Output('my-graph-sat-Inflight-entertainment','figure'),
    Output('my-graph-sat-Online-support','figure'),
    Output('my-graph-sat-Ease-of-Online-booking','figure'),
    Output('my-graph-sat-Online-boarding','figure'),
    Output('my-graph-sat-Leg-room-service','figure'),
    Output('my-graph-sat-Cleanliness','figure'),
    Output('my-graph-sat-Food-and-drink','figure')],
    [Input('my-graph-sat-Seat-comfort-pie','hover-data')]
)
def interactive_graphs(value_genre):
    print(value_genre)

    fig6 = px.pie(data_frame=dff6, values='Online boarding', names='Seat comfort',
    labels={ # replaces default labels by column name
                "Online boarding": "Percentage"
            },
            title="Seat Comfort Rate"
    )
    fig6.layout.template = 'plotly_dark'

    fig7 = px.pie(data_frame=dff7, values='Online boarding', names='Inflight wifi service',
    labels={ # replaces default labels by column name
    "Online boarding": "Percentage"
    })
    fig7.layout.template = 'plotly_dark'

    fig8 = px.pie(data_frame=dff8, values='Online boarding', names='Inflight entertainment',
    labels={ # replaces default labels by column name
    "Online boarding": "Percentage"
    })
    fig8.layout.template = 'plotly_dark'

    fig9 = px.pie(data_frame=dff9, values='Online boarding', names='Online support',
    labels={ # replaces default labels by column name
    "Online boarding": "Percentage"
    })
    fig9.layout.template = 'plotly_dark'

    fig10 = px.pie(data_frame=dff10, values='Online boarding', names='Ease of Online booking',
    labels={ # replaces default labels by column name
    "Online boarding": "Percentage"
    })
    fig10.layout.template = 'plotly_dark'

    fig11 = px.pie(data_frame=dff11, values='Online boarding', names='Online boarding',
    labels={ # replaces default labels by column name
    "Online boarding": "Percentage"
    })
    fig11.layout.template = 'plotly_dark'

    fig12 = px.pie(data_frame=dff12, values='Online boarding', names='Leg room service',
    labels={ # replaces default labels by column name
    "Online boarding": "Percentage"
    })
    fig12.layout.template = 'plotly_dark'

    fig13 = px.pie(data_frame=dff13, values='Online boarding', names='Cleanliness',
    labels={ # replaces default labels by column name
    "Online boarding": "Percentage"
    })
    fig13.layout.template = 'plotly_dark'

    fig14 = px.pie(data_frame=dff14, values='Online boarding', names='Food and drink',
    labels={ # replaces default labels by column name
    "Online boarding": "Percentage"
    })
    fig14.layout.template = 'plotly_dark'



    return fig6,fig7,fig8,fig9,fig10,fig11,fig12,fig13,fig14