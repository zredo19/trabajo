import streamlit as st
import pandas as pd
from PIL import Image

st.title('Analisis de los suicidios y la salud mental en Santiago de Chile')

st.write('Durante este informe realizaremos el análisis de un DataFrame, el cual nos muestra datos acerca de los Antecedentes de Suicidios ocurridos en Santiago durante el año 2011 ocupamos las librerias de pandas y para mostrar varios datos importantes de este DataFrame y analizarlo de mejor manera. Además de ocupar la libreria Matplotlib para realizar graficos con la información del DataFrame')
st.write("Nuestro objetivo como grupo será analizar los suicidios ocurridos en el año 2011 en Santiago, esto se debe a que queremos demostrar que la problemática de la salud mental en nuestra capital que viene de hace muchos años y lo poca importancia que se le da este asunto tan delicado como lo es el suicidio y nuestra salud mental a nivel país. Para poder realizar este trabajo ocuparemos bibliotecas como requests, json, pandas, streamlit, entre otras, para seleccionar y procesar datos donde encontraremos las comunas con mayor tasa de suicidio, también evidenciaremos que edades hay mayor tasa de suicidio y a su vez el sexo de la persona.")

imagen = Image.open("salud.jpg")
st.image(imagen)

st.markdown('---')


st.markdown('**Lo primero que hicimos fue utilizar el siguiente codigo para obtener los datos del DataFrame de la pagina https://datos.gob.cl/group, el cual contiene Antecedentes de Suicidios ocurridos en Santiago durante el año 2011:**')

st.code("""
# Definir la URL del recurso que contiene los datos
url = "https://datos.gob.cl/api/3/action/datastore_search?resource_id=92af6f2b-22a0-41ea-897c-93f1c382aabb"

# Realizar una solicitud HTTP para obtener los datos de la URL
respuesta = requests.get(url)

# Crear un objeto StringIO a partir de los datos de la respuesta
# y decodificar el contenido de la respuesta como UTF-8
datos_csv = io.StringIO(respuesta.content.decode("utf-8"))

# Utilizar pandas para leer los datos CSV desde el objeto StringIO y cargarlos en un DataFrame
df = pd.read_csv(datos_csv, sep=",")
""", language="python")

st.markdown('**Lo siguiente que hicimos fue usar el método .head() de pandas para mostrar las primeras filas del DataFrame y asi tener un mejor entendimiento de este.**')

st.code("""
print(df.head())
""", language="python")

st.markdown('Este seria el resultado:')

imagen = Image.open("11.png")
st.image(imagen)

st.markdown('---')

st.markdown('**Usamos .info() para conocer el tipo de dato y cuantos datos contenia el dataframe, ademas de alguna que otra información extra. En conjunto también Utilizamos .describe() para obtener una descripción de los datos numéricos en el DataFrame, aunque en este caso solo eran 2.**')

st.code("""
df.info()
print(df.describe())
""", language="python")

st.markdown('Este seria el resultado:')

imagen = Image.open("22.png")
st.image(imagen)

st.markdown('---')

st.markdown('**Utilizamos este metodo para mostrar tanto las edades mas bajas como las mas altas de las personas que se suicidaron:**')

st.code("""
top_5_Edad_Bajo= df.nsmallest(5, 'EDAD')
top_5_Edad_Alto = df.nlargest(5, 'EDAD')
print(top_5_Edad_Bajo)
print(top_5_Edad_Alto)
""", language="python")

st.markdown('Este seria el resultado:')

imagen = Image.open("33.png")
st.image(imagen)

st.markdown('---')

st.markdown('**Utilizamos el siguiente código para contabilizar las veces que se repite cada comuna, es decir, la cantidad de suicidios por comuna para poder realizar un mejor analisis de estos datos.**')

st.code("""
comunas = ['Puente Alto', 'San Miguel', 'Las Condes', 'Paine', 'Maipú','Pudahuel', 'Cerro Navia', 'Colina', 'Providencia', 'Recoleta','Buin', 'La Florida', 'La Pintana']
repeticiones = df['COMUNA RESIDENCIA'].value_counts()[comunas]
print(repeticiones)
""", language="python")

st.markdown('Este seria el resultado:')

imagen = Image.open("44.png")
st.image(imagen)

st.markdown('---')




st.title("Analisis de datos utilizando los gráficos")

st.markdown('**Utilizamos este codigo para encontrar las 5 edades que más se suicidan:**')

st.code("""
edad_counts = df.groupby('EDAD')['EDAD'].count()

top_5_edad = edad_counts.sort_values(ascending=False).head(5)
top_5_edad.plot(kind='bar')
plt.title('Top 5 Edades que mas se suicidan')
plt.xlabel('Edad')
plt.ylabel('Numero de suicidios')
plt.show()
""", language="python")

st.markdown('Este seria el resultado:')

imagen = Image.open("graf1.png")
st.image(imagen)

st.write("Con esta información nos damos cuenta de que las personas que más se suicidan estan entre la edad de 20 y 50 años, esto se debe a un gran cantidad de factores, pero nosotros creemos que los principales son las presiones laborales y económicas, el estigma y barreras para buscar ayuda; y los trastornos de salud mental.")

st.markdown('---')

st.markdown('**Con este codigo buscamos las 5 edades que menos se suicidan:**')

st.code("""
edad_count_2 = df.groupby('EDAD')['EDAD'].count()

top_5_edad2 = edad_count_2.sort_values().head(5)    
top_5_edad2.plot(kind='bar')
plt.title('Top 5 Edades que menos se suicidan')
plt.xlabel('Edad')
plt.ylabel('Numero de suicidios')
plt.show()
""", language="python")

