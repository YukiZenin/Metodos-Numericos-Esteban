## Diferenciación Numérica: Regla de los 3 Puntos

### Teoría y Fundamentación Matemática
La derivación numérica se utiliza para aproximar la derivada de una función $f'(x)$ cuando solo disponemos de un conjunto de datos discretos (una tabla de valores) o cuando la función matemática es demasiado compleja para derivarse analíticamente.

Las **fórmulas de 3 puntos** mejoran sustancialmente la precisión de las diferencias finitas básicas (que usan solo 2 puntos). Como su nombre indica, evalúan la función en tres puntos equiespaciados por una distancia $h$. Existen dos variantes principales:
1. **Regla del punto medio (Diferencia Central):** Aproxima la derivada evaluando un punto hacia adelante y un punto hacia atrás del valor objetivo. Es la más exacta de todas.
2. **Regla del extremo (Diferencias Progresivas/Regresivas):** Evalúa el punto objetivo y dos puntos sucesivos (hacia adelante o hacia atrás). Es indispensable usarla en los "bordes" de una tabla de datos, donde es imposible mirar hacia atrás (o hacia adelante) porque no hay más registros.

### Fórmulas y Criterios
Dado un punto objetivo $x_0$ y un tamaño de paso $h$:

1. **Fórmula de 3 puntos en el punto medio (Central):**
   $$f'(x_0) \approx \frac{f(x_0 + h) - f(x_0 - h)}{2h}$$

2. **Fórmula de 3 puntos en el extremo (Progresiva):**
   *(Se usa para evaluar el primer punto de un conjunto de datos)*
   $$f'(x_0) \approx \frac{-3f(x_0) + 4f(x_0 + h) - f(x_0 + 2h)}{2h}$$

*Nota: Para la fórmula regresiva (último punto de los datos), se utiliza la misma estructura progresiva pero asumiendo un valor de $h$ negativo.*

### Ejercicio Resuelto
**Enunciado:** Aproxima la primera derivada de la función $f(x) = x e^x$ en el punto $x_0 = 2.0$, utilizando un tamaño de paso $h = 0.1$. Calcula tanto la fórmula del punto medio como la del extremo progresivo y compáralas con el valor analítico exacto.

**Solución paso a paso:**
**1. Preparación y evaluación de puntos:**
   Calculamos los valores de la función alrededor de $x = 2.0$:
   * $f(1.9) = 1.9 e^{1.9} = 12.7032$
   * $f(2.0) = 2.0 e^{2.0} = 14.7781$
   * $f(2.1) = 2.1 e^{2.1} = 17.1490$
   * $f(2.2) = 2.2 e^{2.2} = 19.8550$

**2. Valor Real (Analítico):**
   La derivada de $x e^x$ es $f'(x) = e^x(x + 1)$.
   Evaluando en 2.0: $f'(2.0) = e^{2.0}(2 + 1) = 3(7.3891) = \mathbf{22.1672}$

**3. Aproximación con la Regla del Punto Medio (Central):**
   Usamos $x_0 = 2.0$, por lo que necesitamos los valores en $1.9$ y $2.1$:
   $$f'(2.0) \approx \frac{f(2.1) - f(1.9)}{2(0.1)}$$
   $$f'(2.0) \approx \frac{17.1490 - 12.7032}{0.2} = \frac{4.4458}{0.2} = \mathbf{22.2290}$$
   *(Error absoluto aproximado: $0.0618$)*

**4. Aproximación con la Regla del Extremo (Progresiva):**
   Usamos $x_0 = 2.0$, por lo que necesitamos los valores hacia adelante ($2.0$, $2.1$ y $2.2$):
   $$f'(2.0) \approx \frac{-3f(2.0) + 4f(2.1) - f(2.2)}{2(0.1)}$$
   $$f'(2.0) \approx \frac{-3(14.7781) + 4(17.1490) - 19.8550}{0.2}$$
   $$f'(2.0) \approx \frac{-44.3343 + 68.5960 - 19.8550}{0.2} = \frac{4.4067}{0.2} = \mathbf{22.0335}$$
   *(Error absoluto aproximado: $0.1337$)*

**Conclusión:** Como dicta la teoría, la regla del punto medio ofrece una mejor aproximación a la derivada real que la regla del extremo al poseer un menor error de truncamiento.
### Código
[Regla3puntos.py](../3-Codigos/Regla3puntos.py)

## Regla de Simpson 1/3



