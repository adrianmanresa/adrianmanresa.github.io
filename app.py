# -*- coding: utf-8 -*-

# Import Libraries
import dash
import dash_bootstrap_components as dbc


# Initialize dash object
external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
server = app.server




# Get Global data

# Set configurations

# App layout


