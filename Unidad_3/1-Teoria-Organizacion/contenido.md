## Método de Eliminación Gaussiana

### Teoría y Fundamentación Matemática
A diferencia de los métodos iterativos para buscar raíces, la eliminación gaussiana es un **método directo** utilizado para resolver sistemas de ecuaciones lineales de la forma $Ax = b$. 

El objetivo principal de este algoritmo es transformar el sistema de ecuaciones original en un sistema equivalente (que tenga exactamente las mismas soluciones) pero que sea mucho más fácil de resolver. Esto se logra mediante **operaciones elementales de fila** (sumar, restar, multiplicar por constantes o intercambiar filas) aplicadas sobre la matriz aumentada del sistema.

El proceso se divide en dos fases principales:
1. **Eliminación hacia adelante:** Consiste en hacer ceros todos los elementos por debajo de la diagonal principal, convirtiendo la matriz original en una **matriz triangular superior**.
2. **Sustitución hacia atrás:** Una vez obtenida la matriz triangular, la última ecuación del sistema tendrá una sola incógnita, la cual se despeja directamente. Luego, este valor se sustituye en la ecuación de arriba para hallar la siguiente incógnita, y así sucesivamente hasta resolver todo el sistema.

### Fórmulas y Criterios
1. **Operación elemental (Cálculo del factor y actualización de fila):**
   Para eliminar el elemento en la fila $j$ y columna $i$ (donde $j > i$), calculamos un multiplicador o factor $m$:
   $$m = \frac{a_{ji}}{a_{ii}}$$
   Y actualizamos toda la fila $j$:
   $$F_j \leftarrow F_j - m \cdot F_i$$

2. **Sustitución hacia atrás:**
   Una vez triangularizada la matriz (de tamaño $n \times n$), la variable $x_n$ se halla como:
   $$x_n = \frac{b_n}{a_{nn}}$$
   Y las demás variables $x_i$ (desde $i = n-1$ hasta $1$) se despejan iterativamente:
   $$x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij}x_j}{a_{ii}}$$

### Ejercicio Resuelto
**Enunciado:** Resuelve el siguiente sistema de ecuaciones de $3 \times 3$:
$$2x + y - z = 8$$
$$-3x - y + 2z = -11$$
$$-2x + y + 2z = -3$$

**Solución paso a paso:**
**1. Construir la matriz aumentada $[A|b]$:**
$$
\begin{bmatrix}
 2 &  1 & -1 & | &  8 \\
-3 & -1 &  2 & | & -11 \\
-2 &  1 &  2 & | & -3
\end{bmatrix}
$$

**2. Eliminación hacia adelante (hacer ceros debajo del $2$ en la columna 1):**
* Para $F_2$, el factor es $m = \frac{-3}{2} = -1.5$. Operación: $F_2 \leftarrow F_2 - (-1.5)F_1$
  Nuevos valores de $F_2$: $[-3 - (-3), \ -1 - (-1.5), \ 2 - (1.5) \ | \ -11 - (-12)] = [0, 0.5, 0.5 \ | \ 1]$
* Para $F_3$, el factor es $m = \frac{-2}{2} = -1$. Operación: $F_3 \leftarrow F_3 - (-1)F_1$
  Nuevos valores de $F_3$: $[-2 - (-2), \ 1 - (-1), \ 2 - (1) \ | \ -3 - (-8)] = [0, 2, 1 \ | \ 5]$

Nuestra matriz ahora es:
$$
\begin{bmatrix}
2 & 1 & -1 & | & 8 \\
0 & 0.5 & 0.5 & | & 1 \\
0 & 2 & 1 & | & 5
\end{bmatrix}
$$

**3. Continuar la eliminación (hacer ceros debajo del $0.5$ en la columna 2):**
* Para la nueva $F_3$, el factor es $m = \frac{2}{0.5} = 4$. Operación: $F_3 \leftarrow F_3 - 4F_2$
  Nuevos valores de $F_3$: $[0-0, \ 2 - 4(0.5), \ 1 - 4(0.5) \ | \ 5 - 4(1)] = [0, 0, -1 \ | \ 1]$