### Teoría y Fundamentación Matemática
La integración numérica busca aproximar el valor de una integral definida $\int_a^b f(x) dx$ calculando el área bajo la curva de la función. Mientras que la regla del trapecio une los puntos de la función con líneas rectas, la **Regla de Simpson 1/3** los une utilizando **parábolas** (polinomios de segundo grado).

Al utilizar una curva en lugar de una recta para ajustarse al contorno de la función original, este método logra una precisión mucho mayor. Para trazar una parábola se necesitan exactamente tres puntos, lo que significa que el intervalo a evaluar debe dividirse en dos subintervalos iguales. 

Cuando el área total a evaluar es muy grande, se utiliza la **Regla de Simpson 1/3 Compuesta**, que consiste en aplicar el método repetidas veces a lo largo de toda la función. La condición más importante de este método es que el número total de subintervalos ($n$) **debe ser un número par**. El "1/3" en su nombre proviene del factor $h/3$ que aparece al resolver analíticamente la integral de la parábola.

### Fórmulas y Criterios
Dado un intervalo de integración $[a, b]$ dividido en $n$ subintervalos (donde $n$ es par):

1. **Tamaño del paso ($h$):**
   La distancia entre cada punto evaluado (ancho de cada subintervalo) es:
   $$h = \frac{b - a}{n}$$

2. **Fórmula de Simpson 1/3 Compuesta:**
   Para aproximar la integral, se evalúa la función en los puntos $x_0, x_1, x_2, \dots, x_n$ y se aplica la siguiente ponderación:
   $$\int_a^b f(x) dx \approx \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1,3,5...}^{n-1} f(x_i) + 2 \sum_{j=2,4,6...}^{n-2} f(x_j) + f(x_n) \right]$$
   
   *En palabras simples:* Se suman el primer y último punto, más **4 veces** la suma de los puntos en posiciones impares, más **2 veces** la suma de los puntos en posiciones pares; todo esto multiplicado por $h/3$.

### Ejercicio Resuelto
**Enunciado:** Aproxima la integral de la función $f(x) = \frac{1}{x}$ en el intervalo $[1, 3]$ utilizando la Regla de Simpson 1/3 con $n = 4$ subintervalos.

**Solución paso a paso:**
**1. Verificación y cálculo del tamaño de paso ($h$):**
   * El número de subintervalos $n = 4$ es par, por lo que podemos usar el método.
   * Calculamos $h$:
     $$h = \frac{3 - 1}{4} = \frac{2}{4} = 0.5$$

**2. Determinación de los puntos a evaluar ($x_i$):**
   Comenzamos en $a = 1$ y avanzamos de $0.5$ en $0.5$ hasta llegar a $b = 3$.
   * $x_0 = 1.0$
   * $x_1 = 1.5$ (Impar)
   * $x_2 = 2.0$ (Par)
   * $x_3 = 2.5$ (Impar)
   * $x_4 = 3.0$

**3. Evaluación de la función $f(x) = \frac{1}{x}$ en cada punto:**
   * $f(x_0) = \frac{1}{1.0} = 1.0000$
   * $f(x_1) = \frac{1}{1.5} = 0.6667$
   * $f(x_2) = \frac{1}{2.0} = 0.5000$
   * $f(x_3) = \frac{1}{2.5} = 0.4000$
   * $f(x_4) = \frac{1}{3.0} = 0.3333$

**4. Aplicación de la fórmula de Simpson 1/3:**
   Agrupamos según la fórmula (extremos solos, impares $\times 4$, pares $\times 2$):
   $$I \approx \frac{0.5}{3} \Big[ f(1.0) + 4 \big( f(1.5) + f(2.5) \big) + 2 \big( f(2.0) \big) + f(3.0) \Big]$$
   $$I \approx \frac{0.5}{3} \Big[ 1.0000 + 4(0.6667 + 0.4000) + 2(0.5000) + 0.3333 \Big]$$
   $$I \approx \frac{0.5}{3} \Big[ 1.0000 + 4(1.0667) + 1.0000 + 0.3333 \Big]$$
   $$I \approx \frac{0.5}{3} \Big[ 1.0000 + 4.2668 + 1.0000 + 0.3333 \Big]$$
   $$I \approx \frac{0.5}{3} [6.6001] \approx 1.1000$$

**Conclusión:** La aproximación numérica es $1.1000$. El valor real de esta integral (que es $\ln(3)$) es aproximadamente $1.0986$. Con solo 4 subintervalos, logramos una exactitud de hasta el segundo decimal (error de apenas $0.0014$).

