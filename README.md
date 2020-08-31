## Proyecto de Data analytics con pandas - Bootcamp Fulltime de Data Anlytics de Ironhack's

![Ironhack logo](https://www.fundacionuniversia.net/wp-content/uploads/2017/09/ironhack_logo.jpg)

## Resumen del proyecto

Este proyecto consiste en la limpieza y manipulación de los datos contenidos en un archivo CSV con Python, relativo a los ataques de tiburones en el mundo a lo largo de la historia. Asumidas dos hipótesis propias, se trata de validar la veracidad de las mismas a través de los datos.

En este caso, el archivo CSV de origen no se ha subido a Github, a solicitud de su autor.

![Tiburon](https://www.ngenespanol.com/wp-content/uploads/2018/08/%C2%BFPor-qu%C3%A9-disminuy%C3%B3-el-riesgo-de-ataques-de-tibur%C3%B3n-770x413.jpg)


## Recursos utilizados

* Dataset: Archivo CSV con el histórico de ataques de tiburón en el mundo. Se trata de un archivo de 25723 filas y 24 columnas de información:
![Columnas1-10](https://github.com/silviaherf/data-cleaning-pandas/blob/master/Images_readme/Columnas1.png)
![Columnas1-10](https://github.com/silviaherf/data-cleaning-pandas/blob/master/Images_readme/Columnas2.png)


* Jupyer Notebook: aplicación escogida para desarrollar el código que nos permitirá llevar a cabo el proyecto


## Estructura del repositorio

* README.txt: El repositorio cuenta con este archivo resumen del trabajo realizado
* Sharks_analysis.ipynb: Archivo Jupyer Notebook que contiene el script del proyecto

* Input: Contiene la información de partida. En este caso, se incluye el archivo CSV que no se ha publicado en Github
* src: Contiene archivos necesarios para el código. En este caso, incluye un archivo functions.py borrador, que finalmente no se ha utilizado durante el scripting
* Output: Contiene la información de salida del código. Para el proyecto que nos ocupa, se trata fundamentalmente de tablas y gráficos de pandas
* zz_trash: Contiene versiones obsoletas de archivos del proyecto. En este caso, está vacía

## Hipótesis a validar
1. En los años más recientes, la mortalidad en los ataques ha descendido
2. El mayor número de ataques en la historia se ha dado en hombres, aunque en más ocasiones las mujeres fallecen¶


## Desarrollo del proyecto
1. Revisión de los datos disponibles y su limpieza. 
Apertura del archivo CSV con pandas. El dataframe de partida tiene 25723 filas y 24 columnas de información que, en un gran número de casos, contiene datos erróneos o vacíos.
Sobre las columnas, en primer lugar se han renombrado evitando espacios en blanco y nombres excesivamente largos, como los de partida, para que sea más fácil su manejo en Python.
Por otra parte, se ha observado que existen dos columnas 'Unnamed:22' y 'Unnamed:23' cuyos campos se encuentran vacíos en prácticamente todas las filas. Se ha optado por no integrar esas columnas para el análisis. Además, existen columnas con datos que no aportan información para validar las hipótesis, como son 'pdf', 'href', entre otras, por lo que tampoco se seleccionarán en el "df_clean" (dataFrame limpio) para el análisis.
El resultado es un dataFrame de 15 columnas del siguiente tipo:

![df_clean](https://github.com/silviaherf/data-cleaning-pandas/blob/master/Images_readme/15_columnas_limpias.png)

Aun con todo, siguen quedando columnas con una media de 19.000 valores vacíos (NaN) entre sus datos.
Por ello, se comienza eliminando las filas con todos sus datos NaN con dropna(how='all).
El siguiente paso ha sido eliminar valores de filas duplicadas con el método de pandas drop.duplicates()
Y, viendo que 'Case' tiene 3000 datos no nulos más que el resto de filas, se ejecuta el mismo método para todas las columnas a excepción de 'Case'.
El resultado es un dataset de 6222 filas y 10 columnas.

![df_clean](https://github.com/silviaherf/data-cleaning-pandas/blob/master/Images_readme/6000filas.png)