Nuestra **matriz triangular superior** final es:
$$
\begin{bmatrix}
2 & 1 & -1 & | & 8 \\
0 & 0.5 & 0.5 & | & 1 \\
0 & 0 & -1 & | & 1
\end{bmatrix}
$$

**4. Sustitución hacia atrás:**
* De la fila 3: $-1z = 1 \implies z = -1$
* De la fila 2: $0.5y + 0.5(-1) = 1 \implies 0.5y - 0.5 = 1 \implies 0.5y = 1.5 \implies y = 3$
* De la fila 1: $2x + (3) - (-1) = 8 \implies 2x + 4 = 8 \implies 2x = 4 \implies x = 2$

**Resultado final:** La solución al sistema es **$x = 2$, $y = 3$, $z = -1$**.

### Código
[eliminacion_gaussiana2.py](../3-Codigos/eliminacion_gaussiana2.py)

## Método de Gauss-Seidel

### Teoría y Fundamentación Matemática
El método de Gauss-Seidel es un **algoritmo iterativo** utilizado para resolver sistemas de ecuaciones lineales de la forma $Ax = b$. A diferencia de los métodos directos (como la eliminación gaussiana), este método no busca transformar la matriz, sino que parte de una aproximación inicial para las incógnitas (por ejemplo, comenzar asumiendo que todas valen cero) y va refinando los valores ciclo tras ciclo hasta aproximarse a la solución real.

Es una evolución directa del *Método de Jacobi*. La gran mejora de Gauss-Seidel radica en que **utiliza los nuevos valores de las variables inmediatamente después de ser calculados**, en lugar de esperar a que termine toda la iteración completa. Esto acelera significativamente la velocidad de convergencia.

**Criterio de Convergencia:** Para garantizar que el método converja (no se vuelva infinito), la matriz de coeficientes $A$ idealmente debe ser **estrictamente dominante por diagonal**. Esto significa que en cada fila, el valor absoluto del elemento de la diagonal principal debe ser mayor que la suma de los valores absolutos de los demás elementos de esa misma fila:
$$|a_{ii}| > \sum_{j \neq i} |a_{ij}|$$

### Fórmulas y Criterios
Para un sistema de $n$ ecuaciones, se despeja la variable correspondiente a la diagonal principal de cada ecuación ($x_i$). 

1. **Fórmula de iteración:**
   En la iteración $k+1$, el cálculo de la variable $x_i$ se expresa como:
   $$x_i^{(k+1)} = \frac{b_i - \sum_{j=1}^{i-1} a_{ij}x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij}x_j^{(k)}}{a_{ii}}$$
   *Nota: Fíjate cómo las variables desde $j=1$ hasta $i-1$ ya usan el superíndice $(k+1)$ porque acaban de ser actualizadas en esta misma iteración.*

2. **Criterio de paro (Tolerancia):**
   El algoritmo se detiene cuando el cambio máximo entre todas las variables de una iteración a otra es menor que la tolerancia permitida:
   $$\max_{1 \le i \le n} |x_i^{(k+1)} - x_i^{(k)}| \le tol$$

### Ejercicio Resuelto
**Enunciado:** Resuelve el siguiente sistema empleando el método de Gauss-Seidel con un vector inicial $x^{(0)} = [0, 0, 0]^T$. Realiza 2 iteraciones.
$$4x_1 - x_2 = 3$$
$$-x_1 + 4x_2 - x_3 = 2$$
$$-x_2 + 4x_3 = 3$$

*(Nota: El sistema es estrictamente dominante por diagonal ya que $4 > |-1|$, $4 > |-1|+|-1|$ y $4 > |-1|$).*

**Solución paso a paso:**
**1. Despejar las incógnitas de la diagonal principal:**
   * De la ec. 1: $x_1 = \frac{3 + x_2}{4}$
   * De la ec. 2: $x_2 = \frac{2 + x_1 + x_3}{4}$
   * De la ec. 3: $x_3 = \frac{3 + x_2}{4}$