### Código
[simpson13.py](../3-Codigos/simpson13.py)
## Regla de Simpson 3/8



### Teoría y Fundamentación Matemática
Al igual que la regla de Simpson 1/3 usa una parábola (polinomio de segundo grado) para aproximar la forma de la función, la **Regla de Simpson 3/8** da un paso más allá y utiliza un **polinomio cúbico** (de tercer grado) para unir los puntos.

Para definir una ecuación cúbica se requieren exactamente cuatro puntos. Esto significa que el intervalo a evaluar debe dividirse en **tres subintervalos**. Por consiguiente, si se desea aplicar la Regla de Simpson 3/8 Compuesta a lo largo de un dominio más grande, el número total de subintervalos ($n$) **debe ser un múltiplo de 3** ($3, 6, 9, 12, \dots$).

En la práctica, Simpson 1/3 y Simpson 3/8 tienen una precisión muy similar. Sin embargo, Simpson 3/8 resulta extremadamente útil cuando el número total de subintervalos que tenemos en una tabla de datos es impar, pero no es un múltiplo de 3 (por ejemplo, $n=5$). En esos casos, se suele aplicar Simpson 1/3 en los primeros segmentos pares y se remata con Simpson 3/8 en los últimos tres segmentos.

El "3/8" en su nombre proviene del factor $3h/8$ que aparece al resolver la integral analítica del polinomio cúbico.

### Fórmulas y Criterios
Dado un intervalo de integración $[a, b]$ dividido en $n$ subintervalos (donde $n$ es múltiplo de 3):

1. **Tamaño del paso ($h$):**
   $$h = \frac{b - a}{n}$$

2. **Fórmula de Simpson 3/8 Compuesta:**
   La aproximación de la integral sigue un patrón específico de multiplicadores ($1, 3, 3, 2, 3, 3, 2, \dots, 3, 3, 1$):
   $$\int_a^b f(x) dx \approx \frac{3h}{8} \left[ f(x_0) + 3f(x_1) + 3f(x_2) + 2f(x_3) + 3f(x_4) + 3f(x_5) + \dots + f(x_n) \right]$$
   
   *En palabras simples:* Los puntos extremos se multiplican por 1. Los puntos interiores cuyo subíndice es múltiplo de 3 (como $x_3, x_6, x_9$) se multiplican por **2**. Todos los demás puntos interiores se multiplican por **3**.

### Ejercicio Resuelto
**Enunciado:** Aproxima la integral de la función $f(x) = \frac{1}{x}$ en el intervalo $[1, 4]$ utilizando la Regla de Simpson 3/8 con $n = 3$ subintervalos.

**Solución paso a paso:**
**1. Verificación y cálculo del tamaño de paso ($h$):**
   * El número de subintervalos $n = 3$ es múltiplo de 3, por lo que el método es aplicable.
   * Calculamos $h$:
     $$h = \frac{4 - 1}{3} = \frac{3}{3} = 1.0$$

**2. Determinación de los puntos a evaluar ($x_i$):**
   Comenzamos en $a = 1$ y avanzamos de $1.0$ en $1.0$ hasta llegar a $b = 4$.
   * $x_0 = 1.0$
   * $x_1 = 2.0$ 
   * $x_2 = 3.0$
   * $x_3 = 4.0$

**3. Evaluación de la función $f(x) = \frac{1}{x}$ en cada punto:**
   * $f(1.0) = \frac{1}{1.0} = 1.0000$
   * $f(2.0) = \frac{1}{2.0} = 0.5000$
   * $f(3.0) = \frac{1}{3.0} \approx 0.3333$
   * $f(4.0) = \frac{1}{4.0} = 0.2500$

**4. Aplicación de la fórmula de Simpson 3/8:**
   Como solo tenemos 3 subintervalos, no hay puntos interiores múltiples de 3, por lo que el patrón de coeficientes es simple ($1, 3, 3, 1$):
   $$I \approx \frac{3(1.0)}{8} \Big[ f(1.0) + 3f(2.0) + 3f(3.0) + f(4.0) \Big]$$
   $$I \approx 0.375 \Big[ 1.0000 + 3(0.5000) + 3(0.3333) + 0.2500 \Big]$$
   $$I \approx 0.375 \Big[ 1.0000 + 1.5000 + 0.9999 + 0.2500 \Big]$$
   $$I \approx 0.375 \Big[ 3.7499 \Big] \approx \mathbf{1.4062}$$

