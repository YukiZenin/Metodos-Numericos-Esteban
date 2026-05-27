## 1. Interpolación Lineal

### Teoría y Fundamentación Matemática
La interpolación lineal es la forma más elemental de aproximación polinómica. Supone que, dentro de un intervalo cerrado definido por dos puntos conocidos $P_0(x_0, y_0)$ y $P_1(x_1, y_1)$, el comportamiento de la función desconocida $f(x)$ puede modelarse aceptablemente mediante una línea recta (un polinomio de primer grado, $P_1(x)$).

Geométricamente, este método se basa en el principio de la **semejanza de triángulos**. Si trazamos una línea recta entre $P_0$ y $P_1$, la pendiente ($m$) de la recta debe permanecer constante en cualquier punto intermedio $(x, y)$ que pertenezca a dicho segmento. Por lo tanto, podemos igualar las pendientes de la siguiente manera:

$$\frac{y - y_0}{x - x_0} = \frac{y_1 - y_0}{x_1 - x_0}$$



Al despejar la variable dependiente $y$, obtenemos la ecuación clásica de interpolación.

#### Análisis del Error
El error de truncamiento local para la interpolación lineal está sujeto a la segunda derivada de la función real $f(x)$. Si $f(x)$ es dos veces diferenciable en el intervalo $[x_0, x_1]$, el error $E(x) = f(x) - P_1(x)$ viene dado por:

$$E(x) = \frac{f''(\xi)}{2!} (x - x_0)(x - x_1)$$

Donde $\xi$ es un valor desconocido que reside dentro del intervalo $[x_0, x_1]$. Esto implica dos realidades fundamentales:
1. El error es estrictamente cero en los nodos de interpolación ($x = x_0$ y $x = x_1$).
2. El error aumenta si la función real tiene una alta curvatura (segunda derivada grande) o si la distancia horizontal entre $x_0$ y $x_1$ (el tamaño del intervalo) es muy amplia.

### Fórmulas
Para un valor objetivo $x$ tal que $x_0 \le x \le x_1$:

$$y = y_0 + \frac{y_1 - y_0}{x_1 - x_0} (x - x_0)$$

Donde el término $\frac{y_1 - y_0}{x_1 - x_0}$ representa la razón de cambio o pendiente entre los límites del intervalo.

### Ejercicio Resuelto
**Enunciado:** Un experimento químico registra que a una temperatura de $10^\circ\text{C}$ la presión de un gas es de $2.4\text{ atm}$, y a $20^\circ\text{C}$ la presión se eleva a $3.1\text{ atm}$. Suponiendo un comportamiento lineal, estima la presión del gas cuando la temperatura es de $15^\circ\text{C}$.

**Solución paso a paso:**
1. **Definir las variables e identificar los datos:**
   * Nodo inicial: $x_0 = 10$, $y_0 = 2.4$
   * Nodo final: $x_1 = 20$, $y_1 = 3.1$
   * Valor objetivo: $x = 15$
2. **Sustituir los valores en la fórmula matemática:**
   $$y = 2.4 + \frac{3.1 - 2.4}{20 - 10} (15 - 10)$$
3. **Calcular la pendiente (razón de cambio):**
   $$m = \frac{0.7}{10} = 0.07$$
4. **Evaluar el desplazamiento respecto al punto de origen:**
   $$y = 2.4 + 0.07 \cdot (5)$$
   $$y = 2.4 + 0.35 = 2.75$$

**Resultado:** La presión estimada a una temperatura de $15^\circ\text{C}$ es de **2.75 atm**.

---

## 2. Interpolación Cuadrática

### Teoría y Fundamentación Matemática
Cuando el fenómeno físico analizado presenta una dinámica no lineal (aceleración, variaciones parabólicas, curvas de crecimiento), una aproximación lineal introduce un sesgo inaceptable. La interpolación cuadrática resuelve esto aproximando la función mediante un polinomio de segundo grado ($P_2(x) = ax^2 + bx + c$), el cual requiere de manera obligatoria **tres puntos conocidos** no colineales.

