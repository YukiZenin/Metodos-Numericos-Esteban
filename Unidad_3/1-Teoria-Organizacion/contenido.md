## Eliminación Gaussiana

### Naturaleza y Fundamento Matemático
La eliminación gaussiana es un método directo (no iterativo) del álgebra lineal utilizado para resolver sistemas de ecuaciones lineales de la forma $Ax = b$, encontrar el rango de una matriz o calcular su inversa. A diferencia de los métodos de aproximación de raíces, este algoritmo llega a la solución exacta (salvo errores de redondeo de punto flotante) en un número finito y predecible de pasos.

El método consiste en operar sobre la **matriz aumentada** (la matriz de coeficientes $A$ junto con el vector de términos independientes $b$) aplicando operaciones elementales de fila. El objetivo es transformar la matriz original en una **matriz triangular superior** (donde todos los elementos por debajo de la diagonal principal son cero). Una vez lograda esta estructura, las incógnitas se despejan fácilmente desde la última hasta la primera mediante un proceso llamado **sustitución hacia atrás**.

### Fórmulas y Operaciones

El algoritmo se divide en dos fases matemáticas principales:

1. **Eliminación hacia adelante:** Para eliminar el elemento en la fila $i$ usando la fila pivote $j$, se aplica la siguiente operación a toda la fila:
$$R_i \leftarrow R_i - \left( \frac{a_{ij}}{a_{jj}} \right) R_j$$
*(Donde $R_i$ es la fila actual, $R_j$ es la fila pivote, y $\frac{a_{ij}}{a_{jj}}$ es el factor de eliminación).*

2. **Sustitución hacia atrás:**
Una vez que la matriz es triangular superior, las variables $x_i$ se calculan con la fórmula:
$$x_i = \frac{1}{a_{ii}} \left( b_i - \sum_{j=i+1}^{n} a_{ij} x_j \right)$$

### Ejemplo Paso a Paso

Supongamos el siguiente sistema de 3 ecuaciones:
$$2x + y - z = 8$$
$$-3x - y + 2z = -11$$
$$-2x + y + 2z = -3$$

**Paso 1: Construir la matriz aumentada**
$$\begin{bmatrix} 2 & 1 & -1 & | & 8 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}$$

**Paso 2: Eliminación hacia adelante (Hacer ceros debajo de la diagonal)**
Usamos el pivote $a_{11} = 2$ para eliminar el $-3$ y el $-2$ de la primera columna. 
- Fila 2: $R_2 \leftarrow R_2 - \left(\frac{-3}{2}\right) R_1$
- Fila 3: $R_3 \leftarrow R_3 - \left(\frac{-2}{2}\right) R_1$

Matriz resultante:
$$\begin{bmatrix} 2 & 1 & -1 & | & 8 \\ 0 & 0.5 & 0.5 & | & 1 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}$$

Ahora usamos el pivote $a_{22} = 0.5$ para eliminar el $2$ de la segunda columna.
- Fila 3: $R_3 \leftarrow R_3 - \left(\frac{2}{0.5}\right) R_2$

Matriz triangular superior resultante:
$$\begin{bmatrix} 2 & 1 & -1 & | & 8 \\ 0 & 0.5 & 0.5 & | & 1 \\ 0 & 0 & -1 & | & 1 \end{bmatrix}$$

**Paso 3: Sustitución hacia atrás**
- De la 3ra fila: $-1z = 1 \implies z = -1$
- De la 2da fila: $0.5y + 0.5(-1) = 1 \implies 0.5y = 1.5 \implies y = 3$
- De la 1ra fila: $2x + 1(3) - 1(-1) = 8 \implies 2x + 4 = 8 \implies x = 2$

**Solución exacta:** $x = 2$, $y = 3$, $z = -1$.

### Código
[eliminacion_gaussiana2.py](../3-Codigos/eliminacion_gaussiana2.py)

## Método de Gauss-Seidel

### Naturaleza y Fundamento Matemático
A diferencia de la Eliminación Gaussiana, que es un método directo, el método de Gauss-Seidel es un **método iterativo** para resolver sistemas de ecuaciones lineales. Es una versión optimizada y acelerada del método de Jacobi. 

El fundamento de los métodos iterativos es comenzar con una aproximación inicial (usualmente ceros) para todas las variables y refinar esos valores ciclo tras ciclo hasta que la diferencia entre una iteración y la anterior sea imperceptible (menor a una tolerancia). La brillantez de Gauss-Seidel radica en que **utiliza los valores calculados más recientes de inmediato**. En lugar de esperar a que termine toda la iteración para actualizar las variables (como hace Jacobi), Gauss-Seidel sustituye las variables recién descubiertas en las ecuaciones de la misma iteración, lo que acelera dramáticamente la convergencia hacia la respuesta exacta.

