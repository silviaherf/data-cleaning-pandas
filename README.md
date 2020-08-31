## Proyecto de Data analytics con pandas - Bootcamp Fulltime de Data Anlytics de Ironhack's

![Ironhack logo](https://www.fundacionuniversia.net/wp-content/uploads/2017/09/ironhack_logo.jpg)

## Resumen del proyecto

Este proyecto consiste en la limpieza y manipulación de los datos contenidos en un archivo CSV con Python, relativo a los ataques de tiburones en el mundo a lo largo de la historia. Asumidas dos hipótesis propias, se trata de validar la veracidad de las mismas a través de los datos.

En este caso, el archivo CSV de origen no se ha subido a Github, a solicitud de su autor.

![Tiburon](https://www.ngenespanol.com/wp-content/uploads/2018/08/%C2%BFPor-qu%C3%A9-disminuy%C3%B3-el-riesgo-de-ataques-de-tibur%C3%B3n-770x413.jpg)


## Recursos utilizados

* Dataset: Archivo CSV con el histórico de ataques de tiburón en el mundo. Se trata de un archivo de 25723 filas y 24 columnas de información:
![Columnas1-10](Images_readme/Columnas1.png)
![Columnas1-10](Images_readme/Columnas2.png)


* Jupyer Notebook: aplicación escogida para desarrollar el código que nos permitirá llevar a cabo el proyecto


## Estructura del repositorio

* README.txt: El repositorio cuenta con este archivo resumen del trabajo realizado
* Sharks_analysis.ipynb: Archivo Jupyer Notebook que contiene el script del proyecto

* Input: Contiene la información de partida. En este caso, se incluye el archivo CSV que no se ha publicado en Github
* src: Contiene archivos necesarios para el código. En este caso, incluye un archivo functions.py borrador, que finalmente no se ha utilizado durante el scripting
* Output: Contiene la información de salida del código. Para el proyecto que nos ocupa, se trata fundamentalmente de tablas y gráficos de pandas
* zz_trash: Contiene versiones obsoletas de archivos del proyecto. En este caso, está vacía

## Hipótesis a validar
1. El mayor número de ataques en la historia se ha dado en hombres, aunque en más ocasiones las mujeres fallecen. En los años más recientes, la mortalidad en los ataques ha descendido. 
2. La mayor parte de los ataques fueron producidos a surfistas


## Desarrollo del proyecto
## 1. Revisión de los datos disponibles y su limpieza. 
Apertura del archivo CSV con pandas. El dataframe de partida tiene 25723 filas y 24 columnas de información que, en un gran número de casos, contiene datos erróneos o vacíos.

Sobre las columnas, en primer lugar se han renombrado evitando espacios en blanco y nombres excesivamente largos, como los de partida, para que sea más fácil su manejo en Python.

Por otra parte, se ha observado que existen dos columnas 'Unnamed:22' y 'Unnamed:23' cuyos campos se encuentran vacíos en prácticamente todas las filas. Se ha optado por no integrar esas columnas para el análisis. 

Además, existen columnas con datos que no aportan información para validar las hipótesis, como son 'pdf', 'href', entre otras, por lo que tampoco se seleccionarán en el "df_clean" (dataFrame limpio) para el análisis.

El resultado es un dataFrame de 15 columnas del siguiente tipo:

![df_clean15](Images_readme/15_columas_limpias.png)

Aun con todo, siguen quedando columnas con una media de 19.000 valores vacíos (NaN) entre sus datos.

Por ello, se comienza eliminando las filas con todos sus datos NaN con dropna(how='all).

El siguiente paso ha sido eliminar valores de filas duplicadas con el método de pandas drop.duplicates()

Y, viendo que 'Case' tiene 3000 datos no nulos más que el resto de filas, se ejecuta el mismo método para todas las columnas a excepción de 'Case'.
El resultado es un dataset de 6222 filas y 10 columnas.

![df_clean6000](Images_readme/6000filas.png)


## 2. Validando la hipótesis 1: El mayor número de ataques en la historia se ha dado en hombres, aunque en más ocasiones las mujeres fallecen. En los años más recientes, la mortalidad en los ataques ha descendido.
Puesto que es algo que vamos a necesitar más adelante, vamos a arreglar los valores de la columna "Sex", que únicamente cuenta con errores de inserción en 6 filas. Puesto que son tan pocos valores, hemos revisado estas filas una a una.

En los casos en que el género se puede intuir de la columna 'Name', se ha sustituido el valor de 'Sex' por su valor correcto. Es una simple asignación.
Cuando no ha sido posible asignar un género a la columna 'Sex', bien porque el accidente es para un grupo mixto, o porque no se tienen datos para ello, se ha prescindido de esos valores, por ser tan poco representativos.

Se observa que siguen quedando valores donde la columna sexo es null. En principio no podemos rellenarla con la información disponible, por lo que para validar la hipótesis, no se tendrán en cuenta en los totales (value_counts no cuenta los valores NaN)

A continuación, limpiamos los valores de la columna 'Fatal', de forma análoga a lo realizado en 'Sex'. En este caso, en lugar de valores  null, aparece 'UNKNOWN'. Tampoco se utilizarán para sacar conclusiones. Además, de la columna 'Injury', se ha podido localizar accidentes mortales ('Fatal') y asignar el correspondientes 'Y' en la columna 'Fatal', todo ello con regex.

Por último, para validar esta hipótesis en su segunda teoría, antes es necesario poner en orden la columna "year", pues lo que se pretende es agrupar por años los accidentes sufridos, hayan sido mortales o no. Como en los casos anteriores, se ha buscado una forma de completar los valores erróneos o nulos con regex, en este caso sirviéndonos de la columna 'Date'.

Mediante el método groupby() de pandas, y con los intervalos temporales que nos ha interesado, hemos podido cruzar los datos necesarios para la comprobación de la hipótesis, de la siguiente manera:

* Ataques de tiburón por rango temporal y género:

![tabla_actividades](output/1-tabla_gen_fatal_años.png)
![tabla_actividades](output/2-barras_genero_años.png)

* Mortalidad en los ataques de tiburón y su evolución temporal:

![tabla_actividades](output/3-tabla_porcentaje_años.png)
![tabla_actividades](output/4-porcentaje_fatal_años.png)

* Mortalidad en los ataques de tiburón por género en la historia:

![tabla_actividades](output/5-barras_genero_fatal.png)
![tabla_actividades](output/6-tabla_gen_fatal_porcentaje.png)


Por lo que **la hipótesis 1 es errónea en sus dos teorías**

## 3. Validando la hipótesis 2: La mayor parte de los ataques fueron producidos a surfistas
En analogía al apartado anterior, en este caso será necesario depurar la columna 'Activity' para poder contabilizar los casos ocurridos en cada actividad.
En este caso, los problemas que nos encontramos en esta columna son de errores de inserción (palabras escritas de forma incorrecta, frases que contienen la palabra clave,etc.), por lo que con regex podemos renombrar según nuestro interés esos datos.

Ordenando de mayor  a menos el total de casos para las 5 actividades principales, se obtiene lo siguiente:

![tabla_actividades](output/7-tabla_actividades.png)


Por lo que **la hipótesis 2 es errónea**
