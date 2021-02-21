# -*- coding: utf-8 -*-

# Import Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


from layout import layout
import callbacks







if __name__ == '__main__':
    app.run_server(debug=True)

# Initialize dash object
external_stylesheets = [dbc.themes.BOOTSTRAP]

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=layout)
])

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
server = app.server




# Get Global data

# Set configurations

# App layout


