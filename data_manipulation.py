# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:36:23 2021

@author: Adrian Manresa
"""
# Import libraries
import pandas as pd

# function definition

def f_CreateDateCol(df, DateCol):
    df = df.astype({DateCol: str})
    df = df.assign(
            year=df[DateCol].str.slice(stop=4),
            month=df[DateCol].str.slice(start=4),
            day=1
        )
    df = df.assign(date=pd.to_datetime(df[["year", "month", "day"]]))
    
    return df

## global variables definition

# path
v_path_source = 'Datos/Source/'
v_path_input = 'Datos/Input/'

## Load Source data

# Volumen
df_volumen = pd.read_excel(v_path_source+'VOLUMEN.xlsx')
# Create date column
df_volumen = f_CreateDateCol(df_volumen, 'AñoMes')

# Facturación
df_facturacion = pd.read_excel(v_path_source+'FACTURACION.xlsx')
# Create date column
df_facturacion = f_CreateDateCol(df_facturacion, 'AñoMes')

# Cliente
df_clientes = pd.read_excel(v_path_source+'CLIENTES.xlsx')

# Vendedores
df_vendedores = pd.read_excel(v_path_source+'VENDEDORES.xlsx')

# Productos
df_productos = pd.read_excel(v_path_source+'PRODUCTOS.xlsx', usecols=[0, 1, 2, 3])



## Create Calendar Table ##

v_min_date = min(df_volumen.date.min(), df_facturacion.date.min())
v_max_date = max(df_volumen.date.max(), df_facturacion.date.max())

df_calendar = pd.date_range(start=v_min_date, end=v_max_date).to_frame(index= False, name='date')

df_calendar = df_calendar.assign(MonthNum = df_calendar.date.dt.month, Year = df_calendar.date.dt.year,
                                 YearMonth = lambda x: x['Year']*100 + x['MonthNum'])

df_calendar.to_csv(v_path_input+'df_calendar.csv', index=False)



### dataset for KPIs #####

df_volumen_kpi = df_volumen[["AñoMes", "Cajas"]].groupby("AñoMes").sum("Cajas")
df_facturacion_kpi = df_facturacion[["AñoMes", "Saldo"]].groupby("AñoMes").sum("Saldo")


df_kpi = df_volumen_kpi.merge(right=df_facturacion_kpi, how='left', on='AñoMes').reset_index()

df_kpi.to_csv(v_path_input+'df_kpi.csv', index=False)


### dataset for Analysis #####

df_analysis_volumen = df_volumen.merge(right=df_clientes, how='left', on='Cliente_id').merge(
    df_productos, on='Producto_id').merge(df_vendedores, on='Cliente_id')


df_analysis_volumen = df_analysis_volumen[
    ['AñoMes', 'year', 'month', 'Cliente', 'Marca', 'Vendedor', 'Cajas', 'Tipo Cliente','date']]


df_analysis_facturacion = df_facturacion.merge(right=df_clientes, how='left', on='Cliente_id').merge(
    df_productos, how='left', on='Producto_id').merge(df_vendedores, how='left', on='Cliente_id')


df_analysis_facturacion = df_analysis_facturacion[
    ['AñoMes', 'year', 'month', 'Cliente', 'Marca', 'Vendedor', 'Saldo', 'Tipo Cliente','date']]


df_analysis_facturacion.to_csv(v_path_input+'df_analysis_facturacion.csv', index=False)
df_analysis_volumen.to_csv(v_path_input+'df_analysis_volumen.csv', index=False)