Para que este método garantice su convergencia, la matriz de coeficientes debe ser preferentemente **estrictamente diagonal dominante** (el valor absoluto del coeficiente en la diagonal principal de cada fila debe ser mayor que la suma de los valores absolutos del resto de coeficientes de esa misma fila).

### Fórmulas y Operaciones
El sistema $Ax = b$ se reescribe despejando la incógnita de la diagonal principal para cada ecuación. La fórmula general para calcular el valor de la incógnita $x_i$ en la iteración actual $(k+1)$ es:

$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} x_j^{(k)} \right)$$

*Nota matemática: Observa cómo la primera sumatoria utiliza $x_j^{(k+1)}$ (valores ya actualizados en la iteración actual), mientras que la segunda sumatoria usa $x_j^{(k)}$ (valores viejos de la iteración anterior, porque aún no se han calculado los nuevos).*

### Ejemplo Paso a Paso

Dado el sistema de ecuaciones (que es diagonalmente dominante):
$$4x - y + z = 7$$
$$4x - 8y + z = -21$$
$$-2x + y + 5z = 15$$

**Paso 1: Despejar cada variable de la diagonal principal**
- De la ec. 1: $x = \frac{7 + y - z}{4}$
- De la ec. 2: $y = \frac{-21 - 4x - z}{-8} = \frac{21 + 4x + z}{8}$
- De la ec. 3: $z = \frac{15 + 2x - y}{5}$

**Paso 2: Iteración 1 (Partiendo de $x=0, y=0, z=0$)**
- Calculamos $x$ usando los valores viejos de $y, z$:
  $x^{(1)} = \frac{7 + 0 - 0}{4} = 1.75$
- Calculamos $y$ usando el **nuevo** valor de $x$ y el viejo de $z$:
  $y^{(1)} = \frac{21 + 4(1.75) + 0}{8} = \frac{21 + 7}{8} = 3.5$
- Calculamos $z$ usando los **nuevos** valores de $x$ y $y$:
  $z^{(1)} = \frac{15 + 2(1.75) - 3.5}{5} = \frac{15 + 3.5 - 3.5}{5} = 3.0$

Después de solo una iteración, nuestra aproximación es $(1.75, 3.5, 3.0)$. 
Si continuamos iterando, los valores se estabilizarán velozmente en la solución exacta: $x = 2$, $y = 4$, $z = 3$.

### Código
 [Gauss-Seidel.py](../3-Codigos/Gauss-Seidel.py)
 ## Método de Gauss-Jordan

### Naturaleza y Fundamento Matemático
El método de Gauss-Jordan es una variación directa del método de eliminación gaussiana. También se clasifica como un método directo para resolver sistemas de ecuaciones lineales de la forma $Ax = b$. La diferencia fundamental radica en que, en lugar de reducir la matriz aumentada a una forma triangular superior y luego aplicar la sustitución hacia atrás, el método de Gauss-Jordan continúa la eliminación de coeficientes tanto por debajo como por encima de cada elemento pivote.

El objetivo final de este algoritmo es transformar la matriz de coeficientes $A$ directamente en la **matriz identidad** ($I$). Al alcanzar esta estructura balanceada de unos en la diagonal principal y ceros en el resto de las posiciones, el vector de términos independientes $b$ se transforma automáticamente en el vector solución del sistema, eliminando por completo la necesidad de realizar sustituciones hacia atrás.

### Fórmulas y Operaciones

A lo largo del algoritmo se ejecutan dos operaciones elementales por fila en cada columna $j$:

1. **Normalización de la fila pivote:** Se divide toda la fila pivote $R_j$ entre su elemento diagonal $a_{jj}$ para transformarlo estrictamente en 1:
$$R_j \leftarrow \frac{R_j}{a_{jj}}$$

2. **Eliminación en todas las demás filas:** Para cualquier fila $i$ que no sea la fila pivote ($i \neq j$), se elimina el coeficiente de la columna correspondiente aplicando:
$$R_i \leftarrow R_i - a_{ij} R_j$$

### Ejemplo Paso a Paso

Resolveremos el mismo sistema tridimensional para observar la transición operativa de este método:
$$2x + y - z = 8$$
$$-3x - y + 2z = -11$$
$$-2x + y + 2z = -3$$

**Paso 1: Construcción de la matriz aumentada inicial**
$$\begin{bmatrix} 2 & 1 & -1 & | & 8 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}$$

**Paso 2: Procesar la Columna 1**
Normalizamos la Fila 1 dividiendo entre su propio pivote ($a_{11} = 2$):
$$\begin{bmatrix} 1 & 0.5 & -0.5 & | & 4 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}$$
Anulamos los elementos de las filas 2 y 3 en la primera columna:
- $R_2 \leftarrow R_2 - (-3)R_1$
- $R_3 \leftarrow R_3 - (-2)R_1$
$$\begin{bmatrix} 1 & 0.5 & -0.5 & | & 4 \\ 0 & 0.5 & 0.5 & | & 1 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}$$