st.markdown('Este seria el resultado:')

imagen = Image.open("graf2.png")
st.image(imagen)

st.write("Lo que podemos decir con este gráfico es que hay dos etapas en las que hay menos suicidos, una es a temprana edad como pueden ser los 11 años, y la otra es en la tercera edad, nosotros lo asociamos a la Perspectiva de Vida, Algunas personas mayores pueden tener una perspectiva de vida que les permite poner en contexto las dificultades actuales y adoptar una visión más amplia, mientras que cuando estas en una temprana edad tienes muchas menos preocupaciones y problemas por lo que la cantidad de suicidios es muchisimo menor.")

st.markdown('---')

st.markdown('**Usamos el siguiente codigo para crear un grafico de pastel con el % suicidio de hombres y mujeres:**')
st.code("""
sexo_counts = df['SEXO'].value_counts()
plt.pie(sexo_counts, labels=sexo_counts.index, autopct='%1.1f%%')
plt.title('Porcentaje de suicidios de hombres y mujeres')
plt.show()
""", language="python")

st.markdown('Este seria el resultado:')

imagen = Image.open("graf3.png")
st.image(imagen)

st.write("Con esto podemos decir claramente hay muchos mas hombres que se suicidan que mujeres, y aunque hay muchos factores por lo que esto puede ocurrir, nosotros le dmos la razón a una Estigmatización de la salud mental, Los hombres a menudo enfrentan estigmatización en relación con los problemas de salud mental y pueden ser menos propensos a buscar ayuda o hablar abiertamente sobre sus problemas emocionales. ")

st.markdown('---')

st.markdown('**Con el siguiente codigo buscamos comparar la cantidad de suicidios de 3 comunas:**')

st.code("""
puente_alto_s = df[df['COMUNA RESIDENCIA'] == 'Puente Alto']
las_condes_s = df[df['COMUNA RESIDENCIA'] == 'Las Condes']
san_miguel_s = df[df['COMUNA RESIDENCIA'] == 'Maipú']

puente_alto_s = df[df['COMUNA RESIDENCIA'] == 'Puente Alto']
las_condes_s = df[df['COMUNA RESIDENCIA'] == 'Las Condes']
san_miguel_s = df[df['COMUNA RESIDENCIA'] == 'Huechuraba']

df['FECHA DEFUNCION'] = pd.to_datetime(df['FECHA DEFUNCION'])

df_puente = df[df['COMUNA RESIDENCIA'] == 'Puente Alto'].groupby(pd.Grouper(key='FECHA DEFUNCION', freq='M')).count()
df_condes = df[df['COMUNA RESIDENCIA'] == 'Las Condes'].groupby(pd.Grouper(key='FECHA DEFUNCION', freq='M')).count()
df_miguel = df[df['COMUNA RESIDENCIA'] == 'Huechuraba'].groupby(pd.Grouper(key='FECHA DEFUNCION', freq='M')).count()

plt.plot(df_puente.index, df_puente['COMUNA RESIDENCIA'], label='Puente Alto')
plt.plot(df_condes.index, df_condes['COMUNA RESIDENCIA'], label='Las Condes')
plt.plot(df_miguel.index, df_miguel['COMUNA RESIDENCIA'], label='Huechuraba')
plt.xlabel('Fecha')
plt.ylabel('Numero de Suicidios')
plt.legend()
plt.show()
""", language="python")

st.markdown('Este seria el resultado:')

imagen = Image.open("graf4.png")
st.image(imagen)

st.write("Con los resultdos de este gráfico concluimos que mientras menor sea la calidad de vida de la comuna, como en este caso lo es puente alto, mayor es la tasa de suicidio ya que otras comunas con mejor calidad de vida presentan una menor tasa de suicidio.")

st.markdown('---')

st.title("Conclusión")

st.write("En conclusión, el fenómeno del suicidio es una realidad compleja y multifacética que afecta a individuos, comunidades y sociedades en todo el mundo. A lo largo de este trabajo, hemos explorado diversas dimensiones que influyen en el riesgo de suicidio, desde factores biológicos y psicológicos hasta factores sociales y culturales. Es evidente que no hay una única causa que explique el comportamiento suicida, y la interacción de diversos elementos contribuye a la complejidad de este fenómeno. El estigma asociado con los trastornos mentales, la falta de acceso a servicios de salud mental, las presiones sociales y económicas, y la ausencia de redes de apoyo adecuadas son solo algunos de los desafíos que enfrentan aquellos en riesgo. La comprensión profunda de estos factores es esencial para desarrollar estrategias efectivas de prevención y apoyo. En nuestro análisis, hemos observado cómo diferentes grupos de edad y género pueden experimentar tasas de suicidio distintas, destacando la importancia de enfoques personalizados y sensibles a la diversidad. La promoción de la conciencia sobre la salud mental, la reducción del estigma, la mejora del acceso a servicios de apoyo y la creación de entornos de apoyo social son pasos cruciales para abordar el problema del suicidio. En última instancia, la prevención del suicidio requiere un esfuerzo colectivo que involucre a profesionales de la salud, comunidades, gobiernos y a la sociedad en su conjunto. Al trabajar juntos para comprender, abordar y superar los desafíos asociados con el suicidio, podemos aspirar a construir un mundo en el que la salud mental sea prioridad, y donde cada individuo se sienta respaldado y comprendido en su viaje hacia el bienestar emocional.")