**2. Iteración 1 (usando valores iniciales $x_1=0, x_2=0, x_3=0$):**
   * **Calcular $x_1$:** Usamos el valor actual de $x_2$:
     $$x_1^{(1)} = \frac{3 + 0}{4} = 0.75$$
   * **Calcular $x_2$:** Usamos el **nuevo** $x_1=0.75$ y el viejo $x_3=0$:
     $$x_2^{(1)} = \frac{2 + 0.75 + 0}{4} = \frac{2.75}{4} = 0.6875$$
   * **Calcular $x_3$:** Usamos el **nuevo** $x_2=0.6875$:
     $$x_3^{(1)} = \frac{3 + 0.6875}{4} = \frac{3.6875}{4} = 0.921875$$
   * *Vector resultante en Iteración 1:* $x^{(1)} = [0.75, \ 0.6875, \ 0.9219]$

**3. Iteración 2 (usando los resultados de la Iteración 1):**
   * **Calcular $x_1$:** Usamos $x_2=0.6875$:
     $$x_1^{(2)} = \frac{3 + 0.6875}{4} = \frac{3.6875}{4} = 0.921875$$
   * **Calcular $x_2$:** Usamos el nuevo $x_1=0.921875$ y el $x_3=0.921875$ anterior:
     $$x_2^{(2)} = \frac{2 + 0.921875 + 0.921875}{4} = \frac{3.84375}{4} = 0.9609375$$
   * **Calcular $x_3$:** Usamos el nuevo $x_2=0.9609375$:
     $$x_3^{(2)} = \frac{3 + 0.9609375}{4} = \frac{3.9609375}{4} = 0.990234375$$
   * *Vector resultante en Iteración 2:* $x^{(2)} = [0.9219, \ 0.9609, \ 0.9902]$

**Resultado tras 2 iteraciones:** Las aproximaciones son muy cercanas a la solución analítica exacta, la cual es $x = [1, 1, 1]^T$.
### Código
 [Gauss-Seidel.py](../3-Codigos/Gauss-Seidel.py)
 
 ## Método de Gauss-Jordan

### Teoría y Fundamentación Matemática
El método de Gauss-Jordan es una variante y extensión directa del método de Eliminación Gaussiana. Al igual que su predecesor, es un **método directo** que utiliza operaciones elementales de fila sobre una matriz aumentada para resolver sistemas de ecuaciones lineales de la forma $Ax = b$.

La diferencia fundamental radica en su objetivo final: mientras que la eliminación gaussiana se detiene al lograr una matriz triangular superior (requiriendo un proceso de sustitución hacia atrás para encontrar las variables), **Gauss-Jordan continúa operando hasta convertir la matriz de coeficientes en una matriz identidad** (unos en la diagonal principal y ceros en el resto).

Al lograr la matriz identidad, los valores de las incógnitas quedan directamente despejados en el vector de resultados, eliminando por completo la necesidad de la sustitución hacia atrás. Aunque computacionalmente requiere aproximadamente un 50% más de operaciones matemáticas que la eliminación gaussiana clásica, Gauss-Jordan es el método por excelencia cuando se necesita calcular la **matriz inversa** de un sistema.

### Fórmulas y Criterios
El procedimiento se realiza columna por columna (desde $i = 1$ hasta $n$), aplicando dos pasos obligatorios por cada columna:

1. **Normalización del Pivote:**
   Se divide toda la fila actual (pivote) entre el valor del elemento de la diagonal principal para convertirlo en $1$:
   $$F_i \leftarrow \frac{F_i}{a_{ii}}$$

2. **Eliminación Total (Arriba y Abajo):**
   Se hacen ceros todos los demás elementos de la columna actual, **tanto por debajo como por encima** del pivote, restando a cada fila un múltiplo de la fila pivote:
   $$F_j \leftarrow F_j - a_{ji} \cdot F_i \quad \text{para todo } j \neq i$$

### Ejercicio Resuelto
**Enunciado:** Resuelve el mismo sistema de ecuaciones utilizado en Gauss, pero ahora con el método de Gauss-Jordan:
$$2x + y - z = 8$$
$$-3x - y + 2z = -11$$
$$-2x + y + 2z = -3$$

**Solución paso a paso:**
**1. Construir la matriz aumentada:**
$$
\begin{bmatrix}
 2 &  1 & -1 & | &  8 \\
