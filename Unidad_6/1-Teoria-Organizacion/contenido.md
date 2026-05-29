## Método de Euler



### Teoría y Fundamentación Matemática
El método de Euler es un procedimiento numérico de primer orden para resolver ecuaciones diferenciales ordinarias (EDO) que tienen un valor inicial conocido. 

La idea principal se basa en el concepto geométrico de la derivada. Si conocemos la ecuación diferencial $y' = f(x, y)$ y un punto inicial exacto $(x_0, y_0)$, la ecuación nos está dando la **pendiente** de la curva en ese preciso instante. El método de Euler utiliza esa pendiente para trazar una línea recta (tangente) y dar un pequeño "paso" hacia adelante (de tamaño $h$) para predecir el siguiente punto.

Dado que asume que la pendiente se mantiene constante durante todo el paso $h$ (lo cual rara vez es cierto en curvas reales), este método genera un error de truncamiento considerable. Para obtener resultados aceptables, el tamaño de paso $h$ debe ser **muy pequeño**, lo que a su vez requiere más iteraciones.

### Fórmulas y Criterios
Para un problema de valor inicial dado por $y' = f(x, y)$ con la condición inicial $y(x_0) = y_0$, y un tamaño de paso $h$:

1. **Avance en el eje X:**
   Los valores de $x$ avanzan de manera constante sumando el tamaño de paso:
   $$x_{i+1} = x_i + h$$

2. **Fórmula de iteración de Euler (eje Y):**
   El nuevo valor de $y$ se calcula tomando el valor anterior y sumándole el producto de la pendiente evaluada en el punto anterior por el tamaño del paso:
   $$y_{i+1} = y_i + h f(x_i, y_i)$$

### Ejercicio Resuelto
**Enunciado:** Resuelve la ecuación diferencial $y' = x + y$, con la condición inicial $y(0) = 1$. Estima el valor de $y$ cuando $x = 0.2$ utilizando un tamaño de paso $h = 0.1$.

**Solución paso a paso:**
**1. Identificación de datos iniciales:**
   * Función de la derivada: $f(x, y) = x + y$
   * Punto inicial: $x_0 = 0$, $y_0 = 1$
   * Tamaño de paso: $h = 0.1$
   * Objetivo: $y$ en $x = 0.2$ (requerirá 2 iteraciones).

**2. Iteración 1 (Buscando $y_1$ en $x_1 = 0.1$):**
   Evaluamos la pendiente en el punto inicial $(0, 1)$:
   $$f(x_0, y_0) = 0 + 1 = 1$$
   Aplicamos la fórmula de Euler:
   $$y_1 = y_0 + h f(x_0, y_0)$$
   $$y_1 = 1 + 0.1(1) = 1.1$$
   *Resultado:* En $x_1 = 0.1$, el valor aproximado es $y_1 = 1.1$.

**3. Iteración 2 (Buscando $y_2$ en $x_2 = 0.2$):**
   Evaluamos la pendiente en el nuevo punto $(0.1, 1.1)$:
   $$f(x_1, y_1) = 0.1 + 1.1 = 1.2$$
   Aplicamos la fórmula de Euler:
   $$y_2 = y_1 + h f(x_1, y_1)$$
   $$y_2 = 1.1 + 0.1(1.2)$$
   $$y_2 = 1.1 + 0.12 = \mathbf{1.22}$$

**Conclusión:** La aproximación por el método de Euler nos da $y(0.2) \approx 1.22$. 
La solución analítica exacta de esta ecuación es $y(x) = 2e^x - x - 1$. Si evaluamos el valor real en $x = 0.2$, obtenemos $y(0.2) = 2e^{0.2} - 0.2 - 1 \approx 1.2428$. El error es evidente, pero es de esperarse en un método de primer orden con un paso tan "grande" como $h = 0.1$.
---
## Código 
* [Abrir Método de Euler](../3-Codigos/Euler.py)

## Método de Taylor



### Teoría y Fundamentación Matemática
El método de Euler que vimos anteriormente se basa en trazar una línea recta usando la primera derivada. Sin embargo, las funciones reales suelen ser curvas. El **Método de Taylor** resuelve este problema añadiendo derivadas de orden superior (segunda derivada, tercera derivada, etc.) para "doblar" nuestra estimación y ajustarla mucho mejor a la curvatura real de la solución.

