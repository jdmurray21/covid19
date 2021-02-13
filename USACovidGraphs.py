import numpy as np
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def show_graph(state_one, state_two):
    states = {"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado",
              "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
              "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
              "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota",
              "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
              "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina",
              "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania",
              "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas",
              "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
              "WI": "Wisconsin", "WY": "Wyoming", 'DC' : 'District of Columbia'}

    usadata = pd.read_csv('USACovidData.csv')
    usadata.drop(['countyFIPS', 'stateFIPS', 'County Name'], axis=1, inplace=True)
    usadata.set_axis(usadata['State'], axis=0, inplace=True)
    usadata.drop('State', axis=1, inplace=True)
    usadata = usadata.groupby(['State']).sum().T
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=usadata.index, y=usadata[state_one], name = states[state_one]))
    fig.add_trace(go.Scatter(x=usadata.index, y=usadata[state_two], name = states[state_two]))
    fig.update_layout(title='Total Covid Cases by State', xaxis_title='Date', yaxis_title='Cumulative Positive Cases')
    fig.show()