**Conclusión:** La aproximación numérica es $1.4062$. El valor real de la integral $\ln(4)$ es aproximadamente $1.3863$. La discrepancia se debe a que evaluamos un segmento muy ancho (paso de $1.0$); aumentar $n$ a 6 o 9 reduciría el error a casi cero.

### Código
[simpson38.py](../3-Codigos/simpson38.py)
Markdown

## Regla del Trapecio



### Teoría y Fundamentación Matemática
La integración numérica permite aproximar el valor de una integral definida $\int_a^b f(x) dx$. La **Regla del Trapecio** es la primera y más sencilla de las fórmulas cerradas de Newton-Cotes. Su principio fundamental consiste en unir los puntos extremos de la función en el intervalo $[a, b]$ mediante una **línea recta** (un polinomio de primer grado), formando así un trapecio bajo la curva cuya área es fácil de calcular.

Dado que usar una sola línea recta para aproximar toda una curva genera un error de truncamiento significativo (especialmente en intervalos grandes o curvas muy pronunciadas), en la práctica se emplea la **Regla del Trapecio Compuesta**. Esta variante divide el intervalo total en $n$ subintervalos iguales y aplica la regla básica a cada uno de ellos, sumando luego todas las áreas. A diferencia de los métodos de Simpson, la regla del trapecio **no tiene restricciones en cuanto a la cantidad de subintervalos** (pueden ser pares o impares).

### Fórmulas y Criterios
Dado un intervalo de integración $[a, b]$ dividido en $n$ subintervalos:

1. **Tamaño del paso ($h$):**
   La distancia constante entre cada punto a evaluar es:
   $$h = \frac{b - a}{n}$$

2. **Fórmula del Trapecio Compuesta:**
   Para aproximar la integral, se evalúa la función en los puntos $x_0, x_1, x_2, \dots, x_n$ y se agrupan de la siguiente manera:
   $$\int_a^b f(x) dx \approx \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$
   
   *En palabras simples:* Se suman el primer y último punto (los extremos), más **2 veces** la suma de todos los puntos interiores; el resultado total se multiplica por $h/2$.

### Ejercicio Resuelto
**Enunciado:** Aproxima la integral de la función $f(x) = x^2$ en el intervalo $[0, 2]$ utilizando la Regla del Trapecio con $n = 4$ subintervalos. Compara el resultado con el valor analítico exacto.

**Solución paso a paso:**
**1. Cálculo del tamaño de paso ($h$):**
   $$h = \frac{2 - 0}{4} = \frac{2}{4} = 0.5$$

**2. Determinación de los puntos a evaluar ($x_i$):**
   Comenzamos en $a = 0$ y avanzamos de $0.5$ en $0.5$ hasta $b = 2$.
   * $x_0 = 0.0$
   * $x_1 = 0.5$
   * $x_2 = 1.0$
   * $x_3 = 1.5$
   * $x_4 = 2.0$

**3. Evaluación de la función $f(x) = x^2$ en cada punto:**
   * $f(0.0) = 0.0^2 = 0.0000$
   * $f(0.5) = 0.5^2 = 0.2500$
   * $f(1.0) = 1.0^2 = 1.0000$
   * $f(1.5) = 1.5^2 = 2.2500$
   * $f(2.0) = 2.0^2 = 4.0000$

**4. Aplicación de la fórmula del Trapecio Compuesta:**
   $$I \approx \frac{0.5}{2} \Big[ f(0.0) + 2 \big( f(0.5) + f(1.0) + f(1.5) \big) + f(2.0) \Big]$$
   $$I \approx 0.25 \Big[ 0.0000 + 2 \big( 0.2500 + 1.0000 + 2.2500 \big) + 4.0000 \Big]$$
   $$I \approx 0.25 \Big[ 0.0000 + 2 \big( 3.5000 \big) + 4.0000 \Big]$$
   $$I \approx 0.25 \Big[ 0.0000 + 7.0000 + 4.0000 \Big]$$
   $$I \approx 0.25 \Big[ 11.0000 \Big] = \mathbf{2.7500}$$

**Conclusión:** La aproximación numérica es $2.7500$. El valor real de esta integral es $\int_0^2 x^2 dx = [\frac{x^3}{3}]_0^2 = \frac{8}{3} \approx 2.6667$. El error absoluto es de $0.0833$, el cual puede reducirse significativamente utilizando un $n$ mayor (por ejemplo, $n=10$).
### Código
[trapecio.py](../3-Codigos/trapecio.py)

Problemario Unidad 4 Esteban Romero Pérez
 > [!NOTE]
> Link de problemario
https://canva.link/byubmt1vql3punk
