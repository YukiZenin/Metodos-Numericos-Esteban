## Interpolación Lineal



### Teoría y Fundamentación Matemática
La interpolación es un método numérico utilizado para estimar valores desconocidos que se encuentran **dentro** del rango de un conjunto de datos discretos conocidos. 

La **interpolación lineal** es la forma más simple de interpolación. Consiste en asumir que entre dos puntos de datos adyacentes la función se comporta como una **línea recta**. Matemáticamente, esto equivale a unir dos puntos con un polinomio de primer grado.

Este método es muy rápido y fácil de calcular, pero su precisión depende directamente de dos factores:
1. La naturaleza de la función original (si es muy curva, la línea recta será una mala aproximación).
2. La distancia entre los puntos de datos (cuanto más cerca estén los puntos $x_0$ y $x_1$, más se parecerá la recta a la curva real, disminuyendo el error de truncamiento).

### Fórmulas y Criterios
Dados dos puntos conocidos $(x_0, y_0)$ y $(x_1, y_1)$, queremos estimar el valor de $y$ para un valor dado $x$ (donde $x_0 < x < x_1$).

Utilizando la relación de triángulos semejantes o la ecuación de la recta (punto-pendiente), la fórmula de interpolación lineal se define como:
$$f_1(x) = y_0 + \frac{y_1 - y_0}{x_1 - x_0} (x - x_0)$$

Donde:
* $f_1(x)$ es el valor interpolado (el subíndice 1 indica que es un polinomio de primer grado).
* El término $\frac{y_1 - y_0}{x_1 - x_0}$ representa la pendiente de la recta que une a los dos puntos.

### Ejercicio Resuelto
**Enunciado:** Estima el valor del logaritmo natural de 2, $\ln(2)$, utilizando interpolación lineal. Para ello, utiliza los puntos conocidos $x_0 = 1$ y $x_1 = 4$. Compara tu resultado con el valor real para calcular el error.

**Solución paso a paso:**
**1. Identificar los datos conocidos:**
   Sabemos que $f(x) = \ln(x)$. Extraemos nuestros puntos:
   * $x_0 = 1 \implies y_0 = \ln(1) = 0$
   * $x_1 = 4 \implies y_1 = \ln(4) \approx 1.386294$
   * Valor a interpolar: $x = 2$

**2. Sustituir en la fórmula de interpolación lineal:**
   $$f_1(2) = 0 + \frac{1.386294 - 0}{4 - 1} (2 - 1)$$

**3. Resolver las operaciones:**
   Calculamos la pendiente y multiplicamos por la distancia:
   $$f_1(2) = \frac{1.386294}{3} (1)$$
   $$f_1(2) = 0.462098$$

**Conclusión:** La aproximación por interpolación lineal nos da un valor de $0.462098$. El valor analítico real de $\ln(2)$ es aproximadamente $0.693147$. 
La diferencia es notable (un error grande). Esto ocurre porque el logaritmo natural tiene una curvatura muy pronunciada entre 1 y 4, por lo que una línea recta no se ajusta bien. Si hubiéramos usado puntos más cercanos (como $x_0 = 1.5$ y $x_1 = 2.5$), la estimación habría sido mucho más precisa.
---

## Interpolación Cuadrática



### Teoría y Fundamentación Matemática
Como vimos en la interpolación lineal, unir dos puntos con una línea recta genera un error de truncamiento considerable si la función original tiene curvas pronunciadas. Para corregir esto, la **interpolación cuadrática** utiliza **tres puntos** de datos conocidos para trazar una **parábola** (un polinomio de segundo grado) que pase exactamente por ellos.

Al emplear una curva en lugar de una recta, el polinomio se adapta mucho mejor a la forma real de la función, reduciendo drásticamente el error de estimación. La forma más común e intuitiva de construir este polinomio en métodos numéricos es utilizando el formato de los **Polinomios de Interpolación de Newton** (basado en diferencias divididas).

