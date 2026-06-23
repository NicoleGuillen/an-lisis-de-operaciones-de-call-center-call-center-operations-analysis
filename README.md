Data-Driven Call Center Optimization: KPIs & Operational Efficiency

Este proyecto aplica análisis de datos y procesamiento de variables operativas para diagnosticar la eficiencia y el rendimiento de un centro de contacto. A partir de un conjunto de datos crudos (Call Center Data.csv),
se desarrolló un flujo completo de Data Cleaning y Análisis Métrico utilizando Python y Pandas para extraer insights estratégicos sobre el comportamiento de los clientes y la capacidad del equipo.

Objetivos del Proyecto:

Sanitizar y Normalizar Datos: Convertir formatos de tiempo complejos y estructurar variables inconsistentes de la operación.
Evaluar la Eficiencia Operativa: Calcular y monitorear los indicadores clave del negocio (KPIs) como AHT, Tasa de Abandono y Nivel de Servicio.
Identificar Cuellos de Botella: Analizar la degradación del servicio según factores temporales (días de la semana, horas pico).
Análisis Estadístico Avanzado: Evaluar correlaciones matemáticas entre la duración de las interacciones y la capacidad de respuesta global del centro.

Stack Tecnológico:
Lenguaje: Python 3.x
Librería Principal: Pandas (Manipulación, filtrado y agregación de datos)
Visualización (Opcional): Seaborn & Matplotlib (Análisis de tendencias y dispersión)

Arquitectura del Data Cleaning:

Los reportes de telefonía crudos suelen ser caóticos. Para garantizar la consistencia analítica, el script ejecuta las siguientes etapas de limpieza automatizada:
1.Normalización de Tiempos: Formatos de tipo cadena (HH:MM:SS) como 0:02:22 se transforman en variables numéricas enteras (Segundos Totales) mediante la equivalencia matemática para permitir operaciones estadísticas
2.Conversión de Porcentajes: Variables como Answer Rate y Service Level (originalmente interpretadas como texto por el símbolo %) se limpian y transforman en escalas decimales flotantes ($0.0 - 1.0$).
3.Sanidad de Columnas: Eliminación de espacios invisibles en los encabezados (ej. Talk Duration (AVG)  $\rightarrow$ Talk_Duration_Segundos) que rompen la sintaxis del código.
4. Auditoría de Anomalías (Outliers): Filtrado y manejo seguro de registros con valores nulos (NaN), llamadas con tiempos en cero o negativos y desbordamientos matemáticos (porcentajes > 100%).

KPIs Calculados e Interpretación Operativa:
El núcleo del análisis extrae métricas de las tres dimensiones más importantes de un call center: Pérdida, Eficiencia y Planificación.

1. Tasa de Abandono (Abandonment Rate): Mide el porcentaje de clientes que cuelgan antes de ser atendidos debido a la frustración o los tiempos de espera.
2. Tiempo Promedio de Operación (AHT - Average Handling Time): Determina la duración media que consume un agente para resolver y registrar una interacción. Debido a la naturaleza del dataset procesado, se calcula sobre el tiempo de conversación activo
3. Nivel de Servicio (Service Level): Mide el cumplimiento de los estándares operativos (por ejemplo, responder el $80\%$ de las llamadas en menos de 20 segundos) agrupado de manera temporal.

Principales Hallazgos (Insights del Negocio):
Degradación Temporal: Al agrupar el Service Level por día de la semana, se detectan caídas de rendimiento críticas, identificando visualmente qué días específicos se incumple el SLA operativo.
El "Efecto Cola de Espera" (Correlación: -0.35): Se descubrió una correlación negativa moderada entre la duración de las llamadas (AHT) y la tasa de respuesta (Answer_Rate_Decimal). Estadísticamente, esto demuestra que cuando las llamadas se extienden en exceso, los agentes quedan retenidos, la cola se satura, el cliente pierde la paciencia y la capacidad de absorción del centro de contacto disminuye drásticamente.

Recomendaciones de Negocio:

1. Se recomienda mover los horarios de almuerzo del personal de lunes a miercoles para asegurar máxima cobertura en esta franja horaria, reducir el tiempo de espera y automatizar los procesos para que los agentes atiendan a los clientes de manera más eficiente y rápida. Se necesitan automatizar más los procesos y la necesidad de más personal o de cambiar el horario de ciertos agentes a las horas críticas de la mañana/tarde es urgente ya que se encuentra que el máximo tiempo de espera (segundos): 1551 que serían 25 minutos
y el máximo tiempo de conversación (segundos): 288  que serían 4.8 minutos. El negocio necesita idealmente un AHT de 2 min 37 seg cuales si llegan a cumplir los agentes pero es muy inestable porque aveces lo cumplen y otras veces se pasan del límite de AHT.
el incumplimiento de las metricas y la saturación de llamada provoca una tasa de abandono del 10.93% cuando el estandar de la industria permite entre el 2% y el 5% máximo de tasa de abandono.
2. Para los momentos donde el volumen desborde la capacidad instalada, ofrecer al cliente la opción de "no perder su lugar en la fila y recibir una llamada de vuelta cuando un agente se libere" reduce el abandono a cero en esos casos y mejora la percepción de servicio.
3. Un AHT inusualmente alto suele ser síntoma de sistemas lentos, procesos engorrosos de post-llamada (Wrap-up time) o falta de autonomía del agente. Automatizar tareas repetitivas en sus pantallas (ej. rellenar datos del cliente de forma automática) reduce segundos valiosos de la interacción.
4.  Refuerzo en Resolución al Primer Contacto.
5.  Monitoreo de Anomalías Operativas.
