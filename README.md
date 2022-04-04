# unir-cb-algoritmos-geneticos

Implementación de un algoritmo genético no visto en clase.

## Introducción

Para la presente práctica se ha implementado el algoritmo basado en inteligencia de enjambre Algoritmo Genético.

El Algoritmo Genético (AG), presentado por John Holland en 1975, es un algoritmo de optimización de búsqueda basado en la mecánica del proceso de selección natural. El concepto básico de este algoritmo es imitar el concepto de "supervivencia del más apto": simula los procesos observados en un sistema natural donde el fuerte tiende a adaptarse y sobrevivir mientras que el débil tiende a perecer. (Ab Wahab, Nefti-Meziani, & Atyabi, 2015)

## Breve descripción del Algoritmo Genético

El AG utiliza una población en la que sus miembros se clasifican según la aptitud de sus soluciones. En cada generación se seleccionan los individuos más aptos para generar hijos utilizando operaciones genéticas como selección, reproducción, intercambio de genes y mutación.
La carga genética de cada individuo se codifica de la forma que mejor se adapte al dominio del problema que se está intentando solucionar y el desarrollador siempre ha de proporcionar formas -léase, funciones- que permitan evaluar la aptitud de un individuo y crear nuevos hijos a partir de dos especímenes utilizando intercambio de genes y mutación.

El AG comienza con una primera generación de un tamaño de población predeterminado y cada individuo se crea con una carga genética aleatoria. A partir de este punto, para cada generación, se calcula la aptitud de cada espécimen, cada sujeto se compara con otros k elementos aleatorios (se dice que participa en un torneo), se escoge el mejor de cada torneo (puede haber especímenes repetidos) y se crea una nueva generación a partir de estos, emparejados aleatoriamente. Se repite el proceso durante un número de iteraciones preestablecido.

Cuando se emparejan dos especímenes, se crean nuevos individuos alternando secciones completas de cada uno de los progenitores. Existe una probabilidad de intercambio, normalmente bastante alta. Esto permite que, en algunos pocos casos, los padres pasen a la siguiente generación sin ningún intercambio genético. A continuación, se aplican posibles alteraciones aleatorias, aplicando una probabilidad de mutación, normalmente bastante baja.

## Implementación básica

Para implementar el Algoritmo Genético utilizaremos un tutorial que muestra cómo programar un algoritmo genético en Python (Brownlee, 2021).

El problema inicial es el siguiente: encontrar los valores de los genes que maximicen la suma de sus valores. Los genes tienen valor binario, 1 o 0, por lo que se trata de encontrar el genoma que tiene cuantos más unos mejor.

La implementación inicial utiliza los siguientes hiperparámetros:

- Número de iteraciones: 100
- Número de bits (genes dentro del cromosoma): 20
- Tamaño de la población: 100
- Probabilidad de intercambio: 90%
- Probabilidad de mutación: 1 / número de bits = 5%

No se parametriza el número k de individuos que compiten entre sí para pasar a la siguiente generación, que tiene el valor fijo k = 3.

El código puede encontrarse en la siguiente URL: [ag_base_todo_unos.py](./blob/master/ag_base_todo_unos.py).

El resultado es el siguiente:

```
$ python3 ag_base_todo_unos.py
>0, new best f([0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]) = 0.077
>0, new best f([1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1]) = 0.067
>2, new best f([1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]) = 0.062
>3, new best f([1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]) = 0.059
>4, new best f([1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 0.056
>5, new best f([1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 0.053
>9, new best f([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 0.050
Done!
f([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) = 0.050000
```

Recuérdese que la función de aptitud devuelve el inverso de la suma, porque el algoritmo está implementado para minimizar el valor, por lo que 1 / 20 = 0.05.

## Implementación más compleja

El tutorial en el que se basa esta implementación propone a continuación una versión más compleja, en la que se ha de encontrar el valor mínimo de una función de segundo grado.

Para hacer algo un poco más realista, pero constando que nunca he utilizado este tipo de algoritmos en el mundo real, me he propuesto realizar los siguientes cambios:

 -	El programa debe ser capaz de encontrar la solución a una combinación de un número variable de ecuaciones. Esto podría, a mi parecer, ser útil si lo que queremos evaluar depende de diversas variables cuyos valores no están correlados. Un ejemplo sería una flota de camiones, en la que el peso de un nodo (lo que queremos calcular) depende de la longitud, del tipo de vía, de la densidad de tráfico esperada, del consumo promedio del vehículo, etc.

 -	Parametrizar k, solo para poder jugar con su valor.

Una vez realizados los cambios, se crean tres funciones cualesquiera para que el programa encuentre el valor de x que minimiza todas ellas. Las funciones, con sus gráficas y los x que minimizan sus valores son:

- Función 1
  
  `f1(x) = 6x**4 + 20x**3 - 5x`

  ![Graph 1](./img/graph1.png?raw=true)

  `x` aprox. que minimiza `f1(x)`: `-2.5`