### Fórmulas y Criterios
Dados tres puntos conocidos $(x_0, y_0)$, $(x_1, y_1)$ y $(x_2, y_2)$, queremos estimar el valor de $y$ para un valor dado $x$.

El polinomio de interpolación cuadrática (de segundo grado) se define como:
$$f_2(x) = b_0 + b_1(x - x_0) + b_2(x - x_0)(x - x_1)$$

Para encontrar los coeficientes $b_0$, $b_1$ y $b_2$, evaluamos de forma secuencial:
1. **Coeficiente $b_0$:** Es simplemente el valor del primer punto.
   $$b_0 = y_0$$
2. **Coeficiente $b_1$:** Es la pendiente entre el primer y el segundo punto.
   $$b_1 = \frac{y_1 - y_0}{x_1 - x_0}$$
3. **Coeficiente $b_2$:** Representa la curvatura, calculando la diferencia entre las pendientes de los dos intervalos, dividida por la distancia total.
   $$b_2 = \frac{\frac{y_2 - y_1}{x_2 - x_1} - \frac{y_1 - y_0}{x_1 - x_0}}{x_2 - x_0}$$

### Ejercicio Resuelto
**Enunciado:** Vamos a mejorar el cálculo del ejercicio anterior. Estima el valor de $\ln(2)$ mediante interpolación cuadrática utilizando tres puntos: $x_0 = 1$, $x_1 = 4$ y añadiremos un tercer punto $x_2 = 6$. Compara tu resultado con el de la interpolación lineal.

**Solución paso a paso:**
**1. Identificar los datos conocidos:**
   Sabemos que $f(x) = \ln(x)$.
   * $x_0 = 1 \implies y_0 = \ln(1) = 0$
   * $x_1 = 4 \implies y_1 = \ln(4) \approx 1.386294$
   * $x_2 = 6 \implies y_2 = \ln(6) \approx 1.791759$
   * Valor a interpolar: $x = 2$

**2. Calcular los coeficientes $b$:**
   * **Para $b_0$:**
     $$b_0 = 0$$
   * **Para $b_1$:**
     $$b_1 = \frac{1.386294 - 0}{4 - 1} = \frac{1.386294}{3} = \mathbf{0.462098}$$
   * **Para $b_2$:**
     Primero calculamos la pendiente del segundo segmento: $\frac{1.791759 - 1.386294}{6 - 4} = \frac{0.405465}{2} = 0.202732$
     Ahora sustituimos en la fórmula de $b_2$:
     $$b_2 = \frac{0.202732 - 0.462098}{6 - 1} = \frac{-0.259366}{5} = \mathbf{-0.051873}$$

**3. Sustituir en la ecuación del polinomio:**
   $$f_2(2) = 0 + 0.462098(2 - 1) + (-0.051873)(2 - 1)(2 - 4)$$
   $$f_2(2) = 0 + 0.462098(1) - 0.051873(1)(-2)$$
   $$f_2(2) = 0.462098 + 0.103746$$
   $$f_2(2) = \mathbf{0.565844}$$

**Conclusión:** La aproximación por interpolación cuadrática nos da $0.565844$. El valor analítico de $\ln(2)$ es $0.693147$. Nuestro error absoluto ahora es de $\approx 0.1273$, lo cual es **casi la mitad del error** que obtuvimos con la interpolación lineal ($0.2310$). Al añadir la curvatura (coeficiente negativo $b_2$), la parábola se "dobló" hacia abajo acercándose mucho más a la curva real del logaritmo natural.

## Interpolación Segmentada (Splines)



### Teoría y Fundamentación Matemática
A medida que aumentamos el número de puntos de datos, los polinomios de interpolación tradicionales (como Newton o Lagrange) requieren un grado cada vez mayor. Esto provoca que la curva resultante oscile violentamente entre los puntos, generando errores de estimación masivos. 

La **interpolación segmentada** resuelve este problema aplicando un enfoque de "divide y vencerás". En lugar de buscar un único polinomio gigante que pase por todos los puntos, se aplican polinomios de **bajo grado** (líneas, parábolas o curvas cúbicas) para unir los puntos **segmento por segmento**.

