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
