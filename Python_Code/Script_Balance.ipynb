# %%
# Selecciona Balance y Período para descargar: 
BalanceFile = "Balance2019.csv"
Periodo = 'Anual' # 'Anual' si es Balance del Año. 'Q1'..'Q4' si es Trimestral.

# %% [markdown]
# ### Tranformación Automatizada Datos Holded:

# %%
import pandas as pd 
import numpy as np 

# %%
# Importamos data:
    # BalanceFile = "Balance2022.csv"
    # Periodo = 'Anual'

Balance = pd.read_csv(f"/home/user/holded/HoldedFiles/{BalanceFile}", header = None) 

# %%
# Renombramos nombres de columnas:
Balance = Balance.rename(columns={0 : 'Subcuenta', 1 : 'Valor'})

# %% [markdown]
# * 1. Partida:

# %%
# Creamos columna con el nombre de la partida:
Balance['Partida'] = Balance['Subcuenta'].where(Balance['Valor'].isna()).ffill()
# Borrar fila original donde Valor es NaN:
Balance = Balance[~Balance['Valor'].isna()]

# %%
Balance

# %% [markdown]
# * 2. Subpartida:

# %%
Subpartidas = pd.Series(['Activo No Corriente', 'Activo Corriente', 'Patrimonio Neto',
                       'Pasivo Corriente', 'Pasivo No Corriente'])
print(Subpartidas)

# %%
# 1. Creamos columna para filas con Subpartidas:
Balance['Subpartida'] = Balance['Subcuenta'].where(Balance['Subcuenta'].isin(Subpartidas)).ffill()
# 2. Eliminamos la columna con Subpartida Original:
Balance = Balance[~Balance['Subcuenta'].isin(Subpartidas)]

# %%
Balance

# %% [markdown]
# * 3. Grupo:

# %%
Grupo_id = pd.Series(['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'])

# %%
Grupo_id = Grupo_id.tolist()

# %%
# Para crear columna Grupo:
Balance['Grupo'] = Balance['Subcuenta'].where(Balance['Subcuenta'].str.startswith(tuple(Grupo_id))).ffill()
# Para Borrar Filas Grupo Original:
Balance = Balance[~Balance['Subcuenta'].str.startswith(tuple(Grupo_id))]

# %%
Balance

# %% [markdown]
# * Subgrupo:

# %%
Subgrupo_id = pd.Series(['1.', '2.', '3.', '4.', '5.', '6.', '7.',
                         '8.', '9.']).tolist()

# %%
# Creamos columna Subgrupo:
Balance['SubGrupo'] = Balance['Subcuenta'].where(Balance['Subcuenta'].str.startswith(tuple(Subgrupo_id))).ffill()
# Eliminamos columna original con Subgrupo:
Balance = Balance[~Balance['Subcuenta'].str.startswith(tuple(Subgrupo_id))]

# %%
Balance

# %% [markdown]
# * Cuenta:

# %%
print(Balance)

# %%
Balance['Subcuenta'].where(pd.to_numeric(Balance['Subcuenta'].str.extract(r'^(\d+)')[0]) < 1000).ffill()


# %%
Balance['Cuenta'] = Balance['Subcuenta'].where(pd.to_numeric(Balance['Subcuenta'].str.extract(r'^(\d+)')[0]) < 10000).ffill()

# %%
Balance

# %%
Balance['Cuenta'] = Balance['Cuenta'].where(pd.to_numeric(Balance['Subcuenta'].str.extract(r'^(\d+)')[0]) < 10000).ffill()

Balance['Cuenta'].where(pd.to_numeric(Balance['Subcuenta'].str.extract(r'^(\d+)')[0]) < 10000)

# %%
Balance = Balance[~(pd.to_numeric(Balance['Subcuenta'].str.extract(r'^(\d+)')[0]) < 10000)]

# %%
Balance

# %%
# Configuración Año y Periodo (Establecidos en el inicio del script)

Año = BalanceFile[7:11]

Balance['Año'] = Año
Balance['Periodo'] = Periodo

# %% [markdown]
# * Ordenar Columnas:

# %%
Balance = Balance[['Año', 'Periodo', 'Partida', 'Subpartida', 'Grupo', 'SubGrupo', 'Cuenta', 'Subcuenta', 'Valor']]

# %%
Balance

# %% [markdown]
# * Pendiente Transformación: Desglosar Columnas correspondientes en {Id y Nombre}

# %%
# Division Columnas y creación columnas_id's: 

Balance[['Grupo_id', 'Grupo']] = Balance['Grupo'].str.split('. ', n = 1, expand = True)              # Grupo
Balance[['SubGrupo_id', 'SubGrupo']] = Balance['SubGrupo'].str.split('. ', n = 1, expand = True)     # SubGrupo
Balance[['Cuenta_id', 'Cuenta']] = Balance['Cuenta'].str.split(' ', n = 1, expand = True)            # Cuenta
Balance[['Subcuenta_id', 'Subcuenta']] = Balance['Subcuenta'].str.split(' - ', n = 1, expand = True) # Subcuenta


# %%
Balance.head(5)

# %%
Balance.columns

# %%
# Ordenamos el dataframe: 
Balance = Balance[['Año', 'Periodo', 'Partida', 'Subpartida', 'Grupo_id', 'Grupo', 'SubGrupo_id', 'SubGrupo',
                 'Cuenta_id', 'Cuenta', 'Subcuenta_id', 'Subcuenta', 'Valor']]

# %%
# Cambiamos tipo de dato de Valor de Object a Numeric:
Balance['Valor'] = Balance['Valor'].str.replace('.', '', regex=False)   # Elimina los puntos que separan miles
Balance['Valor'] = Balance['Valor'].str.replace(',', '.', regex=False)  # Reemplaza las comas por puntos decimales
Balance['Valor'] = pd.to_numeric(Balance['Valor'], errors='coerce')

# %%
Balance.head(10)

# %% [markdown]
# ### Resultado y Descarga: 

# %%
Balance.head(4)

# %%
### Descarga arhivo: 
NombreArchivo = f"File.Balance{Año}.csv"
Balance.to_csv(NombreArchivo, index=False)


# %%
f"Archivo creado llamado: 'File.Balance{Año}.csv'"