-3 & -1 &  2 & | & -11 \\
-2 &  1 &  2 & | & -3
\end{bmatrix}
$$

**2. Trabajar la Columna 1:**
* **Normalizar pivote (Fila 1):** Dividimos entre $2$.
  Nuevos valores $F_1$: $[1, \ 0.5, \ -0.5 \ | \ 4]$
* **Eliminar en Fila 2 y Fila 3:**
  $F_2 \leftarrow F_2 - (-3)F_1 \implies [-3+3, \ -1+1.5, \ 2-1.5 \ | \ -11+12] = [0, \ 0.5, \ 0.5 \ | \ 1]$
  $F_3 \leftarrow F_3 - (-2)F_1 \implies [-2+2, \ 1+1, \ 2-1 \ | \ -3+8] = [0, \ 2, \ 1 \ | \ 5]$

Matriz resultante (Fase 1):
$$
\begin{bmatrix}
1 & 0.5 & -0.5 & | & 4 \\
0 & 0.5 & 0.5 & | & 1 \\
0 & 2 & 1 & | & 5
\end{bmatrix}
$$

**3. Trabajar la Columna 2:**
* **Normalizar pivote (Fila 2):** Dividimos entre $0.5$ (o multiplicamos por 2).
  Nuevos valores $F_2$: $[0, \ 1, \ 1 \ | \ 2]$
* **Eliminar arriba (Fila 1) y abajo (Fila 3):**
  $F_1 \leftarrow F_1 - (0.5)F_2 \implies [1-0, \ 0.5-0.5, \ -0.5-0.5 \ | \ 4-1] = [1, \ 0, \ -1 \ | \ 3]$
  $F_3 \leftarrow F_3 - (2)F_2 \implies [0-0, \ 2-2, \ 1-2 \ | \ 5-4] = [0, \ 0, \ -1 \ | \ 1]$

Matriz resultante (Fase 2):
$$
\begin{bmatrix}
1 & 0 & -1 & | & 3 \\
0 & 1 & 1 & | & 2 \\
0 & 0 & -1 & | & 1
\end{bmatrix}
$$

**4. Trabajar la Columna 3:**
* **Normalizar pivote (Fila 3):** Dividimos entre $-1$.
  Nuevos valores $F_3$: $[0, \ 0, \ 1 \ | \ -1]$
* **Eliminar arriba (Fila 1 y Fila 2):**
  $F_1 \leftarrow F_1 - (-1)F_3 \implies [1, \ 0, \ -1+1 \ | \ 3-1] = [1, \ 0, \ 0 \ | \ 2]$
  $F_2 \leftarrow F_2 - (1)F_3 \implies [0, \ 1, \ 1-1 \ | \ 2-(-1)] = [0, \ 1, \ 0 \ | \ 3]$

**Matriz Identidad Final:**
$$
\begin{bmatrix}
1 & 0 & 0 & | & 2 \\
0 & 1 & 0 & | & 3 \\
0 & 0 & 1 & | & -1
\end{bmatrix}
$$

**Resultado final:** Sin necesidad de sustitución hacia atrás, la columna de resultados nos da directamente la solución: **$x = 2$, $y = 3$, $z = -1$**.

---
### Código
[GaussJordan.py](../3-Codigos/GaussJordan.py)

## Método de Jacobi

### Teoría y Fundamentación Matemática
El método de Jacobi es un **algoritmo iterativo** para resolver sistemas de ecuaciones lineales de la forma $Ax = b$. Al igual que Gauss-Seidel, requiere que la matriz de coeficientes sea preferentemente **estrictamente dominante por diagonal** para asegurar su convergencia.

La diferencia fundamental entre Jacobi y Gauss-Seidel es la forma en que se actualizan las variables. En el método de Jacobi, para calcular los valores de la iteración actual ($k+1$), **se utilizan única y exclusivamente los valores de la iteración anterior ($k$)**. 