- Función 2

  `f2(x) = 3x`

  ![Graph 2](./img/graph2.png?raw=true)

  `x` aprox. que minimiza `f2(x)`: `-infinito`

- Función 3

  `f3(x) = 2x**4 - 10x**3 +3x**2 -5x`

  ![Graph 3](./img/graph3.png?raw=true)

  `x` aprox. que minimiza `f3(x)`: `3.6`

- Función combinada

  `f4(x) = f1(x) + f2(x) + f3(x)`
  
  `f4(x) = 8x**4 + 10x**3 + 3x**2 - 7x`

  ![Graph 4](./img/graph4.png?raw=true)

  `x` aprox. que minimiza `f4(x)`: `0.35`

### Versión 1: tres valores

Este programa se puede encontrar en la URL [ag_tres_valores.py](./blob/master/ag_tres_valores.py).

En la primera versión del programa, no sé en qué estaba pensando. Ahora es evidente que, si busco el valor, un único valor, de x que minimiza una función, entonces el cromosoma de cada individuo debe contener únicamente ese posible valor de x.

Pero en un inicio, al tratarse de tres funciones, cada individuo tenía un cromosoma de 60 bits que representaban tres números enteros sin signo, cada uno de 20 bits, con valores posibles entre 0 y 220-1.

Cada uno de estos valores se convertía posteriormente a un número real dentro de un rango que, en este caso, vistas las gráficas y mínimos de las funciones anteriores, era [-5, 5].

Estas son las definiciones específicas del problema:

```python
def func1(x):
    return 6.0 * x**4 + 20.0 * x**3 - 5 * x 

def func2(x):
    return 3 * x 

def func3(x):
    return 2.0 * x**4 - 10.0 * x**3 + 3.0 * x**2 - 5.0 * x 

def objective(values):
    return func1(values[0]) + func2(values[0]) + func3(values[0])

n_values = 1
n_bits = n_values * [20]
rangos = n_values * [[-5.0, 5.0]]
```

El resultado de la ejecución del programa es el siguiente (como el número de iteración de la mejor solución se acercaba sospechosamente a 100, se aumentó el número de iteraciones hasta 200):

```
$ python3 ag_tres_valores.py
>0, new best f([-2.165431, 4.167385, 4.256896]) = -129.390177
>0, new best f([-2.408609, -3.046817, 3.707103]) = -183.667771
>4, new best f([-2.576999, -4.846992, 3.850269]) = -185.345501
>5, new best f([-2.575950, -4.895114, 3.709545]) = -188.490978
>5, new best f([-2.585620, -4.850263, 3.621482]) = -188.883220
>6, new best f([-2.585620, -4.850263, 3.619041]) = -188.890834
>7, new best f([-2.498130, -4.895267, 3.709545]) = -189.330635
>7, new best f([-2.538566, -4.869480, 3.632011]) = -189.597610
>8, new best f([-2.528162, -4.861621, 3.549957]) = -189.693748
>9, new best f([-2.497978, -4.908552, 3.631114]) = -190.035172
>12, new best f([-2.498111, -4.919567, 3.632621]) = -190.061071
[ . . . ]
>49, new best f([-2.465171, -4.999990, 3.593873]) = -190.471147
>50, new best f([-2.465629, -4.999990, 3.593873]) = -190.471168
>52, new best f([-2.465629, -4.999990, 3.593797]) = -190.471201
>54, new best f([-2.465162, -5.0, 3.593797]) = -190.471207
>58, new best f([-2.465696, -5.0, 3.593797]) = -190.471230
>68, new best f([-2.465610, -5.0, 3.59375]) = -190.471249
>75, new best f([-2.465763, -5.0, 3.59375]) = -190.471250
>79, new best f([-2.465753, -5.0, 3.59375]) = -190.471250
>89, new best f([-2.465715, -5.0, 3.59375]) = -190.471250
>99, new best f([-2.465724, -5.0, 3.59375]) = -190.471250
>193, new best f([-2.465734, -5.0, 3.59375]) = -190.471250
Done!
f([-2.465734, -5.0, 3.59375]) = -190.471250
```

Para mi sorpresa, ¡el programa no ha encontrado la mejor x para la función combinada, sino cada una de las mejores x para cada una de las funciones base!

Recordemos que las soluciones aproximadas mirando las gráficas eran, respectivamente, -2.5, -infinito (al acotar los resultados al rango [-5, 5], el resultado es -5) y 3.6.

Este, definitivamente, no es el resultado esperado, pero mirando atentamente el código comprendo cómo ha llegado hasta él el programa.

Lo normal habría sido no incluir este intento “fallido” en la actividad, y pasar directamente a la solución correcta. Pero creo que esta implementación podría ser útil en situaciones paras las que se quiera encontrar muchos factores, multiplicadores o pesos dentro de una función; por ejemplo, en una regresión lineal con numerosas variables. O para optimizar los pesos de las entradas de un nivel de neuronas en una red neuronal.

