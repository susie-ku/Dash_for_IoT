import pandas as pd
import numpy as np
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

from sklearn.datasets import load_iris
iris = load_iris() ## It returns simple dictionary like object with all data.
print("IRIS Dataset Size : ",iris.data.shape, iris.target.shape)
print("IRIS Flower Names : ", iris.target_names)
print("IRIS Flower Feature Names : ", iris.feature_names)

## Creating dataframe of total data
iris_df = pd.DataFrame(data=np.concatenate((iris.data,iris.target.reshape(-1,1)), axis=1), columns=(iris.feature_names+['Flower Type']))
iris_df["Flower Name"] = [iris.target_names[int(i)] for i in iris_df["Flower Type"]]

chart1 = px.scatter(data_frame=iris_df,
           x="sepal length (cm)",
           y="petal length (cm)",
           color="Flower Name",
           size=[1.0]*150,
           title="sepal length (cm) vs petal length (cm)")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

graph1 = dcc.Graph(
        id='graph1',
        figure=chart1,
        style={'width': '180vh'},
        className="six columns"
    )

header = html.H2(children="IRIS")
# row = html.Div(children=graph1)
layout = html.Div(children=[header, graph1], style={"text-align": "center"})

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)

