import pandas as pd

## global variables definition
v_path_input = 'datos/Input/'

# Get Global data
df_kpi = pd.read_csv(v_path_input+'df_kpi.csv')

df_calendar = pd.read_csv(v_path_input+'df_calendar.csv')


df_analysis_facturacion = pd.read_csv(v_path_input+'df_analysis_facturacion.csv')

df_analysis_volumen = pd.read_csv(v_path_input+'df_analysis_volumen.csv')[['AñoMes', 'Cliente', 'Marca', 'Cajas', 'Tipo Cliente', 'Vendedor']]

#
v_CYear= df_calendar.Year.max()
v_CYearMonth_max = df_calendar[df_calendar.Year.eq(v_CYear)]['YearMonth'].max()
v_CYearMonth_min = df_calendar[df_calendar.Year.eq(v_CYear)]['YearMonth'].min()

v_PYear = v_CYear - 1
v_PYearMonth_max = df_calendar[df_calendar.Year.eq(v_PYear)]['YearMonth'].max()
v_PYearMonth_min = df_calendar[df_calendar.Year.eq(v_PYear)]['YearMonth'].min()


df_kpi_CYear = df_kpi[(df_kpi.AñoMes<=v_CYearMonth_max) & (df_kpi.AñoMes>=v_CYearMonth_min)][['Cajas', 'Saldo']].sum()
df_kpi_PYear = df_kpi[(df_kpi.AñoMes<=v_PYearMonth_max) & (df_kpi.AñoMes>=v_PYearMonth_min)][['Cajas', 'Saldo']].sum()


df_analysis_volumen_CYear = df_analysis_volumen[(df_analysis_volumen.AñoMes <= v_CYearMonth_max) & 
                                                (df_analysis_volumen.AñoMes >= v_CYearMonth_min)]

df_analysis_volumen_CYear_Cliente = df_analysis_volumen[(df_analysis_volumen.AñoMes <= v_CYearMonth_max) & 
                                                (df_analysis_volumen.AñoMes >= v_CYearMonth_min)][['Cajas', 'Cliente']].groupby('Cliente').sum('Cajas').reset_index()


df_analysis_volumen_CYear_Cliente = df_analysis_volumen_CYear_Cliente.sort_values('Cajas', ascending= False)[:20]
df_gdp = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')