Tipos de Splines más comunes:
* **Splines Lineales (Grado 1):** Une los puntos con líneas rectas. Es simple y rápido, pero genera "picos" en los nodos (no hay suavidad).
* **Splines Cuadráticos (Grado 2):** Une los puntos con parábolas, asegurando que la primera derivada (la pendiente) sea continua en los nodos.
* **Splines Cúbicos (Grado 3):** Es el estándar de la industria (usado en software de diseño y gráficos por computadora). Une los puntos con curvas de tercer grado, garantizando que tanto la primera como la segunda derivada sean continuas, logrando una curva visualmente perfecta y suave sin oscilaciones.

Para fines prácticos y de asimilación manual, esta guía se enfoca en la formulación de los **Splines Lineales**.

### Fórmulas y Criterios
Dado un conjunto de puntos ordenados $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$, la interpolación segmentada lineal crea una función $f_i(x)$ para cada intervalo entre $x_{i-1}$ y $x_i$.

Para interpolar un valor $x$, primero se debe encontrar en qué intervalo $[x_{i-1}, x_i]$ se encuentra. Una vez identificado el segmento $i$, se aplica la ecuación de la recta para ese tramo:

$$f_i(x) = y_{i-1} + m_i (x - x_{i-1})$$

Donde la pendiente $m_i$ del segmento se calcula como:
$$m_i = \frac{y_i - y_{i-1}}{x_i - x_{i-1}}$$

### Ejercicio Resuelto
**Enunciado:** Tienes los siguientes datos de velocidad de un vehículo en distintos tiempos:
* Tiempo 2.0 seg: Velocidad 15.0 m/s
* Tiempo 4.0 seg: Velocidad 25.0 m/s
* Tiempo 5.5 seg: Velocidad 20.0 m/s

Calcula la velocidad estimada en el tiempo de 4.5 segundos utilizando interpolación segmentada lineal.

**Solución paso a paso:**
**1. Ordenar e identificar los datos:**
   Tenemos tres puntos y, por lo tanto, dos intervalos (segmentos):
   * Segmento 1: Entre $x_0 = 2.0$ y $x_1 = 4.0$
   * Segmento 2: Entre $x_1 = 4.0$ y $x_2 = 5.5$
   * Valor objetivo a estimar: $x = 4.5$

**2. Ubicar el intervalo correspondiente:**
   El valor objetivo $4.5$ se encuentra entre $4.0$ y $5.5$. Por lo tanto, debemos trabajar exclusivamente con el **Segmento 2**.
   * Puntos a usar: $(4.0, 25.0)$ y $(5.5, 20.0)$

**3. Calcular la pendiente del Segmento 2 ($m_2$):**
   $$m_2 = \frac{20.0 - 25.0}{5.5 - 4.0}$$
   $$m_2 = \frac{-5.0}{1.5} = -3.3333$$

**4. Sustituir en la ecuación del Spline Lineal para ese tramo:**
   $$f_2(4.5) = 25.0 + (-3.3333)(4.5 - 4.0)$$
   $$f_2(4.5) = 25.0 - 3.3333(0.5)$$
   $$f_2(4.5) = 25.0 - 1.6667 = \mathbf{23.3333}$$

**Conclusión:** La velocidad estimada a los 4.5 segundos es de 23.3333 m/s. La principal ventaja de los Splines es que el punto lejano $(2.0, 15.0)$ no afectó negativamente el cálculo en nuestro segmento de interés, evitando así distorsiones globales.

## Código
[Interpolacion.py](../3-Codigos/Interpolacion.py)
---
﻿Problemario Unidad 5 Esteban Romero Pérez
 > [!NOTE]
> Link de problemario
https://docs.google.com/document/d/1conBeG_7cQcDNQxqpWYS1doGB19HsSLmJ-oKKWu0jPg/edit?usp=drive_link
