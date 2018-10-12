# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:05:32 2018

@author: 50295
"""

import pandas as pd
import seaborn as sns

sns.set_style("whitegrid")

xlsFile = xls = pd.ExcelFile('bd_lineas.xls')
sheets = xlsFile.sheet_names

dfLineas = pd.DataFrame()
dfAux = [pd.read_excel(xlsFile, sheet_name=s) for s in sheets]
dfLineas = pd.concat(dfAux)
dfLineas = dfLineas.drop(['Calibre de conductor', 'Tipo de condcutor'], axis=1)
dfLineas = dfLineas[dfLineas['Estado'] == 'Operacion']
dfLineas = dfLineas.drop('Estado')

dfLineas['Nivel de tensión (kV)']=dfLineas['Nivel de tensión (kV)'].astype('category')
dfLineas['Clase']=dfLineas['Clase'].astype('category')
niveles=dfLineas['Nivel de tensión (kV)'].cat.categories

dNiv={nivel:dfLineas[dfLineas['Nivel de tensión (kV)'] == nivel].describe() for nivel in niveles}