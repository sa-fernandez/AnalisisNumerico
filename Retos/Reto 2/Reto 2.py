import numpy as np
import scipy.interpolate as spi
import pandas as pd
import matplotlib.pyplot as plt
import math

#Reto 2 Analisis Numerico
#Santiago Fernandez - Mariana Galavis - German Velasco
#Principales referencias durante el desarrollo del codigo:
#https://numpy.org/
#https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splprep.html#scipy.interpolate.splprep
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splev.html#scipy.interpolate.splev
#https://pandas.pydata.org/
#https://matplotlib.org/
#https://www.fisicalab.com/apartado/errores-absoluto-relativos

def cambio_punto_coma(df, col_name):
    df[col_name] = df[col_name].apply(lambda x: float(x.replace(',', '.')))
    return df

def creacion_data(df, columns):
    df = df.pipe(cambio_punto_coma, 'Temp. Interna (ºC)')
    df_dht = df[:][columns]
    data = df_dht.to_numpy()
    return data

def eliminacion_porcentaje(data, p):
    tam = int(np.ceil(len(data) * p))
    restantes = np.zeros((tam, 4))
    for i in range(0, tam):
        r = np.random.randint(0, len(data) - i)
        restantes[i] = data[r]
        data = np.delete(data, r, 0)
    return (data, restantes)

#Lectura y transformacion de archivos
df_pen = pd.read_csv('/Users/safer/Desktop/Quinto Semestre Ingeniería de Sistemas/Análisis Numérico/Referencias/Quixada.csv', encoding='utf-8', sep=';')
df_sga = pd.read_csv('/Users/safer/Desktop/Quinto Semestre Ingeniería de Sistemas/Análisis Numérico/Referencias/Quixera.csv', encoding='utf-8', sep=';')
n, m = df_pen[df_pen.columns[0]].count(), df_sga[df_sga.columns[0]].count()
#Creacion indices
indices_1 = np.arange(n)
indices_2 = np.arange(m)
#Anexo nueva columna
df_pen.insert(24, 'Indice', indices_1, False)
df_sga.insert(24, 'Indice', indices_2,False)
data_pen = df_pen.pipe(creacion_data, ['Dia Juliano', 'Hora', 'Temp. Interna (ºC)','Indice'])
data_sga = df_sga.pipe(creacion_data, ['Dia Juliano', 'Hora', 'Temp. Interna (ºC)','Indice'])
#Establecer una copia de cada conjunto de datos
org_dp = data_pen
org_ds = data_sga
#Eliminacion del 20% de datos de forma aleatoria
p = 0.2
data_pen, elm_pen = eliminacion_porcentaje(data_pen, p)
data_sga, elm_sga = eliminacion_porcentaje(data_sga, p)
#Creacion de splines para primera estacion
s_pen = spi.splrep(data_pen[:, 3], data_pen[:, 2])
xn_pen = data_pen[:, 3]
yn_pen = spi.splev(xn_pen, s_pen)
#Creacion de interpolacion lineal para primera estacion
f_pen = spi.interp1d(data_pen[:, 3], data_pen[:, 2])
#Grafica de datos originales (primera parte)
plt.plot(org_dp[:, 3], org_dp[:, 2], 'k-')
#Grafica de spline cubico (primera parte)
plt.plot(xn_pen, yn_pen, 'r--')
#Grafica de interpolacion lineal (primera parte)
plt.plot(xn_pen, f_pen(xn_pen), 'm-.')
#Instancia de graficas (primera parte)
plt.xlabel("Índice Calculado")
plt.ylabel("Temperatura Interna")
plt.title("Primer Punto - Estacion Quixadá")
plt.legend(['Datos originales', 'Splines Cubicos', 'Interpolacion Lineal'])
plt.show()
#Ajuste de datos de segunda estacion
data_n = np.empty(((len(data_sga)), 4), float)

for i in range(0, len(data_sga)):
    for j in range(0, len(org_dp)):
        if data_sga[i][0] == org_dp[j][0] and data_sga[i][1] == org_dp[j][1]:
            data_n[i] = org_dp[j]
            data_n[i][3] = data_sga[i][3]
            break

