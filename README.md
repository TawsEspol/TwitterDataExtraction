# Práctica: Twitter Data Extraction II #

- **Facilitador:** [Leonardo Kuffo](https://github.com/lkuffo/)
- **Fecha:** 6/16/2017

## Descripción ##

En este taller aprendimos como extraer datos de Twitter utilizando Tweepy. Vimos algunos metodos disponibles en el API REST de Twitter. Para afianzar los conocimientos aprendidos se propone la practica aqui expuesta. Recuerde que en [la documentacion de Tweepy](http://docs.tweepy.org/en/v3.5.0/index.html) puede encontrar muchos metodos adicionales a los que hemos visto.


## Práctica ##

Para la realización de la practica se les ha proporcionado dos scripts incompletos, los cuales usted tendra que completar.

### Parte 1: Manejar Twitter desde Tweepy ###

Muchas aplicaciones tuitean automaticamente por los usuarios. Esto lo realizan utilizando el API de Twitter. En esta primera parte usted tiene que realizar lo siguiente:
- Twitee en su cuenta desde Tweepy.
- ~~Dele ReTweet al Tweet que acaba de crear desde Tweepy.~~
- ~~Elimine el tweet que acaba de crear desde Tweepy.~~

### Parte 2: Analizando Texto ###

Muchas veces nos preguntamos de que hablan en general un conjunto de Tweets. Existen muchas tecnicas de analisis sofisticado para poder determinar topicos y emociones dentro de mucho texto. El dia de hoy, vamos a utilizar una tecnica muy simple y efectiva para poder tener una retrospectiva rapida de que esta hablando un texto: Realizar un **WordCloud**. Un WordCloud o nube de palabras, es una imagen que contiene las palabras presentes en el texto, y el tamano de la palabra representa que tan frecuente es la palabra dentro del texto.

Para esto se le ha proporcionado un script incompleto que procesa el texto de tal manera que sea apto para el analisis, usted  tiene que copiar y pegar el texto de esos tweets en [esta pagina](https://www.jasondavies.com/wordcloud/). En esa pagina usted podra genera un WordCloud a partir del texto que se le ingrese.

- Extraiga todo el timeline de un usuario en especifico, el que usted desee. Utilice el [generador de WordClouds](https://www.jasondavies.com/wordcloud/) para analizar el texto obtenido.
- ~~Extraiga tweets de una busqueda. Utilice el [generador de WordClouds](https://www.jasondavies.com/wordcloud/) para analizar el texto obtenido.~~

### Parte 3: Analisis Temporal ###
- ~~Extraiga todo el timeline de un usuario en especifico, el que usted desee. Y determine a que hora del dia esta persona tuitea mas.~~
- ~~Extraiga todo el timeline de un usuario en especifico, el que usted desee. Y determine que dia de la semana esta persona tuitea mas.~~
- ~~De ambos literales, muestre graficos que le permitan analizar mejor los datos.~~


### Parte 4: Analisis Espacial - Visualizacion ###
Usted va a completar y utilizar el script `parte4.1`, para poder sacar tweets en tiempo real utilizando el parametro locations, y almacene los tweets en una coleccion de MongoDB. En [esta pagina](http://boundingbox.klokantech.com/) puede generar Bounding Boxes de manera facil. En la parte de abajo, seleccione CSV RAW.

Luego, completando el script `parte4.2`, usted tiene que generar un archivo que tenga el siguiente formato:
> latitud,longitude

> 40.166,-105.15

> 38.9833,-121.15

> ...,...

El cual contiene las coordenadas de latitud y longitud de sus tweets. Recuerde que no todos los tweets que baje poseen este atributo.

Luego, ingrese a [CARTO](https://carto.com/), y cree una cuenta con GitHub o Google. Una vez ingresado al dashboard, cargue el dataset, genere una visualizacion y realice conclusiones sobre la misma.