La base de este método es la famosa **Serie de Taylor**, la cual establece que cualquier función suave puede ser aproximada alrededor de un punto mediante un polinomio. Al aplicar esto a ecuaciones diferenciales ordinarias (EDOs), podemos controlar la precisión de nuestro cálculo eligiendo el "orden" del método. 
* Un Taylor de orden 1 (solo la primera derivada) es el Método de Euler.
* Un Taylor de orden 2 incluye la curvatura (segunda derivada), disminuyendo radicalmente el error de truncamiento sin necesidad de usar un tamaño de paso $h$ microscópico.

La principal desventaja geométrica/analítica de este método es que **requiere que calculemos las derivadas de la función a mano** antes de programarlo, lo cual puede ser tedioso si la EDO original es muy compleja.

### Fórmulas y Criterios
Dada una EDO de la forma $y' = f(x, y)$ con valor inicial $y(x_0) = y_0$, y un tamaño de paso $h$, el avance en $x$ es constante ($x_{i+1} = x_i + h$).

**Fórmula de iteración de Taylor de Orden $k$:**
$$y_{i+1} = y_i + h y'_i + \frac{h^2}{2!} y''_i + \frac{h^3}{3!} y'''_i + \dots + \frac{h^k}{k!} y^{(k)}_i$$

Donde:
* $y'_i = f(x_i, y_i)$
* $y''_i = f'(x_i, y_i)$ (Se debe aplicar regla de la cadena derivando implícitamente respecto a $x$).

### Ejercicio Resuelto
**Enunciado:** Vamos a resolver la misma ecuación que en el método de Euler: $y' = x + y$, con condición inicial $y(0) = 1$. Estima el valor de $y$ en $x = 0.2$ con paso $h = 0.1$, pero esta vez usando **Taylor de Orden 2**.

**Solución paso a paso:**
**1. Preparación y cálculo de derivadas:**
   * EDO original (1ra derivada): $y' = x + y$
   * Derivamos respecto a $x$ para obtener la 2da derivada: $y'' = 1 + y'$
   * Sustituyendo $y'$ en la segunda derivada: $y'' = 1 + (x + y)$

**2. Iteración 1 (Buscando $y_1$ en $x_1 = 0.1$):**
   * Punto actual: $x_0 = 0$, $y_0 = 1$
   * Evaluamos las derivadas:
     $y'_0 = 0 + 1 = 1$
     $y''_0 = 1 + 0 + 1 = 2$
   * Aplicamos la fórmula de Taylor de Orden 2:
     $$y_1 = y_0 + h y'_0 + \frac{h^2}{2} y''_0$$
     $$y_1 = 1 + 0.1(1) + \frac{(0.1)^2}{2}(2)$$
     $$y_1 = 1 + 0.1 + 0.01 = \mathbf{1.11}$$
   *(Nota: Euler simple nos había dado 1.1)*

**3. Iteración 2 (Buscando $y_2$ en $x_2 = 0.2$):**
   * Punto actual: $x_1 = 0.1$, $y_1 = 1.11$
   * Evaluamos las derivadas:
     $y'_1 = 0.1 + 1.11 = 1.21$
     $y''_1 = 1 + 0.1 + 1.11 = 2.21$
   * Aplicamos la fórmula:
     $$y_2 = y_1 + h y'_1 + \frac{h^2}{2} y''_1$$
     $$y_2 = 1.11 + 0.1(1.21) + \frac{0.01}{2}(2.21)$$
     $$y_2 = 1.11 + 0.121 + 0.01105 = \mathbf{1.24205}$$

**Conclusión:** La aproximación por Taylor de orden 2 nos da $1.24205$. 
Recordemos que el valor exacto de la solución $y(0.2)$ es aproximadamente $1.2428$. El error absoluto ha caído a **$0.00075$** (mientras que Euler con el mismo paso $h$ tuvo un error de $0.0228$). ¡Un salto masivo en precisión por tan solo añadir un término más a la serie!
---
## Código 
* [Abrir Método de Taylor](../3-Codigos/taylor.py)

## Método de Runge-Kutta (RK4)



### Teoría y Fundamentación Matemática
Como vimos, el método de Euler sufre de falta de precisión, y el método de Taylor requiere el cálculo manual y tedioso de derivadas de orden superior. Los matemáticos Carl Runge y Martin Kutta desarrollaron una familia de métodos que logran la misma precisión que las series de Taylor de alto grado, **pero evaluando únicamente la primera derivada (la función original)** en diferentes puntos dentro del intervalo.

