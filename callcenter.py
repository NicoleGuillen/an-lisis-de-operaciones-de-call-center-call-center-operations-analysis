import pandas as pd

# 1. Cargar el archivo CSV
df = pd.read_csv("Call Center Data.csv")

# 2. Ver las dimensiones (Filas, Columnas)
print(df.shape)

# 3. Inspeccionar los tipos de datos y nulos
print(df.info())

# 4. Ver estadísticas rápidas de las columnas numéricas
print(df.describe())


# Limpieza de datos (data cleaning)

# 1. Convertir 'Answer Speed (AVG)' a segundos
# Nota: errors='coerce' transforma cualquier texto corrupto o nulo en NaN para que no rompa el código
timedelta_speed = pd.to_timedelta(df['Answer Speed (AVG)'], errors='coerce')
df['Answer_Speed_Segundos'] = timedelta_speed.dt.total_seconds().fillna(0).astype(int)

# 2. Convertir 'Talk Duration (AVG) ' a segundos 
# Ojo: nota que tu columna original tiene un espacio al final del nombre 'Talk Duration (AVG) '
timedelta_talk = pd.to_timedelta(df['Talk Duration (AVG)'], errors='coerce')
df['Talk_Duration_Segundos'] = timedelta_talk.dt.total_seconds().fillna(0).astype(int)

# 3. Convertir 'Waiting Time (AVG)' a segundos
timedelta_waiting = pd.to_timedelta(df['Waiting Time (AVG)'], errors='coerce')
df['Waiting_Time_Segundos'] = timedelta_waiting.dt.total_seconds().fillna(0).astype(int)

# --- Verificación ---
# Imprimir las nuevas columnas creadas para confirmar que son números enteros
print(df[['Answer_Speed_Segundos','Talk_Duration_Segundos', 'Waiting_Time_Segundos']].head())

# 4. Transformar 'Answer Rate'
# Eliminamos el símbolo '%', convertimos a numérico y dividimos entre 100
df['Answer_Rate_Decimal'] = pd.to_numeric(df['Answer Rate'].str.replace('%', ''), errors='coerce') / 100

# 5. Transformar 'Service Level (20 Seconds)'
# Hacemos exactamente lo mismo para el nivel de servicio
df['Service_Level_Decimal'] = pd.to_numeric(df['Service Level (20 Seconds)'].str.replace('%', ''), errors='coerce') / 100

# --- Verificación ---
# Imprimimos las columnas originales junto a las nuevas transformadas
print(df[['Answer Rate', 'Answer_Rate_Decimal', 'Service Level (20 Seconds)', 'Service_Level_Decimal']].head())

# 6. Eliminar filas duplicadas si existen
duplicados_antes = df.duplicated().sum()
df = df.drop_duplicates()

print(f"Se eliminaron {duplicados_antes} filas exactamente duplicadas.")

# 7. Eliminar espacios en blanco al principio y al final de los nombres de todas las columnas
df.columns = df.columns.str.strip()

# 8. Ver cuántos valores nulos hay en cada columna antes de limpiar
print("Nulos por columna:")
print(df.isnull().sum())

# 9. Rellenar los nulos de las columnas de conteo con 0
columnas_conteo = ['Incoming Calls', 'Answered Calls', 'Abandoned Calls']
df[columnas_conteo] = df[columnas_conteo].fillna(0)

# 10. Crear una máscara para encontrar filas donde la suma no cuadre
error_matematico = df['Incoming Calls'] != (df['Answered Calls'] + df['Abandoned Calls'])

# 11. Contar cuántas filas tienen este error
print(f"Filas con inconsistencias en el conteo de llamadas: {error_matematico.sum()}")

# 12. Si se quiere ver cuáles son esas filas con errores para revisarlas:
print(df[error_matematico])

# 13.Convertir columnas de conteo a enteros
df['Incoming Calls'] = df['Incoming Calls'].astype(int)
df['Answered Calls'] = df['Answered Calls'].astype(int)
df['Abandoned Calls'] = df['Abandoned Calls'].astype(int)


# Buscar si hay llamadas donde el tiempo de hablar o esperar sea menor o igual a cero
tiempo_cero_o_negativo = (df['Talk_Duration_Segundos'] <= 0) | (df['Waiting_Time_Segundos'] < 0)
print(f"Llamadas con tiempos ilógicos: {tiempo_cero_o_negativo.sum()}")

# Opción: Quedarte solo con las filas que sí tengan tiempos lógicos
df = df[~tiempo_cero_o_negativo]

# Ver el valor máximo de cada columna de tiempo
print("Máximo tiempo de conversación (segundos):", df['Talk_Duration_Segundos'].max())
print("Máximo tiempo de espera (segundos):", df['Waiting_Time_Segundos'].max())

# Si encuentras una llamada de 12 horas, puedes filtrarla para que no altere tus KPIs:
# Ejemplo: borrar llamadas de más de 3 horas (10800 segundos)
df = df[df['Talk_Duration_Segundos'] < 10800]

# Validar que ningún porcentaje supere el 100%
porcentajes_corruptos = (df['Answer_Rate_Decimal'] > 1.0) | (df['Service_Level_Decimal'] > 1.0)
print(f"Filas con porcentajes imposibles: {porcentajes_corruptos.sum()}")


# 14. Guardar el resultado limpio en un nuevo CSV
df.to_csv("Call_Center_Data_PROCESADO.csv", index=False)
print("¡Limpieza de datos completada con éxito!")