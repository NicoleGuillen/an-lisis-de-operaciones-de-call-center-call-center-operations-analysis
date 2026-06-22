import pandas as pd

# 1. Cargar el archivo CSV
df = pd.read_csv(r"C:\Users\nicol\OneDrive\Desktop\Call center data PYTHON\Call_Center_Data_PROCESADO.csv")

#Análisis Exploratorio de Métricas claves - KPI´s importantes

#1. Average Handle Time (AHT)
#código en Python utilizando Pandas para calcular el AHT total y también para ver cómo varía día a día (por fila) 
# el kpi se calcula sobre las llamadas contestadas (Answered Calls)

aht_general_segundos = df['Talk_Duration_Segundos'].mean()

# Convertir a formato minutos:segundos para que sea legible
minutos = int(aht_general_segundos // 60)
segundos = int(aht_general_segundos % 60)
print("--- REPORTE DE AHT ---")
print(f"AHT General del Call Center: {aht_general_segundos:.2f} segundos ({minutos} min {segundos} seg)\n")

#AVERAGE HANDLING TIME DIARIO, creación de columna de análisis de KPIs
df['AHT_Segundos'] = df['Talk_Duration_Segundos']

# Mostramos las primeras filas para verificar
print("Primeras filas con la métrica AHT:")
print(df[['Index', 'Answered Calls', 'Talk_Duration_Segundos', 'AHT_Segundos']].head())

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar el dataset
df = pd.read_csv('Call_Center_Data_PROCESADO.csv')

# Renombrar Talk_Duration_Segundos a AHT para mantener coherencia en el análisis
df['AHT_Segundos'] = df['Talk_Duration_Segundos']

print("--- 1. SEGMENTACIÓN POR NIVEL DE EFICIENCIA (AHT) ---")
# Clasificamos el AHT en 3 rangos (Bajo, Objetivo, Alto) usando los cuantiles del dataset
q1 = df['AHT_Segundos'].quantile(0.33)
q2 = df['AHT_Segundos'].quantile(0.66)

def clasificar_aht(segundos):
    if segundos <= q1:
        return 'Bajo (Rápido)'
    elif segundos <= q2:
        return 'Normal (Objetivo)'
    else:
        return 'Alto (Lento)'

df['Categoria_AHT'] = df['AHT_Segundos'].apply(clasificar_aht)

# Ver cuántos días/intervalos caen en cada categoría y su Service Level promedio
resumen_eficiencia = df.groupby('Categoria_AHT').agg(
    Frecuencia=('Index', 'count'),
    AHT_Promedio_Seg=('AHT_Segundos', 'mean'),
    Llamadas_Atendidas_Promedio=('Answered Calls', 'mean'),
    Nivel_Servicio_Promedio=('Service_Level_Decimal', 'mean')
).reset_index()

print(resumen_eficiencia.to_string(index=False))
print("\n" + "-"*50 + "\n")


print("--- 2. SEGMENTACIÓN POR VOLUMEN DE LLAMADAS ENTRANTES ---")
# ¿El volumen de llamadas entrantes afecta la velocidad con la que atienden?
df['Segmento_Trafico'] = pd.qcut(df['Incoming Calls'], q=3, labels=['Tráfico Bajo', 'Tráfico Medio', 'Tráfico Alto'])

resumen_trafico = df.groupby('Segmento_Trafico').agg(
    AHT_Promedio_Seg=('AHT_Segundos', 'mean'),
    Nivel_Servicio_Promedio=('Service_Level_Decimal', 'mean'),
    Tasa_Abandono_Promedio=('Abandoned Calls', 'mean')
).reset_index()

print(resumen_trafico.to_string(index=False))
print("\n" + "-"*50 + "\n")





#CALCULAR LA TASA DE ABANDONO GLOBAL (De todo el dataset)
total_entrantes = df['Incoming Calls'].sum()
total_abandonadas = df['Abandoned Calls'].sum()
tasa_abandono_global = (total_abandonadas / total_entrantes) * 100

print(f"--- Métrica Global ---")
print(f"Total Llamadas Entrantes: {total_entrantes:,}")
print(f"Total Llamadas Abandonadas: {total_abandonadas:,}")
print(f"Tasa de Abandono Global: {tasa_abandono_global:.2f}%\n")

# CREAR COLUMNA FILA POR FILA (Por día o registro)
# Usamos .div() o división directa cuidando que no haya divisiones por cero
df['Abandon_Rate_Decimal'] = df['Abandoned Calls'] / df['Incoming Calls']
# Opción blindada contra ceros (rellena con 0 si no hubo llamadas entrantes):
df["Abandon_Rate_Decimal"] = (
    df["Abandoned Calls"] / df["Incoming Calls"]
).fillna(0)
df['Abandon_Rate_Porcentaje'] = df['Abandon_Rate_Decimal'] * 100

# Ver los primeros resultados para verificar
print("--- Muestra de las primeras filas con la nueva métrica ---")
print(df[['Incoming Calls', 'Abandoned Calls', 'Abandon_Rate_Porcentaje']].head())

# Calculo de Service level
nivel_servicio_global = df["Service_Level_Decimal"].mean() * 100
print(f"Nivel de Servicio Global: {nivel_servicio_global:.2f}%")

# Velocidad Promedio de Respuesta (Average Speed of Answer - ASA)
asa_global = df["Answer_Speed_Segundos"].mean()
print(f"Velocidad Promedio de Respuesta (ASA): {asa_global:.2f} segundos")

# Tiempo Promedio de Espera (Average Waiting Time - AWT)
awt_global = df["Waiting_Time_Segundos"].mean()
print(f"Tiempo Promedio de Espera (AWT): {awt_global:.2f} segundos")

# Calculamos la columna de abandono justo como se tenía (blindado contra división por cero)
df["Abandon_Rate_Porcentaje"] = (
    df["Abandoned Calls"] / df["Incoming Calls"]
).fillna(0) * 100

# Análisis de Capacidad Extrema (Días de Desbordamiento)
# Si el tiempo de espera promedio supera los 3 minutos (180 segundos), el sistema colapsó
df["Sistema_Saturado"] = df["Waiting_Time_Segundos"] > 180

Días_colapsados = df["Sistema_Saturado"].sum()
print(f"El Call Center colapsó debido a alta demanda en {Días_colapsados} días de todo el histórico.")

correlacion = df["Talk_Duration_Segundos"].corr(df["Answer_Rate_Decimal"])
print(f"Correlación entre duración y tasa de respuesta: {correlacion:.2f}")

# 2. Seleccionar ÚNICAMENTE las columnas numéricas limpias para la matriz
# Usamos los nombres exactos de tus columnas numéricas en segundos y decimales
columnas_numericas = [
    "Talk_Duration_Segundos",
    "Answer_Rate_Decimal",
    "Incoming Calls",
]

# Creamos la matriz de correlación asegurando que no haya texto interfiriendo
matriz_corr = df[columnas_numericas].corr()

# 3. Configurar el diseño de la gráfica
plt.figure(figsize=(6, 4))
sns.set_theme(style="white")

# Creación del Heatmap (Mapa de calor)
sns.heatmap(
    matriz_corr,
    annot=True,  # Muestra los números de correlación (como el -0.35)
    cmap="coolwarm",  # Azul para negativo, Rojo para positivo
    fmt=".2f",
    vmin=-1,
    vmax=1,
    linewidths=0.5,
)

# 4. Títulos y etiquetas limpias
plt.title("Matriz de Correlación: Eficiencia Operativa", fontsize=12, pad=15)
plt.tight_layout()

# 5. Mostrar la gráfica y cerrar procesos para evitar congelamientos o bucles
plt.show()
plt.close()