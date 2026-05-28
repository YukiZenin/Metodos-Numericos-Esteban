## 1. Método de Euler

### Teoría y Fundamentación Matemática
El método de Euler es el procedimiento numérico más básico para resolver Ecuaciones Diferenciales Ordinarias (EDO) de primer orden con valores iniciales dados. Su lógica se basa en la aproximación lineal local: utiliza la derivada (la pendiente de la curva) en un punto conocido para proyectar y estimar el valor de la función en un punto futuro cercano.

Si avanzamos mediante incrementos pequeños (llamados tamaño de paso, $h$), la recta tangente en el punto inicial nos guía hacia el siguiente valor. Al repetir este proceso iterativamente, construimos una curva poligonal que aproxima la solución real. La principal desventaja de este método es que el error de truncamiento se acumula rápidamente si el tamaño de paso $h$ no es lo suficientemente pequeño, ya que asume que la pendiente se mantiene constante durante todo el intervalo.

### Fórmulas
Dada una EDO de la forma $y' = f(x, y)$ con una condición inicial $y(x_0) = y_0$, el valor en el siguiente paso se calcula como:

$$y_{i+1} = y_i + h \cdot f(x_i, y_i)$$
$$x_{i+1} = x_i + h$$

Donde:
* $h$ es el tamaño de paso (incremento en el eje horizontal).
* $f(x_i, y_i)$ es la evaluación de la derivada en el punto actual (la pendiente).

### Ejercicio Resuelto
**Enunciado:** Resuelve la EDO $y' = x + y$, con la condición inicial $y(0) = 1$. Estima el valor de $y$ para $x = 0.1$ utilizando un tamaño de paso $h = 0.1$.

**Solución paso a paso:**
1. **Identificar los datos iniciales:**
   * $x_0 = 0, \quad y_0 = 1$
   * Función: $f(x, y) = x + y$
   * Paso: $h = 0.1$
2. **Evaluar la función en el punto inicial para obtener la pendiente:**
   $$f(x_0, y_0) = 0 + 1 = 1$$
3. **Aplicar la fórmula de Euler:**
   $$y_1 = y_0 + h \cdot f(x_0, y_0)$$
   $$y_1 = 1 + 0.1 \cdot (1)$$
4. **Calcular el resultado final:**
   $$y_1 = 1 + 0.1 = 1.1$$

**Resultado:** Mediante el método de Euler, el valor estimado de $y(0.1)$ es **1.1**.

---
## Código 
* [Abrir Método de Euler](./3-Codigos/Euler.py)

## 2. Método de Taylor (Orden Superior)

### Teoría y Fundamentación Matemática
El método de Taylor busca superar la imprecisión de Euler agregando más información sobre la curvatura real de la función. Mientras Euler solo utiliza la primera derivada (aproximación lineal), el método de Taylor expande la función en una serie matemática que incluye la segunda, tercera o enésima derivada de la EDO.

Al incorporar derivadas de orden superior, el algoritmo "anticipa" cómo va a cambiar la pendiente dentro del intervalo $h$, logrando una adaptación mucho más fiel a las curvas pronunciadas. La dificultad práctica de este método radica en que requiere calcular analíticamente las derivadas sucesivas de la función $f(x, y)$ antes de programarlo, lo cual puede ser algebraicamente complejo.

### Fórmulas
La fórmula general de la serie de Taylor de orden $n$ para avanzar al siguiente punto es:

$$y_{i+1} = y_i + h y'_i + \frac{h^2}{2!} y''_i + \frac{h^3}{3!} y'''_i + \dots + \frac{h^n}{n!} y^{(n)}_i$$

Donde $y'_i = f(x_i, y_i)$, y las derivadas siguientes se obtienen derivando implícitamente $f(x, y)$ respecto a $x$.

### Ejercicio Resuelto
**Enunciado:** Resuelve la misma EDO $y' = x + y$, con $y(0) = 1$. Calcula $y(0.1)$ con $h = 0.1$ utilizando el método de Taylor de **segundo orden**.

**Solución paso a paso:**
1. **Definir las derivadas necesarias:**
   * Primera derivada: $y' = x + y$
   * Segunda derivada (derivando implícitamente): $y'' = 1 + y'$
2. **Evaluar las derivadas en el punto inicial ($x_0 = 0, y_0 = 1$):**
   * $y'_0 = 0 + 1 = 1$
   * $y''_0 = 1 + (1) = 2$
