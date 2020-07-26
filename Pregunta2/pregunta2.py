# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:21:15 2020

@author: Usuario
"""
#libreias a utilizar
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
#importando los cvs
paciente =pd.read_csv('Paciente.csv',header=0)
# imprimiendo pacientes
print("............. Pacientes ...............")
# print(paciente)
paciente_train=pd.read_csv('Paciente_train.csv',header=0)
print("............. Pacientes Train ...............")
# print(paciente_train)

#------------------Preprocesamiento-----------
#Eliminamos columnas que no llegaremos a utilizar
paciente=paciente.drop(['Nombre Completo', 'id'],axis=1)
paciente_train=paciente_train.drop(['Nombre Completo', 'id'],axis=1)
#Cambiamos las variables por numericos
paciente['Sexo'].replace(['M','F'],[1,0],inplace=True)
paciente_train['Sexo'].replace(['M','F'],[1,0],inplace=True)
paciente['Residencia'].replace(['La Paz','Oruro','Cochabamba','Beni','Potosi','Santa Cruz'],[0,1,2,3,4,5],inplace=True)
paciente_train['Residencia'].replace(['La Paz','Oruro','Cochabamba','Beni','Potosi','Santa Cruz'],[0,1,2,3,4,5],inplace=True)
paciente_train['Observacion'].replace(['Normal','Pre_Diabetes','Diabetes'],[0,1,2],inplace=True)
# pacientes con el <= 5.7es Normal
# paciente en el rango de >=5.7 o <=6.4 indica una pre Diabetes
# pacientes >=6.5 pacientes con diabetes
print(paciente)
print(paciente_train)

#----------------PIPELINE----------------------
from sklearn.model_selection import train_test_split
X = np.array(paciente_train.drop(['Observacion'],1))
Y = np.array(paciente_train['Observacion'])
# print(X)
# print(Y)

X_train, X_test, Y_train, Y_test =train_test_split(X,Y,test_size=0.3)

#predicción
modelo = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
modelo.fit(X_train, Y_train)
print("......... ----PREDICCION----..............")
print(modelo.predict(X_test))
print("....................................")

#_-------------------------------------
model = make_pipeline(StandardScaler(),LogisticRegression())
model.fit(X_train, Y_train)
print("Presicion del modelo: %f" % model.score(X_test, Y_test))
# print(model.predict_proba(X_test))