Aunque es posible encontrar este polinomio planteando un sistema de ecuaciones lineales de $3 \times 3$ utilizando la matriz de Vandermonde ($ax_i^2 + bx_i + c = y_i$), este enfoque suele ser computacionalmente ineficiente y propenso a errores de redondeo si los nodos están muy juntos. En su lugar, se utiliza el enfoque del **Polinomio de Interpolación de Lagrange**.

La filosofía de Lagrange consiste en construir funciones polinómicas base, denotadas como $L_i(x)$, que actúan como "conmutadores algebraicos". Cada polinomio base $L_i(x)$ tiene la propiedad única de valer exactamente **1** cuando se evalúa en su propio nodo $x_i$, y exactamente **0** cuando se evalúa en cualquier otro nodo $x_j$ (donde $j \neq i$).



De este modo, el polinomio cuadrático global se forma simplemente sumando las ordenadas $y_i$ ponderadas por sus respectivas bases de Lagrange, garantizando que la parábola resultante pase de manera exacta por los tres puntos dados.

### Fórmulas
Dados los puntos $P_0(x_0, y_0)$, $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$, el polinomio de interpolación es:

$$y = y_0 L_0(x) + y_1 L_1(x) + y_2 L_2(x)$$

Las funciones base de Lagrange de segundo grado se estructuran omitiendo sistemáticamente el nodo actual en el numerador y normalizando el valor en el denominador:

$$L_0(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)}$$

$$L_1(x) = \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)}$$

$$L_2(x) = \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}$$

### Ejercicio Resuelto
**Enunciado:** Un vehículo en una pista de pruebas registra las siguientes posiciones en determinados tiempos: a los $0\text{ s}$ está en la marca de $1\text{ m}$, al cabo de $1\text{ s}$ llega a los $3\text{ m}$, y a los $2\text{ s}$ se ubica en los $7\text{ m}$. Encuentra su posición estimada a los $1.5\text{ s}$ empleando un polinomio de Lagrange de segundo grado.

**Solución paso a paso:**
1. **Estructurar el conjunto de datos:**
   * $P_0(0, 1) \rightarrow x_0 = 0, \quad y_0 = 1$
   * $P_1(1, 3) \rightarrow x_1 = 1, \quad y_1 = 3$
   * $P_2(2, 7) \rightarrow x_2 = 2, \quad y_2 = 7$
   * Valor a evaluar: $x = 1.5$
2. **Calcular los polinomios base de Lagrange para $x = 1.5$:**
   * **Para $L_0$:**
     $$L_0(1.5) = \frac{(1.5 - 1)(1.5 - 2)}{(0 - 1)(0 - 2)} = \frac{(0.5)(-0.5)}{(-1)(-2)} = \frac{-0.25}{2} = -0.125$$
   * **Para $L_1$:**
     $$L_1(1.5) = \frac{(1.5 - 0)(1.5 - 2)}{(1 - 0)(1 - 2)} = \frac{(1.5)(-0.5)}{(1)(-1)} = \frac{-0.75}{-1} = 0.75$$
   * **Para $L_2$:**
     $$L_2(1.5) = \frac{(1.5 - 0)(1.5 - 1)}{(2 - 0)(2 - 1)} = \frac{(1.5)(0.5)}{(2)(1)} = \frac{0.75}{2} = 0.375$$
3. **Efectuar la combinación lineal con las ordenadas:**
   $$y = (1 \cdot -0.125) + (3 \cdot 0.75) + (7 \cdot 0.375)$$
   $$y = -0.125 + 2.25 + 2.625$$
   $$y = 4.75$$

**Resultado:** La posición estimada del vehículo a los $1.5\text{ s}$ es de **4.75 metros**.

---

## 3. Interpolación Segmentada (Lineal)

### Teoría y Fundamentación Matemática
A primera vista, podría pensarse que para aproximar con mayor precisión un conjunto grande de datos ($n$ puntos) bastaría con elevar el grado del polinomio de interpolación (por ejemplo, usar un polinomio de grado 6 o 7 para 8 puntos). Sin embargo, esto introduce un problema severo conocido en análisis numérico como el **Fenómeno de Runge**. 