3. **Aplicar la fórmula de Taylor de orden 2:**
   $$y_1 = y_0 + h(y'_0) + \frac{h^2}{2}(y''_0)$$
   $$y_1 = 1 + 0.1(1) + \frac{(0.1)^2}{2}(2)$$
4. **Resolver las operaciones:**
   $$y_1 = 1 + 0.1 + \frac{0.01}{2}(2)$$
   $$y_1 = 1 + 0.1 + 0.01 = 1.11$$

**Resultado:** Mediante Taylor de 2º orden, el valor estimado de $y(0.1)$ es **1.11**.

---
## Código 
* [Abrir Método de Taylor](./3-Codigos/taylor.py)

## 3. Método de Runge-Kutta (Cuarto Orden - RK4)

### Teoría y Fundamentación Matemática
El método de Runge-Kutta de cuarto orden (comúnmente llamado RK4) es el estándar de oro en la ingeniería y la física para resolver EDOs. Logra la misma asombrosa precisión que un método de Taylor de cuarto orden, pero con una ventaja crucial: **no requiere calcular derivadas analíticas complejas**. 

En lugar de derivar, RK4 toma una "muestra" de la pendiente en cuatro puntos estratégicos dentro del intervalo de tamaño $h$:
1. $k_1$: La pendiente al inicio del intervalo (igual a Euler).
2. $k_2$: La pendiente en el punto medio, usando $k_1$ para estimar la altura.
3. $k_3$: Una nueva estimación de la pendiente en el punto medio, pero ahora usando $k_2$.
4. $k_4$: La pendiente al final del intervalo, proyectada usando $k_3$.

Finalmente, realiza un promedio ponderado de estas cuatro pendientes (dando más peso a las centrales) para calcular un incremento altamente preciso.

### Fórmulas
Para calcular el siguiente punto $y_{i+1}$:

$$y_{i+1} = y_i + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)$$

Donde los coeficientes $k$ se evalúan secuencialmente así:
$$k_1 = f(x_i, y_i)$$
$$k_2 = f\left(x_i + \frac{h}{2}, y_i + \frac{h}{2} k_1\right)$$
$$k_3 = f\left(x_i + \frac{h}{2}, y_i + \frac{h}{2} k_2\right)$$
$$k_4 = f(x_i + h, y_i + h k_3)$$

### Ejercicio Resuelto
**Enunciado:** Resuelve la EDO $y' = x + y$, con $y(0) = 1$. Calcula $y(0.1)$ con $h = 0.1$ usando Runge-Kutta de cuarto orden.

**Solución paso a paso:**
1. **Identificar datos:** $x_0 = 0$, $y_0 = 1$, $h = 0.1$, $f(x,y) = x + y$.
2. **Calcular los cuatro coeficientes $k$:**
   * **$k_1$ (evaluado en $x=0, y=1$):**
     $$k_1 = 0 + 1 = 1$$
   * **$k_2$ (evaluado en $x = 0 + 0.05, y = 1 + 0.05(1)$):**
     $$k_2 = f(0.05, 1.05) = 0.05 + 1.05 = 1.1$$
   * **$k_3$ (evaluado en $x = 0 + 0.05, y = 1 + 0.05(1.1)$):**
     $$k_3 = f(0.05, 1.055) = 0.05 + 1.055 = 1.105$$
   * **$k_4$ (evaluado en $x = 0 + 0.1, y = 1 + 0.1(1.105)$):**
     $$k_4 = f(0.1, 1.1105) = 0.1 + 1.1105 = 1.2105$$
3. **Calcular el promedio ponderado y sumar a $y_0$:**
   $$y_1 = 1 + \frac{0.1}{6} [1 + 2(1.1) + 2(1.105) + 1.2105]$$
   $$y_1 = 1 + \frac{0.1}{6} [1 + 2.2 + 2.21 + 1.2105]$$
   $$y_1 = 1 + \frac{0.1}{6} [6.6205]$$
   $$y_1 = 1 + 0.1103416...$$
4. **Resultado final:**
   $$y_1 \approx 1.11034$$

**Resultado:** Mediante RK4, el valor altamente preciso de $y(0.1)$ es **1.11034**.

---
﻿Problemario Unidad 6 Esteban Romero Pérez
 > [!NOTE]
> Link de problemario
(https://docs.google.com/document/d/1rk-MkA3gbgQdhzJpSb7arZnZ0lK3JochQMAkRW4v-HY/edit?usp=sharing)
## Código 

* [Abrir Método de Runge-Kutta](./3-Codigos/Runge-Kutta.py)


