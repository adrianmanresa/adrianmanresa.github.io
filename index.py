# index.py

# Import Libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

	
from app import app

from layout import layout
import callbacks



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=layout)
])




if __name__ == '__main__':
    app.run_server(debug=True)