Esto significa que no se actualizan las variables "en tiempo real" durante el ciclo. Aunque esto hace que su convergencia sea más lenta comparada con Gauss-Seidel, tiene una gran ventaja computacional: los cálculos de cada variable son completamente independientes entre sí, lo que hace que este método sea ideal para el **procesamiento en paralelo**.

### Fórmulas y Criterios
Para un sistema de $n$ ecuaciones, se despeja la variable correspondiente a la diagonal principal de cada ecuación ($x_i$).

1. **Fórmula de iteración:**
   En la iteración $k+1$, el cálculo de la variable $x_i$ se expresa como:
   $$x_i^{(k+1)} = \frac{b_i - \sum_{j \neq i} a_{ij}x_j^{(k)}}{a_{ii}}$$
   *Nota: Observa que todas las variables del lado derecho de la ecuación usan el superíndice $(k)$, es decir, pertenecen estrictamente a la iteración pasada.*

2. **Criterio de paro (Tolerancia):**
   El proceso se detiene cuando la máxima diferencia absoluta entre los valores nuevos y los anteriores es menor que la tolerancia fijada:
   $$\max_{1 \le i \le n} |x_i^{(k+1)} - x_i^{(k)}| \le tol$$

### Ejercicio Resuelto
**Enunciado:** Resuelve el siguiente sistema empleando el método de Jacobi con un vector inicial $x^{(0)} = [0, 0, 0]^T$. Realiza 2 iteraciones. *(Es el mismo sistema usado en Gauss-Seidel para que notes la diferencia en los resultados intermedios).*
$$4x_1 - x_2 = 3$$
$$-x_1 + 4x_2 - x_3 = 2$$
$$-x_2 + 4x_3 = 3$$

**Solución paso a paso:**
**1. Despejar las incógnitas de la diagonal principal:**
   * $x_1 = \frac{3 + x_2}{4}$
   * $x_2 = \frac{2 + x_1 + x_3}{4}$
   * $x_3 = \frac{3 + x_2}{4}$

**2. Iteración 1 (usando valores iniciales $x^{(0)} = [0, 0, 0]$):**
   * **Calcular $x_1^{(1)}$:** $x_1^{(1)} = \frac{3 + 0}{4} = 0.75$
   * **Calcular $x_2^{(1)}$:** $x_2^{(1)} = \frac{2 + 0 + 0}{4} = 0.5$
   * **Calcular $x_3^{(1)}$:** $x_3^{(1)} = \frac{3 + 0}{4} = 0.75$
   * *Vector resultante en Iteración 1:* $x^{(1)} = [0.75, \ 0.5, \ 0.75]$
   *(Nota cómo en Gauss-Seidel el valor de $x_2$ daba 0.6875 porque usaba el nuevo $x_1$. Aquí, usamos los ceros iniciales para todos).*

**3. Iteración 2 (usando los resultados de la Iteración 1):**
   * **Calcular $x_1^{(2)}$:** Usamos $x_2^{(1)} = 0.5$:
     $$x_1^{(2)} = \frac{3 + 0.5}{4} = \frac{3.5}{4} = 0.875$$
   * **Calcular $x_2^{(2)}$:** Usamos $x_1^{(1)} = 0.75$ y $x_3^{(1)} = 0.75$:
     $$x_2^{(2)} = \frac{2 + 0.75 + 0.75}{4} = \frac{3.5}{4} = 0.875$$
   * **Calcular $x_3^{(2)}$:** Usamos $x_2^{(1)} = 0.5$:
     $$x_3^{(2)} = \frac{3 + 0.5}{4} = \frac{3.5}{4} = 0.875$$
   * *Vector resultante en Iteración 2:* $x^{(2)} = [0.875, \ 0.875, \ 0.875]$

**Resultado tras 2 iteraciones:** Se observa cómo los valores se van acercando uniformemente a la solución analítica $x = [1, 1, 1]^T$, aunque un poco más lento que con Gauss-Seidel.

---
### Código
[Jacobi.py](../3-Codigos/Jacobi.py)

Problemario Unidad 3 Esteban Romero Pérez
 > [!NOTE]
> Link de problemario
https://drive.google.com/file/d/1Rq9Q2qoK5nQ9JtzqtupkDXnKjnEdOZk-/view?usp=drive_link