#Creacion de splines para segunda estacion
s_sga = spi.splrep(data_n[:, 3], data_n[:, 2])
xn_sga = data_n[:, 3]
yn_sga = spi.splev(xn_sga, s_sga)
#Creacion de interpolacion lineal para segunda estacion
f_sga = spi.interp1d(data_n[:, 3], data_n[:, 2])
#Grafica de datos originales (segunda parte)
plt.plot(org_ds[:, 3], org_ds[:, 2], 'b-')
#Grafica de interpolacion lineal (segunda parte)
plt.plot(xn_sga, yn_sga, 'g--')
#Grafica de interpolacion lineal (segunda parte)
plt.plot(xn_sga, f_pen(xn_sga), 'c-.')
#Instancia de graficas (segunda parte)
plt.xlabel("Índice Calculado")
plt.ylabel("Temperatura Interna")
plt.title("Segundo Punto - Estacion Quixeramobim")
plt.legend(['Datos originales', 'Splines Cubicos', 'Interpolacion Lineal'])
plt.show()
#Calculo de errores
errorL = np.zeros(len(elm_pen))
errorS = np.zeros(len(elm_pen))
errorEMC_L = 0
errorEMC_S = 0

for k in range (0, len(elm_pen)):
    er = abs(elm_pen[k][2]-f_pen(elm_pen[k][3]))
    errorL[k] = er
    errorEMC_L += math.pow(er, 2)
    erS = abs(elm_pen[k][2]-spi.splev(elm_pen[k][3], s_pen))
    errorS[k] = erS
    errorEMC_S += math.pow(erS,2)

errorL_2 = np.zeros(len(elm_sga))
errorS_2 = np.zeros(len(elm_sga))
errorEMC_L2 = 0
errorEMC_S2 = 0

for k in range (0, len(elm_sga)):
    er = abs(elm_sga[k][2]-f_sga(elm_sga[k][3]))
    errorL_2[k] = er
    errorEMC_L2 += math.pow(er, 2)
    erS = abs(elm_sga[k][2]-spi.splev(elm_sga[k][3], s_sga))
    errorS_2[k] = erS
    errorEMC_S2 += math.pow(erS, 2)

#CALCULO DE ERRORES DE PRIMER PUNTO

print("ERRORES PRIMER PUNTO")

#Impresion de errores - Lineal
print("ERROR MAXIMO LINEAL {}".format(np.amax(errorL)))
print("ERROR MINIMO LINEAL {}".format(np.amin(errorL)))
media = np.sum(errorL)/len(errorL)
print ("ERROR MEDIA LINEAL {}".format(media))
absoluto = 0
for k in range (0, len(errorL)):
    absoluto += abs(media-errorL[k])
absoluto = absoluto/len(errorL)
print("ERROR ABSOLUTO LINEAL {}".format(absoluto))
print("ERROR MEDIO CUADRADO LINEAL {}".format(math.sqrt(errorEMC_L/len(elm_pen))))

print("----------------------------------------------")

#Impresion de errores Spline
print("ERROR MAXIMO SPLINE {}".format(np.amax(errorS)))
print("ERROR MINIMO SPLINE {}".format(np.amin(errorS)))
media = np.sum(errorS)/len(errorS)
print("ERROR MEDIA SPLINE {}".format(media))
absoluto = 0
for k in range (0,len(errorS)):
    absoluto += abs(media-errorS[k])
absoluto = absoluto/len(errorS)
print("ERROR ABSOLUTO SPLINE {}".format(absoluto))
print("ERROR MEDIO CUADRADO SPLINE {}".format(math.sqrt(errorEMC_S/len(elm_pen))))

print("--------------------------------------------------------------------------------------------------------------------------")

#CALCULO DE ERRORES DE SEGUNDO PUNTO

print("ERRORES SEGUNDO PUNTO")

#Impresion de errores - Lineal
print("ERROR MAXIMO LINEAL {}".format(np.amax(errorL_2)))
print("ERROR MINIMO LINEAL {}".format(np.amin(errorL_2)))
media = np.sum(errorL_2)/len(errorL_2)
print ("ERROR MEDIA LINEAL {}".format(media))
absoluto = 0
for k in range (0, len(errorL_2)):
    absoluto += abs(media-errorL_2[k])
absoluto = absoluto/len(errorL_2)
print("ERROR ABSOLUTO LINEAL {}".format(absoluto))
print("ERROR MEDIO CUADRADO LINEAL {}".format(math.sqrt(errorEMC_L2/len(elm_sga))))

print("----------------------------------------------")

#Impresion de errores Spline
print("ERROR MAXIMO SPLINE {}".format(np.amax(errorS_2)))
print("ERROR MINIMO SPLINE {}".format(np.amin(errorS_2)))
media = np.sum(errorS_2)/len(errorS_2)
print("ERROR MEDIA SPLINE {}".format(media))
absoluto = 0
for k in range (0,len(errorS_2)):
    absoluto += abs(media-errorS_2[k])
absoluto = absoluto/len(errorS_2)
print("ERROR ABSOLUTO SPLINE {}".format(absoluto))
print("ERROR MEDIO CUADRADO SPLINE {}".format(math.sqrt(errorEMC_S2/len(elm_sga))))