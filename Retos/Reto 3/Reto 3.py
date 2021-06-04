import numpy as np
from scipy.integrate import odeint, solve_ivp
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def derivSIR(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def derivSIR_RK45(t, y, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def derivSI_RK45(t, y, N, beta):
    S, I = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N
    return dSdt, dIdt

def derivSI(y, t, N, beta):
    S, I = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N
    return dSdt, dIdt

#Modelos SI y SIR
#Lectura de datos SALUDATA
data_covid = pd.read_csv('/Users/safer/Desktop/Quinto Semestre Ingeniería de Sistemas/Análisis Numérico/Referencias/covid_19_bog.csv', encoding='cp1252', sep=';')
data_covid['FECHA_DIAGNOSTICO'] = pd.to_datetime(data_covid['FECHA_DIAGNOSTICO'], format='%d/%m/%Y')
#Datos iniciales
pob = 7743955
rec = 0
inf = 1
sus = pob - inf - rec
t = np.arange(0, 360)
r = [pob, inf]
v = [pob, inf, rec]
#Indices de contacto y recuperacion
beta, gamma = 0.2775, 0.022
#Calculo de sistemas de ecuaciones con ODEINT
retSI = odeint(derivSI, r, t, args=(pob, beta))
retSIR = odeint(derivSIR, v, t, args=(pob, beta, gamma))
SS, II = retSI.T
S, I, R = retSIR.T
#Calculo de sistemas de ecuaciones con RK45
retSI_RK45 = solve_ivp(derivSI_RK45, (t[0], t[-1]), r, 'RK45', args=(pob, beta))
retSIR_RK45 = solve_ivp(derivSIR_RK45, (t[0], t[-1]), v, 'RK45', args=(pob, beta, gamma))
SS_RK45, II_RK45 = retSI_RK45.y[0], retSI_RK45.y[1]
S_RK45, I_RK45, R_RK45 = retSIR_RK45.y[0], retSIR_RK45.y[1], retSIR_RK45.y[2]
#Graficas ODEINT
dfSI = pd.DataFrame({
    'Susceptibles': SS,
    'Infectados': II,
    'Dia': t
})
plt.style.use('ggplot')
dfSI.plot(x='Dia',
        y=['Infectados', 'Susceptibles'],
        color=['#bb6424', '#aac6ca', '#cc8ac0'],
        kind='line',
        stacked=False, 
        title="Modelo SI (Odeint)")
plt.show()
dfSIR = pd.DataFrame({
    'Susceptibles': S,
    'Infectados': I,
    'Recuperados': R,
    'Dia': t
})
plt.style.use('ggplot')
dfSIR.plot(x='Dia',
        y=['Infectados', 'Susceptibles', 'Recuperados'],
        color=['#bb6424', '#aac6ca', '#cc8ac0'],
        kind='area',
        stacked=False, 
        title="Modelo SIR (Odeint)")
plt.show()
#Graficas RK45
dfSI_RK45 = pd.DataFrame({
    'Susceptibles': SS_RK45,
    'Infectados': II_RK45,
    'Dia': retSI_RK45.t
})
plt.style.use('ggplot')
dfSI.plot(x='Dia',
        y=['Infectados', 'Susceptibles'],
        color=['#bb6424', '#aac6ca', '#cc8ac0'],
        kind='line',
        stacked=False, 
        title="Modelo SI (RK45)")
plt.show()
dfSIR = pd.DataFrame({
    'Susceptibles': S_RK45,
    'Infectados': I_RK45,
    'Recuperados': R_RK45,
    'Dia': retSIR_RK45.t
})
plt.style.use('ggplot')
dfSIR.plot(x='Dia',
        y=['Infectados', 'Susceptibles', 'Recuperados'],
        color=['#bb6424', '#aac6ca', '#cc8ac0'],
        kind='area',
        stacked=False, 
        title="Modelo SIR (RK 45)")
plt.show()
#Calculo de errores
TEMP = 14
index = 0
errorSI = []
errorSIR = []
start_date = pd.to_datetime('2020-03-06')
end_date = pd.to_datetime('2020-03-20')
for i in range(10):
    df_quincenal = data_covid.loc[(data_covid['FECHA_DIAGNOSTICO'] > start_date) & (data_covid['FECHA_DIAGNOSTICO'] < end_date)]
    errorSI.append(abs(II[index] - len(df_quincenal)))
    errorSIR.append(abs(I[index] - len(df_quincenal)))
    start_date = end_date
    end_date += datetime.timedelta(days=TEMP)
    index += TEMP

dfER = pd.DataFrame({
    'Errores SI': errorSI,
    'Errores SIR': errorSIR,
})
print(dfER)
print("----------------------------------------------")
#Modelo Depredador-Presa
def euler_completo(x0, y0, h, f, g, a, b):
    val_x = []
    val_y = []
    val_t = []
    
    x = x0
    y = y0
    t = 0
    
    while t < b:
        val_t.append(t)
        val_x.append(x)
        val_y.append(y)
        x = x + h * f(x,y)
        y = y + h * g(x,y) 
        t += h
    
    return val_t, val_x, val_y

def rungeKutta(f, g, x0, y0, a, b, h):
    t = np.arange(a, b, h)
    n = len(t)
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0
    y[0] = y0
    for i in range(0, n - 1):
        k1 = h*f(x[i], y[i])
        l1 = h*g(x[i], y[i])
        k2 = h*f(x[i] + k1/2, y[i] + l1/2)
        l2 = h*g(x[i] + k1/2, y[i] + l1/2)
        k3 = h*f(x[i] + k2/2, y[i] + l2/2)
        l3 = h*g(x[i] + k2/2, y[i] + l2/2)
        k4 = h*f(x[i] + k3, y[i] + l3)
        l4 = h*g(x[i] + k3, y[i] + l3)
        x[i + 1] = x[i] + (1/6) * (k1 + 2 * k2 + 2 * k3 + 2 * k4)
        y[i + 1] = y[i] + (1/6) * (l1 + 2 * l2 + 2 * l3 + 2 * l4)

    return t, y, x

f = lambda x, y: 0.4*x - 0.3*x*y
g = lambda x, y: -0.37*y + 0.05*x*y
x0 = 3
y0 = 1
a = 0
b = 100
h = 1
ti, y, x = rungeKutta(f, g, x0, y0, a, b, h)

plt.plot(ti, y, 'r--',ti, x, 'c.-')
plt.xlabel("Tiempo")
plt.ylabel("Poblacion")
plt.title('Modelo Depredador-Presa (Runge-Kutta)')
plt.legend(['Datos Depredador', 'Datos Presa'])
plt.show()
#Calculo de errores
datos_error_dp = pd.read_csv("C:/Users/safer/Desktop/Quinto Semestre Ingeniería de Sistemas/Análisis Numérico/Referencias/datosErrorDP.csv", encoding='cp1252', sep=';')

def cambio_punto_coma(df, col_name):
    df[col_name] = df[col_name].apply(lambda x: float(x.replace(',', '.')))
    return df

datos_error_dp.pipe(cambio_punto_coma,'x')
datos_error_dp.pipe(cambio_punto_coma,'y')
datos_error_dp = datos_error_dp.to_numpy()
errorRelativoPresa = (abs(datos_error_dp[len(datos_error_dp)-1, 2] - x[len(x) - 1]) / datos_error_dp[len(datos_error_dp) - 1, 2]) * 100
errorRelativoDepredador = (abs(datos_error_dp[len(datos_error_dp)-1, 3] - y[len(y) - 1]) / datos_error_dp[len(datos_error_dp) - 1, 3]) * 100

print("Eror Relativo Presas RK = {}% ".format(errorRelativoPresa))
print("Error Relativo Depredadores RK {}%".format(errorRelativoDepredador))
print("----------------------------------------------")

ti, x, y = euler_completo(x0,y0,h,f,g,a,b)

plt.plot(ti, y, 'r--',ti, x, 'c.-')
plt.xlabel("Tiempo")
plt.ylabel("Poblacion")
plt.title('Modelo Depredador-Presa (Euler)')
plt.legend(['Datos Depredador', 'Datos Presa'])
plt.show()
#Calculo de errores
datos_error_dp = pd.read_csv("C:/Users/safer/Desktop/Quinto Semestre Ingeniería de Sistemas/Análisis Numérico/Referencias/datosErrorDP.csv", encoding='cp1252', sep=';')

def cambio_punto_coma(df, col_name):
    df[col_name] = df[col_name].apply(lambda x: float(x.replace(',', '.')))
    return df

datos_error_dp.pipe(cambio_punto_coma,'x')
datos_error_dp.pipe(cambio_punto_coma,'y')
datos_error_dp = datos_error_dp.to_numpy()
errorRelativoPresa = (abs(datos_error_dp[len(datos_error_dp)-1, 2] - x[len(x) - 1]) / datos_error_dp[len(datos_error_dp) - 1, 2]) * 100
errorRelativoDepredador = (abs(datos_error_dp[len(datos_error_dp)-1, 3] - y[len(y) - 1]) / datos_error_dp[len(datos_error_dp) - 1, 3]) * 100

print("Eror Relativo Presas Euler = {}% ".format(errorRelativoPresa))
print("Error Relativo Depredadores Euler {}%".format(errorRelativoDepredador))