El método más popular es el de **Cuarto Orden (RK4)**. Su lógica consiste en calcular cuatro pendientes intermedias (llamadas $k_1, k_2, k_3, k_4$) a lo largo del paso $h$, y luego promediarlas dándole más "peso" a las pendientes centrales. 
* $k_1$: Pendiente al inicio del intervalo (idéntica a la de Euler).
* $k_2$: Pendiente en el punto medio, usando $k_1$ para avanzar.
* $k_3$: Pendiente en el punto medio, usando $k_2$ para avanzar.
* $k_4$: Pendiente al final del intervalo, usando $k_3$ para avanzar.

Este promedio ponderado se ajusta maravillosamente a la curva real, eliminando casi por completo el error de truncamiento sin necesidad de derivar analíticamente.

### Fórmulas y Criterios
Dada una EDO de la forma $y' = f(x, y)$ con valor inicial $y(x_0) = y_0$, y un tamaño de paso $h$, el avance en $x$ es constante ($x_{i+1} = x_i + h$).

Para calcular el nuevo valor $y_{i+1}$, primero se evalúan las cuatro pendientes ($k$):
1. $$k_1 = f(x_i, y_i)$$
2. $$k_2 = f\left(x_i + \frac{h}{2}, y_i + \frac{h}{2} k_1\right)$$
3. $$k_3 = f\left(x_i + \frac{h}{2}, y_i + \frac{h}{2} k_2\right)$$
4. $$k_4 = f(x_i + h, y_i + h k_3)$$

Finalmente, se combinan en la fórmula iterativa principal:
$$y_{i+1} = y_i + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)$$

### Ejercicio Resuelto
**Enunciado:** Resuelve la misma ecuación que en los métodos anteriores: $y' = x + y$, con condición inicial $y(0) = 1$. Para demostrar el poder de RK4, estimaremos el valor de $y$ en $x = 0.2$ en un solo "salto" usando un tamaño de paso **el doble de grande**: $h = 0.2$.

**Solución paso a paso:**
**1. Identificación de datos iniciales:**
   * Función: $f(x, y) = x + y$
   * Punto actual: $x_0 = 0$, $y_0 = 1$
   * Tamaño de paso: $h = 0.2$
   * Punto medio para las X: $x_0 + \frac{h}{2} = 0 + 0.1 = 0.1$

**2. Cálculo de las 4 pendientes ($k$):**
   * **Para $k_1$:**
     $$k_1 = f(0, 1) = 0 + 1 = \mathbf{1.0}$$
   * **Para $k_2$:**
     Evaluamos en $x = 0.1$ y $y = 1 + \frac{0.2}{2}(1.0) = 1.1$
     $$k_2 = f(0.1, 1.1) = 0.1 + 1.1 = \mathbf{1.2}$$
   * **Para $k_3$:**
     Evaluamos en $x = 0.1$ y $y = 1 + \frac{0.2}{2}(1.2) = 1.12$
     $$k_3 = f(0.1, 1.12) = 0.1 + 1.12 = \mathbf{1.22}$$
   * **Para $k_4$:**
     Evaluamos en $x = 0 + 0.2 = 0.2$ y $y = 1 + 0.2(1.22) = 1.244$
     $$k_4 = f(0.2, 1.244) = 0.2 + 1.244 = \mathbf{1.444}$$

**3. Aplicación de la fórmula principal (promedio ponderado):**
   $$y_1 = 1 + \frac{0.2}{6} \Big[ 1.0 + 2(1.2) + 2(1.22) + 1.444 \Big]$$
   $$y_1 = 1 + \frac{0.2}{6} \Big[ 1.0 + 2.4 + 2.44 + 1.444 \Big]$$
   $$y_1 = 1 + \frac{0.2}{6} \Big[ 7.284 \Big]$$
   $$y_1 = 1 + 0.2428 = \mathbf{1.2428}$$

**Conclusión:** La aproximación por RK4 nos da exactamente $1.2428$. 
Recordemos que el valor analítico de $y(0.2)$ es $2e^{0.2} - 0.2 - 1 \approx 1.2428055$. ¡A pesar de usar un tamaño de paso del doble de grande que en Euler y Taylor, RK4 logró una precisión exacta hasta el cuarto decimal! El error es microscópico ($0.0000055$).
---
* [Abrir Método de Runge-Kutta](../3-Codigos/Runge-Kutta.py)
---
﻿Problemario Unidad 6 Esteban Romero Pérez
 > [!NOTE]
> Link de problemario
(https://docs.google.com/document/d/1rk-MkA3gbgQdhzJpSb7arZnZ0lK3JochQMAkRW4v-HY/edit?usp=sharing)
