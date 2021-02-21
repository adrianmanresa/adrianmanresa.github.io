# layouts.py

# Import Libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


import pandas as pd
import plotly.express as px
from plotly.offline import plot


from app import app
from dash.dependencies import Input, Output
import global_data as gd 

## global variables definition
# v_path_input = 'datos/Input/'

# # Get Global data
# df_kpi = pd.read_csv(v_path_input+'df_kpi.csv')

# df_calendar = pd.read_csv(v_path_input+'df_calendar.csv')

# ## Data transformations
# v_CYear= df_calendar.Year.max()
# v_CYearMonth_max = df_calendar[df_calendar.Year.eq(v_CYear)]['YearMonth'].max()
# v_CYearMonth_min = df_calendar[df_calendar.Year.eq(v_CYear)]['YearMonth'].min()

# v_PYear = v_CYear - 1
# v_PYearMonth_max = df_calendar[df_calendar.Year.eq(v_PYear)]['YearMonth'].max()
# v_PYearMonth_min = df_calendar[df_calendar.Year.eq(v_PYear)]['YearMonth'].min()


# df_kpi_CYear = df_kpi[(df_kpi.AñoMes<=v_CYearMonth_max) & (df_kpi.AñoMes>=v_CYearMonth_min)][['Cajas', 'Saldo']].sum()
# df_kpi_PYear = df_kpi[(df_kpi.AñoMes<=v_PYearMonth_max) & (df_kpi.AñoMes>=v_PYearMonth_min)][['Cajas', 'Saldo']].sum()


# df_gdp = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')



# Plots
fig = px.bar(gd.df_analysis_volumen_CYear_Cliente, x='Cajas', y='Cliente', orientation= 'h')

fig_gdp = px.scatter(gd.df_gdp, x="gdp per capita", y="life expectancy",
                  size="population", color="continent", hover_name="country",
                  log_x=True, size_max=60)



# Define reutilizable objects ##
def card_kpi(Title, Value):
    return html.Div(
        [
            dbc.Card(
                id = 'kpi-card'+Title,
                children= [
                    dbc.CardBody(
                        [
                            html.H4(Title, className="card-title", style={"textAlign": "right"}),
                            # html.P("This is some card text", className="card-text"),
                            html.H5(id= 'kpi-card-'+Title+'-Value', 
                                    children= Value, className="card-title", style={"textAlign": "left"})
                        ]
                    )
                ],
                # style={"width": "18rem", "height": "30vh"},
                color= "dark", inverse= True
            )
        ]
    ) 


layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_kpi("Volumen CYear", gd.df_kpi_CYear.Cajas), md= 2),
                dbc.Col(card_kpi("Volumen PYear", gd.df_kpi_PYear.Cajas), md= 2),
                dbc.Col(card_kpi("Ingresos", "vs AA"), md= 2),
                dbc.Col(card_kpi("Facturacion CYear", gd.df_kpi_CYear.Saldo), md= 2),
                dbc.Col(card_kpi("Facturacion PYear", gd.df_kpi_PYear.Saldo), md= 2),
                dbc.Col(card_kpi("Margen", "vs AA"), md= 2)
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id= 'year-dropdown',
                        options=[
                            {'label': i, 'value': i} for i in gd.df_calendar.Year.unique()   
                        ],
                        value= gd.df_calendar.Year.max(),
                        placeholder= 'Select a Year'
                    )
                )
            ]
        ),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(figure=fig, style={'width': '100%', 'height': '100%'}),  
                            md=4, 
                            style={"height": "100%", "background-color": "green"} #
                        ),
                        dbc.Col(
                            [
                                dbc.Row(
                                    [
                                    dbc.Col(
                                        dcc.Graph(figure=fig_gdp, style={'width': '100%', 'height': '100%'}),
                                        md= 6,
                                        style={"height": "100%", "background-color": "red"} #
                                    ),
                                    dbc.Col(
                                        dcc.Graph(figure=fig_gdp, style={'width': '100%', 'height': '100%'}),
                                        md= 6,
                                        style={"height": "100%", "background-color": "yellow"} #
                                    )
                                    ], 
                                    className="h-50"
                                ),
                                dbc.Row(
                                    [
                                    dbc.Col(
                                        dcc.Graph(figure=fig_gdp, style={'width': '100%', 'height': '100%'}),
                                        md= 6,
                                        style={"height": "100%", "background-color": "blue"} #
                                    ),
                                    dbc.Col(
                                        dcc.Graph(figure=fig_gdp, style={'width': '100%', 'height': '100%'}),
                                        md= 6,
                                        style={"height": "100%", "background-color": "black"} #
                                    )
                                    ], 
                                    className="h-50"
                                )
                            ], 
                            className= "h-100",
                            md=8 
                        )
                    ], className= "h-100"
                )
            ], 
            style={"height": "70vh"}, 
            fluid=True
        )
    ]
) 



@app.callback(
    Output(component_id='kpi-card-Volumen CYear-Value', component_property='children'),
    Output(component_id='kpi-card-Facturacion CYear-Value', component_property='children'),
    Input(component_id='year-dropdown', component_property='value')
)
def update_kpi_card(selected_year):
    
    v_CYearMonth_max1 = gd.df_calendar[gd.df_calendar.Year.eq(selected_year)]['YearMonth'].max()
    v_CYearMonth_min1 = gd.df_calendar[gd.df_calendar.Year.eq(selected_year)]['YearMonth'].min() 
    
    df_kpi_CYear_filtered = gd.df_kpi[(gd.df_kpi.AñoMes <= v_CYearMonth_max1) & (gd.df_kpi.AñoMes >= v_CYearMonth_min1)][['Cajas', 'Saldo']].sum()
    
    return df_kpi_CYear_filtered.Cajas, df_kpi_CYear_filtered.Saldo