**Paso 3: Procesar la Columna 2**
Normalizamos la Fila 2 dividiendo entre su nuevo pivote ($a_{22} = 0.5$):
$$\begin{bmatrix} 1 & 0.5 & -0.5 & | & 4 \\ 0 & 1 & 1 & | & 2 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}$$
Anulamos los elementos de las columnas restantes en las filas 1 y 3:
- $R_1 \leftarrow R_1 - (0.5)R_2$
- $R_3 \leftarrow R_3 - (2)R_2$
$$\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & -1 & | & 1 \end{bmatrix}$$

**Paso 4: Procesar la Columna 3**
Normalizamos la Fila 3 dividiendo entre su pivote final ($a_{33} = -1$):
$$\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & 1 & | & -1 \end{bmatrix}$$
Anulamos los elementos superiores en las filas 1 y 2:
- $R_1 \leftarrow R_1 - (-1)R_3$
- $R_2 \leftarrow R_2 - (1)R_3$
$$\begin{bmatrix} 1 & 0 & 0 & | & 2 \\ 0 & 1 & 0 & | & 3 \\ 0 & 0 & 1 & | & -1 \end{bmatrix}$$

**Solución directa obtenida del vector b:** $x = 2$, $y = 3$, $z = -1$.

### Código
[GaussJordan.py](../3-Codigos/GaussJordan.py)

## Método de Jacobi

### Naturaleza y Fundamento Matemático
El método de Jacobi es un **método iterativo** clásico para resolver sistemas de ecuaciones lineales de la forma $Ax = b$. Al igual que Gauss-Seidel, requiere que se parta de una aproximación inicial (generalmente un vector de ceros) y va refinando los resultados en cada ciclo hasta alcanzar una convergencia dentro de un margen de tolerancia. También exige que la matriz de coeficientes sea preferentemente diagonal dominante para asegurar que el algoritmo converja y no diverja hacia el infinito.

La diferencia fundamental (y su principal desventaja) frente a Gauss-Seidel radica en **cómo actualiza las variables**. En el método de Jacobi, los nuevos valores calculados en la iteración actual no se utilizan inmediatamente; se guardan en un vector temporal. Para calcular cualquier variable en el ciclo actual, el algoritmo está forzado a usar **únicamente los valores viejos** del ciclo anterior. Una vez que se terminan de calcular todas las variables, el vector viejo se reemplaza por completo con el vector nuevo. Esto hace que converja más lentamente que Gauss-Seidel.

### Fórmulas y Operaciones
El sistema se despeja dejando sola a la variable de la diagonal principal para cada ecuación. La fórmula general para calcular el valor de la incógnita $x_i$ en la nueva iteración $(k+1)$ es:

$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1, j \neq i}^{n} a_{ij} x_j^{(k)} \right)$$

*Nota matemática: Observa que toda la sumatoria utiliza exclusivamente $x_j^{(k)}$ (los valores de la iteración pasada), a diferencia de Gauss-Seidel que mezcla iteraciones.*

### Ejemplo Paso a Paso

Utilizaremos el mismo sistema del método anterior para notar la diferencia de velocidad:
$$4x - y + z = 7$$
$$4x - 8y + z = -21$$
$$-2x + y + 5z = 15$$

**Paso 1: Despejar cada variable de la diagonal principal**
- $x = \frac{7 + y - z}{4}$
- $y = \frac{21 + 4x + z}{8}$
- $z = \frac{15 + 2x - y}{5}$

**Paso 2: Iteración 1 (Partiendo de $x^{(0)}=0, y^{(0)}=0, z^{(0)}=0$)**
- Calculamos $x$ usando los valores viejos (0 y 0):
  $x^{(1)} = \frac{7 + 0 - 0}{4} = 1.75$
- Calculamos $y$ usando los valores viejos de $x$ y $z$ (0 y 0) *(Nota: No usamos el 1.75 aquí)*:
  $y^{(1)} = \frac{21 + 4(0) + 0}{8} = 2.625$
- Calculamos $z$ usando los valores viejos de $x$ y $y$ (0 y 0):
  $z^{(1)} = \frac{15 + 2(0) - 0}{5} = 3.0$

Al finalizar la iteración 1, nuestra aproximación es $(1.75, 2.625, 3.0)$. 
Comparado con Gauss-Seidel que logró $(1.75, 3.5, 3.0)$ en el mismo tiempo, Jacobi está un poco más atrasado en acercarse a la solución real exacta ($x=2, y=4, z=3$), por lo que requerirá más iteraciones computacionales.

### Código
[Jacobi.py](../3-Codigos/Jacobi.py)