Al ajustar un único polinomio global de alto grado sobre puntos equiespaciados, la curva tiende a desarrollar oscilaciones extremas e inestabilidades violentas, especialmente cerca de los límites del dominio. El polinomio cumple matemáticamente con pasar por los puntos, pero falla por completo en representar el comportamiento intermedio real.



La **interpolación segmentada** (o interpolación por *splines* de bajo grado) elimina este problema de raíz. En lugar de forzar a que una sola función matemática compleja cubra todo el conjunto de datos, el dominio global se divide en una secuencia de subintervalos adyacentes conectados por los propios nodos. 

En la variante **lineal segmentada**, cada par de puntos consecutivos $[x_i, x_{i+1}]$ se une mediante una recta independiente. Esto garantiza que la aproximación sea continua a lo largo de todo el dominio (continuidad $C^0$), evitando las oscilaciones artificiales de los polinomios de alto grado.

El proceso algorítmico consta de tres etapas esenciales:
1. **Ordenamiento:** Asegurar que el conjunto de puntos esté estrictamente ordenado de menor a mayor en el eje $X$.
2. **Búsqueda del intervalo:** Localizar el segmento específico $[x_i, x_{i+1}]$ tal que cumpla la condición de confinamiento $x_i \le x_{obj} \le x_{i+1}$.
3. **Evaluación local:** Aplicar la fórmula lineal acotada exclusivamente a los dos puntos que definen el segmento hallado.

### Fórmulas
Para un conjunto ordenado de $n$ puntos donde $x \in [x_i, x_{i+1}]$:

$$y = y_i + \frac{y_{i+1} - y_i}{x_{i+1} - x_i} (x - x_i)$$

La función global queda definida por tramos:

$$S(x) = \begin{cases} 
S_0(x) & x \in [x_0, x_1] \\
S_1(x) & x \in [x_1, x_2] \\
\vdots & \\
S_{n-1}(x) & x \in [x_{n-1}, x_n] 
\end{cases}$$

### Ejercicio Resuelto
**Enunciado:** Se dispone del siguiente perfil topográfico digitalizado en tres coordenadas: $P_0(0, 0)$, $P_1(2, 4)$ y $P_2(5, 1)$. Utiliza interpolación lineal segmentada para estimar la altura del terreno ($y$) en la posición horizontal $x = 3$.

**Solución paso a paso:**
1. **Identificar y verificar el orden de los intervalos:**
   * Los puntos ya se encuentran ordenados en el eje $X$ ($0 < 2 < 5$).
   * Segmento 1: abarca el intervalo $x \in [0, 2]$ mediante los puntos $(0,0)$ y $(2,4)$.
   * Segmento 2: abarca el intervalo $x \in [2, 5]$ mediante los puntos $(2,4)$ y $(5,1)$.
2. **Fase de localización del valor objetivo:**
   * El valor buscado es $x = 3$.
   * Evaluamos las condiciones: $3$ no pertenece al intervalo $[0, 2]$, pero sí cumple con estar confinado en el intervalo del **Segmento 2** ($2 \le 3 \le 5$). El Segmento 1 queda descartado para el cálculo.
3. **Efectuar el cálculo lineal restringido al Segmento 2:**
   * Definimos los parámetros locales del segmento: $x_i = 2, \ y_i = 4$ y $x_{i+1} = 5, \ y_{i+1} = 1$.
   * Sustituimos en la ecuación lineal de tramo:
     $$y = 4 + \frac{1 - 4}{5 - 2} (3 - 2)$$
4. **Resolver la aritmética analíticamente:**
   $$y = 4 + \frac{-3}{3} (1)$$
   $$y = 4 + (-1) \cdot 1 = 3$$

**Resultado:** La altura estimada en la posición $x = 3$ mediante el método segmentado es **3**.

## Código
[Interpolacion.py](./3-Codigos/Interpolacion.py)