### Versión 2: un único valor

Este programa se puede encontrar en la URL [ag_un_valor.py](./blob/master/ag_un_valor.py).

Ahora sí, se crea un cromosoma que representa un único entero sin signo de 20 bits, que posteriormente se convertirá a un número dentro del rango [-5, 5].

Solo cambian la función objective y n_values:

```python
def objective(values):
    return func1(values[0]) + func2(values[0]) + func3(values[0])

n_values = 1
```

El resultado de la ejecución del nuevo programa es la siguiente:

```
$ python3 ag_un_valor.py
>0, new best f([2.9681968688964844]) = 888.113019
>0, new best f([2.8617191314697266]) = 775.429890
>0, new best f([1.2843513488769531]) = 38.912684
>0, new best f([-1.3319587707519531]) = 16.195433
>0, new best f([-0.4431629180908203]) = 3.129541
>0, new best f([0.27194976806640625]) = -1.436897
>0, new best f([0.39711952209472656]) = -1.481488
>1, new best f([0.3605461120605469]) = -1.529969
>1, new best f([0.3524494171142578]) = -1.533223
>4, new best f([0.3447151184082031]) = -1.533939
>5, new best f([0.34483909606933594]) = -1.533945
>5, new best f([0.34745216369628906]) = -1.533949
>6, new best f([0.34531593322753906]) = -1.533966
>7, new best f([0.3459453582763672]) = -1.533979
>9, new best f([0.34605979919433594]) = -1.533980
>12, new best f([0.3462791442871094]) = -1.533980
>19, new best f([0.34618377685546875]) = -1.533980
Done!
f([0.34618377685546875]) = -1.533980
```

En este caso, el resultado es el esperado, aprox. 0.35.

## Efectos de los cambios en los hiperparámetros

Cambiando los hiperparámetros, he podido observar lo siguiente:

-	Reducir la probabilidad de intercambio o aumentar la probabilidad de mutación reducen la eficiencia del algoritmo, haciendo que converja más tarde. Con el problema que se está tratando en esta actividad, no he podido comprobar si esta situación es aceptable, ya que se podría encontrar una solución mejor.

-	Al aumentar k mejora la eficiencia del programa. Con k = 3, tarda unas 20 iteraciones en encontrar la mejor solución, mientras que con k = 10 tarda unas 8 iteraciones. Esto se debe a que los individuos peor adaptados tienen menos probabilidades de ganar en grupos con más elementos. ¿Qué es más fácil, ganar un campeonato deportivo local, nacional o mundial?
  Valores de k muy altos (50% o 75% del tamaño de la población) han generado a veces soluciones muy rápidas, mientras que otras veces se han acercado al límite de iteraciones. Esto se puede deber a que al preferir los especímenes más prometedores se ignoran otros que en un futuro, gracias a las combinaciones y mutaciones, pueden dar lugar a soluciones mejores. ¡Como la genética real!

## Posibles mejoras

Para la presente actividad se ha escogido una implementación muy sencilla. Como todos los algoritmos de inteligencia de enjambre, se puede optimizar de numerosas formas. En este caso, aun no siendo un experto en la materia, algunas optimizaciones que se ocurren son:

-	Detener el bucle si el mejor resultado no cambia después de n iteraciones. El beneficio es evidente: converger antes. Pero se podrían dejar de obtener mejores soluciones en algunos casos (los menos, a mi parecer, si se escoge bien el valor del parámetro).

-	Que cada pareja genere más de dos hijos. No muchos más, 3 o 4. Después se descartarían los peor adaptados para quedarse con el tamaño de población estipulado antes de pasar a los torneos. El posible beneficio es descartar los peores prospectos directamente. Un inconveniente es el coste computacional.

-	En vez de emparejar a los ganadores de los torneos aleatoriamente, emparejar al mejor con el segundo, al tercero con el cuarto, y así hasta el penúltimo con el último.

-	Almacenar soluciones descartadas (utilizando un hash único para cada una de ellas) para evitar reevaluaciones innecesarias. Habría que evaluar si el coste de implementar esta optimización (en tiempo y espacio) compensa el tiempo ahorrado.

-	Después de cada evaluación y antes de los torneos, desestimar los peores n miembros de la población y sustituirlos por los n mejores miembros de la generación anterior. Esto podría ayudar a encontrar la mejor solución más rápido.

## Referencias

- Ab Wahab, M. N., Nefti-Meziani, S., & Atyabi, A. (2015, mayo 18). A Comprehensive Review of Swarm Optimization Algorithms. Retrieved abril 3, 2022, from Plos One: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0122827

- Brownlee, J. (3 de marzo de 2021). Simple Genetic Algorithm From Scratch in Python. Recuperado el 3 de abril de 2022, de Simple Genetic Algorithm From Scratch in Python: https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/
