PAV - P3: estimación de pitch
=============================

Esta práctica se distribuye a través del repositorio GitHub [Práctica 3](https://github.com/albino-pav/P3).
Siga las instrucciones de la [Práctica 2](https://github.com/albino-pav/P2) para realizar un `fork` de la
misma y distribuir copias locales (*clones*) del mismo a los distintos integrantes del grupo de prácticas.

Recuerde realizar el *pull request* al repositorio original una vez completada la práctica.

Ejercicios básicos
------------------

- Complete el código de los ficheros necesarios para realizar la estimación de pitch usando el programa
  `get_pitch`.

   * Complete el cálculo de la autocorrelación e inserte a continuación el código correspondiente.
   
   	```c
    	void PitchAnalyzer::autocorrelation(const vector<float> &x, vector<float> &r) const {

    	for (unsigned int l = 0; l < r.size(); ++l) {
  		/// \TODO Compute the autocorrelation r[l]
      		/// \DONE Implementado el calculo de la autocorrelación
      
      	r[l]=0;
      	for (unsigned int n = 0; n < (x.size()-l); ++n) {
        	r[l] =x[n]*x[n+l] + r[l];
      	}
      	r[l] /= x.size();
    	}

    	if (r[0] == 0.0F) //to avoid log() and divide zero 
      		r[0] = 1e-10; 
  	}
   	```
   
   **`
   El cálculo de la autocorrelación es la correlacion de la señal consigo misma y desplazada. Realizamos la convolución, haciendo el producto para cada muestra y finalmente dividimos el resultado por el número total de muestras de la señal.
   `**

   * Inserte una gŕafica donde, en un *subplot*, se vea con claridad la señal temporal de un segmento de
     unos 30 ms de un fonema sonoro y su periodo de pitch; y, en otro *subplot*, se vea con claridad la
	 autocorrelación de la señal y la posición del primer máximo secundario.

	 NOTA: es más que probable que tenga que usar Python, Octave/MATLAB u otro programa semejante para
	 hacerlo. Se valorará la utilización de la biblioteca matplotlib de Python.
	 
	 Código de Matlab
	 
	```c
	[y, Fs] = audioread("fonema_sonoro_a_30ms.wav");
	delta_t = 1/Fs;
	t=0:delta_t:((length(y)-1)*delta_t);
	subplot(2,1,1)
	 plot(t,y);
	 xlabel("Segundos");
	 ylabel("Amplitud");
	 title("Señal de 30 ms");
	 subplot(2,1,2)
	 a=xcorr(y);
	 plot(a);
	 xlabel("Muestras");
	 ylabel("Amplitud");
	 title("Autocorrelación");
	 ```
	 
	
	En esta función, se lee una señal de aproximadamente 30 ms de un fonema sonoro, en este caso la a, 
	finalmente se hace un plot de la señal temporal, así como de su autocorrelación.
	A continuación se muestra las gráficas:
	
	<img src="img/matlab.png" width="640" align="center">
	
	<img src="img/periodos_señal.png" width="640" align="center">
	
	**`
	Como se puede observar en el dominio temporal, hay una periodicidad de 
	8,125ms, por lo que el pitch es aproximadamente 123,07Hz.
	Mientras que en la autocorrelación, observamos un periodo de 130 muestras, que corresponde  a un pitch de 123,07Hz, observamos por lo tanto, como coincide.
	`**
 

   * Determine el mejor candidato para el periodo de pitch localizando el primer máximo secundario de la
     autocorrelación. Inserte a continuación el código correspondiente.
     
		<img src="img/mejor candidato.png" width="640" align="center">
		
	
   * Implemente la regla de decisión sonoro o sordo e inserte el código correspondiente.

		Primero implementamos una función básica (desarrollada en clase) para detectar si era sordo 
		o sonoro a partir de la comprobación de un umbral fijo utilizando un simple if().
	
		Esto es bastante mejorable para tener una mejor detección, y hemos implementado esta segunda 
		versión a partir de la comprobación de la potencia y las autocorrelación normalizadas
		(parámetros que recibimos de la cabecera). *Usamos el umbral umaxnorm = 0.51*
	
		<img src="img/regla de decisión.png" width="640" align="center">
	
	
	
   * Puede serle útil seguir las instrucciones contenidas en el documento adjunto `código.pdf`.

- Una vez completados los puntos anteriores, dispondrá de una primera versión del estimador de pitch. El 
  resto del trabajo consiste, básicamente, en obtener las mejores prestaciones posibles con él.

  * Utilice el programa `wavesurfer` para analizar las condiciones apropiadas para determinar si un
    segmento es sonoro o sordo. 
	
	  - Inserte una gráfica con la estimación de pitch incorporada a `wavesurfer` y, junto a ella, los 
	    principales candidatos para determinar la sonoridad de la voz: el nivel de potencia de la señal
		(r[0]), la autocorrelación normalizada de uno (r1norm = r[1] / r[0]) y el valor de la
		autocorrelación en su máximo secundario (rmaxnorm = r[lag] / r[0]).

		Puede considerar, también, la conveniencia de usar la tasa de cruces por cero.

	    Recuerde configurar los paneles de datos para que el desplazamiento de ventana sea el adecuado, que
		en esta práctica es de 15 ms.
		
		//
		
		Para obtener los datos de autocorrealciones normalizadas y máximas (r1norm y rmaxnorm), 
		utilizamos la señal de train rl010.wav de donde extraemos los datos para la autocorrelación un fichero .out
		que nos permitirá poder separar en los dos tipos de autocorrelaciones deseadas.
		Utilizamos el comando cut para extraer los datos y hacer dos ficheros separados que introduciremos
		posteriormente en el wavesurfer:
		
		<img src="img/creacion archivos pot.png" width="640" align="center">
		

      - Use el estimador de pitch implementado en el programa `wavesurfer` en una señal de prueba y compare
	    su resultado con el obtenido por la mejor versión de su propio sistema.  Inserte una gráfica
		ilustrativa del resultado de ambos estimadores.
     
		Aunque puede usar el propio Wavesurfer para obtener la representación, se valorará
	 	el uso de alternativas de mayor calidad (particularmente Python).
  
  * Optimice los parámetros de su sistema de estimación de pitch e inserte una tabla con las tasas de error
    y el *score* TOTAL proporcionados por `pitch_evaluate` en la evaluación de la base de datos 
	`pitch_db/train`..

Ejercicios de ampliación
------------------------

- Usando la librería `docopt_cpp`, modifique el fichero `get_pitch.cpp` para incorporar los parámetros del
  estimador a los argumentos de la línea de comandos.
  
  Esta técnica le resultará especialmente útil para optimizar los parámetros del estimador. Recuerde que
  una parte importante de la evaluación recaerá en el resultado obtenido en la estimación de pitch en la
  base de datos.

  * Inserte un *pantallazo* en el que se vea el mensaje de ayuda del programa y un ejemplo de utilización
    con los argumentos añadidos.

- Implemente las técnicas que considere oportunas para optimizar las prestaciones del sistema de estimación
  de pitch.

  Entre las posibles mejoras, puede escoger una o más de las siguientes:

  * Técnicas de preprocesado: filtrado paso bajo, diezmado, *center clipping*, etc.
  * Técnicas de postprocesado: filtro de mediana, *dynamic time warping*, etc.
  * Métodos alternativos a la autocorrelación: procesado cepstral, *average magnitude difference function*
    (AMDF), etc.
  * Optimización **demostrable** de los parámetros que gobiernan el estimador, en concreto, de los que
    gobiernan la decisión sonoro/sordo.
  * Cualquier otra técnica que se le pueda ocurrir o encuentre en la literatura.

  Encontrará más información acerca de estas técnicas en las [Transparencias del Curso](https://atenea.upc.edu/pluginfile.php/2908770/mod_resource/content/3/2b_PS%20Techniques.pdf)
  y en [Spoken Language Processing](https://discovery.upc.edu/iii/encore/record/C__Rb1233593?lang=cat).
  También encontrará más información en los anexos del enunciado de esta práctica.

  Incluya, a continuación, una explicación de las técnicas incorporadas al estimador. Se valorará la
  inclusión de gráficas, tablas, código o cualquier otra cosa que ayude a comprender el trabajo realizado.

  También se valorará la realización de un estudio de los parámetros involucrados. Por ejemplo, si se opta
  por implementar el filtro de mediana, se valorará el análisis de los resultados obtenidos en función de
  la longitud del filtro.
   

Evaluación *ciega* del estimador
-------------------------------

Antes de realizar el *pull request* debe asegurarse de que su repositorio contiene los ficheros necesarios
para compilar los programas correctamente ejecutando `make release`.

Con los ejecutables construidos de esta manera, los profesores de la asignatura procederán a evaluar el
estimador con la parte de test de la base de datos (desconocida para los alumnos). Una parte importante de
la nota de la práctica recaerá en el resultado de esta evaluación.
