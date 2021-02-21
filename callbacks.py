# callbacks.py

# Import Libraries

# from dash.dependencies import Input, Output

# from app import app


# @app.callback(
#     Output(component_id='kpi-card-Volumen CYear-Value', component_property='children'),
#     Input(component_id='year-dropdown', component_property='value')
# )
# def update_kpi_card(selected_year):
    
#     v_CYearMonth_max1 = df_calendar[df_calendar.Year.eq(selected_year)]['YearMonth'].max()
#     v_CYearMonth_min1 = df_calendar[df_calendar.Year.eq(selected_year)]['YearMonth'].min() 
#     df_kpi_CYear_filtered = df_kpi[(df_kpi.AñoMes<=v_CYearMonth_max1) & (df_kpi.AñoMes>=v_CYearMonth_min1)][['Cajas', 'Saldo']].sum()
    
#     return df_kpi_CYear_filtered.Cajas