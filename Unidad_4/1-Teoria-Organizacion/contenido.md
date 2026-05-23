## Diferenciación Numérica: Regla de los 3 Puntos

### Naturaleza y Fundamento Matemático
La diferenciación numérica es una técnica utilizada para aproximar la derivada de una función cuando no se conoce su expresión analítica, la función es demasiado compleja para derivar, o solo se dispone de un conjunto de datos tabulados discretos. 

Las **fórmulas de 3 puntos** surgen al expandir la función mediante series de Taylor y tomar tres puntos vecinos (usualmente separados por una distancia constante $h$) para estimar la pendiente. A diferencia de las aproximaciones básicas de dos puntos (que tienen un error de truncamiento del orden de $O(h)$), las reglas de tres puntos logran un error de truncamiento del orden de $O(h^2)$, lo que las hace significativamente más precisas. Dependiendo de la posición del punto de interés respecto a los datos disponibles, se puede calcular la derivada evaluando hacia adelante, hacia atrás, o de forma centrada.

### Fórmulas y Operaciones

Sea $x_i$ el punto donde queremos evaluar la primera derivada $f'(x_i)$, y $h$ el tamaño del paso (distancia entre puntos).

1. **Diferencia hacia adelante (Progresiva):**
Se utiliza cuando se conocen los puntos actuales y los dos siguientes ($x_i, x_{i+1}, x_{i+2}$). Es útil en el límite inicial de un conjunto de datos.
$$f'(x_i) \approx \frac{-3f(x_i) + 4f(x_{i+1}) - f(x_{i+2})}{2h}$$

2. **Diferencia hacia atrás (Regresiva):**
Se utiliza cuando se conocen los puntos actuales y los dos anteriores ($x_i, x_{i-1}, x_{i-2}$). Es ideal para el límite final de un conjunto de datos.
$$f'(x_i) \approx \frac{3f(x_i) - 4f(x_{i-1}) + f(x_{i-2})}{2h}$$

3. **Diferencia Centrada:**
Utiliza el punto anterior y el siguiente ($x_{i-1}$ y $x_{i+1}$). Curiosamente, el término $f(x_i)$ se cancela algebraicamente durante la deducción con series de Taylor, pero se sigue considerando una fórmula de 3 puntos porque abarca ese dominio. Es la más exacta de las tres para un mismo tamaño de $h$.
$$f'(x_i) \approx \frac{f(x_{i+1}) - f(x_{i-1})}{2h}$$

### Ejemplo Paso a Paso

Aproximemos la primera derivada de la función $f(x) = x^3$ en el punto $x = 1.0$ utilizando un paso $h = 0.1$.
*(Nota: Analíticamente, la derivada es $f'(x) = 3x^2$, por lo que el valor exacto en $x=1.0$ es **$3.0$**).*

**Paso 1: Identificar los puntos necesarios**
Necesitamos calcular $f(x)$ para los puntos circundantes:
- $x_{i-2} = 0.8 \implies f(0.8) = 0.8^3 = 0.512$
- $x_{i-1} = 0.9 \implies f(0.9) = 0.9^3 = 0.729$
- $x_i = 1.0 \implies f(1.0) = 1.0^3 = 1.000$
- $x_{i+1} = 1.1 \implies f(1.1) = 1.1^3 = 1.331$
- $x_{i+2} = 1.2 \implies f(1.2) = 1.2^3 = 1.728$

**Paso 2: Aplicar Regla Hacia Adelante**
$$f'(1.0) \approx \frac{-3(1.000) + 4(1.331) - 1.728}{2(0.1)} = \frac{-3.000 + 5.324 - 1.728}{0.2} = \frac{0.596}{0.2} = 2.98$$

**Paso 3: Aplicar Regla Hacia Atrás**
$$f'(1.0) \approx \frac{3(1.000) - 4(0.729) + 0.512}{2(0.1)} = \frac{3.000 - 2.916 + 0.512}{0.2} = \frac{0.596}{0.2} = 2.98$$

**Paso 4: Aplicar Regla Centrada**
$$f'(1.0) \approx \frac{1.331 - 0.729}{2(0.1)} = \frac{0.602}{0.2} = 3.01$$

Como se observa, las tres reglas ofrecen valores muy cercanos al valor real de $3.0$, siendo aproximaciones excelentes de orden $O(h^2)$.

### Código
[Regla3puntos.py](../3-Codigos/Regla3puntos.py)
## Integración Numérica: Regla de Simpson 1/3

### Naturaleza y Fundamento Matemático
La regla de Simpson 1/3 es un método de integración numérica que pertenece a la familia de las fórmulas de Newton-Cotes. Mientras que métodos más simples (como la regla del trapecio) conectan los puntos de una función con líneas rectas, la regla de Simpson 1/3 conecta grupos de tres puntos sucesivos utilizando **parábolas** (polinomios de segundo grado). 

Al curvarse para adaptarse a la forma de la función real, este método reduce drásticamente el error de aproximación frente a las líneas rectas. Una peculiaridad matemática muy importante de la regla de Simpson 1/3 es que, aunque utiliza polinomios de grado 2 para aproximar, es capaz de integrar exactamente polinomios de hasta grado 3 (cúbicos) sin ningún margen de error. 

Para poder aplicar la regla de Simpson 1/3 de forma compuesta (repetida) en un intervalo grande, es un requisito estricto que el número de subintervalos ($n$) sea un **número par** (lo que equivale a un número impar de puntos evaluados).

### Fórmulas y Operaciones

Dado un intervalo de integración $[a, b]$ dividido en $n$ subintervalos (donde $n$ es par):

1. **Cálculo del tamaño del paso ($h$):**
$$h = \frac{b - a}{n}$$

2. **Fórmula Compuesta de Simpson 1/3:**
La aproximación de la integral $I$ se calcula sumando los extremos y alternando coeficientes de 4 y 2 para los puntos intermedios:
$$I \approx \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1, 3, 5...}^{n-1} f(x_i) + 2 \sum_{j=2, 4, 6...}^{n-2} f(x_j) + f(x_n) \right]$$

*Regla mnemotécnica: Los extremos se multiplican por 1, los índices impares se multiplican por 4, y los índices pares se multiplican por 2.*

### Ejemplo Paso a Paso

Vamos a aproximar la integral definida de la función $f(x) = x^2$ en el intervalo de $a = 0$ a $b = 2$, utilizando $n = 2$ subintervalos.
*(Nota: Analíticamente, la integral exacta es $\int_{0}^{2} x^2 dx = \frac{x^3}{3} \Big|_0^2 = \frac{8}{3} \approx 2.6666...$)*

**Paso 1: Calcular $h$ y los puntos a evaluar**
$$h = \frac{2 - 0}{2} = 1$$
Los puntos $x$ espaciados por $h$ son:
- $x_0 = 0 \implies f(0) = 0^2 = 0$
- $x_1 = 1 \implies f(1) = 1^2 = 1$
- $x_2 = 2 \implies f(2) = 2^2 = 4$

**Paso 2: Aplicar la fórmula de Simpson 1/3**
Como solo tenemos $n=2$, la fórmula se simplifica a los tres puntos básicos:
$$I \approx \frac{h}{3} \left[ f(x_0) + 4f(x_1) + f(x_2) \right]$$
$$I \approx \frac{1}{3} \left[ 0 + 4(1) + 4 \right]$$
$$I \approx \frac{1}{3} [8] = \frac{8}{3} \approx 2.6666...$$

*El resultado es numéricamente exacto al valor analítico, demostrando la eficacia de este método en polinomios de grado bajo.*

### Código
[simpson13.py](../3-Codigos/simpson13.py)
## Integración Numérica: Regla de Simpson 3/8

### Naturaleza y Fundamento Matemático
La regla de Simpson 3/8 es otra técnica de integración numérica de la familia de Newton-Cotes. Mientras que la regla de Simpson 1/3 utiliza parábolas (polinomios de grado 2) para conectar tres puntos, la regla de Simpson 3/8 utiliza **polinomios cúbicos** (grado 3) para conectar grupos de **cuatro puntos** sucesivos.

Aunque podría pensarse que al usar un polinomio de mayor grado es infinitamente superior, en la práctica la regla de Simpson 3/8 tiene una precisión muy similar a la de 1/3. Su verdadera utilidad y ventaja radica en la restricción de los intervalos: mientras que Simpson 1/3 exige estrictamente un número de subintervalos par, **Simpson 3/8 exige que el número de subintervalos ($n$) sea un múltiplo de 3**. En software de ingeniería, ambas reglas suelen combinarse (usando 1/3 para la mayor parte del área y 3/8 para el residuo si la cantidad total de intervalos es impar).

### Fórmulas y Operaciones

Dado un intervalo de integración $[a, b]$ dividido en $n$ subintervalos (donde $n$ es múltiplo de 3):

1. **Cálculo del tamaño del paso ($h$):**
$$h = \frac{b - a}{n}$$

2. **Fórmula Compuesta de Simpson 3/8:**
La aproximación de la integral $I$ suma los extremos, y para los puntos interiores alterna coeficientes multiplicadores. Los puntos cuyo índice es múltiplo de 3 se multiplican por 2, y todos los demás se multiplican por 3:
$$I \approx \frac{3h}{8} \left[ f(x_0) + 3 \sum_{i \neq \text{múltiplo de 3}} f(x_i) + 2 \sum_{j = \text{múltiplo de 3}} f(x_j) + f(x_n) \right]$$

*Regla mnemotécnica para los coeficientes interiores: 3, 3, 2, 3, 3, 2, 3, 3, 2...*

### Ejemplo Paso a Paso

Aproximemos la integral definida de la función cúbica $f(x) = x^3$ en el intervalo de $a = 0$ a $b = 3$, utilizando $n = 3$ subintervalos.
*(Nota: Analíticamente, la integral exacta es $\int_{0}^{3} x^3 dx = \frac{x^4}{4} \Big|_0^3 = \frac{81}{4} = 20.25$)*

**Paso 1: Calcular $h$ y los puntos a evaluar**
$$h = \frac{3 - 0}{3} = 1$$
Los cuatro puntos $x$ espaciados por $h$ son:
- $x_0 = 0 \implies f(0) = 0^3 = 0$
- $x_1 = 1 \implies f(1) = 1^3 = 1$
- $x_2 = 2 \implies f(2) = 2^3 = 8$
- $x_3 = 3 \implies f(3) = 3^3 = 27$

**Paso 2: Aplicar la fórmula de Simpson 3/8**
Dado que $n=3$, utilizamos la versión simple de la fórmula sin repeticiones:
$$I \approx \frac{3h}{8} \left[ f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3) \right]$$
$$I \approx \frac{3(1)}{8} \left[ 0 + 3(1) + 3(8) + 27 \right]$$
$$I \approx \frac{3}{8} \left[ 3 + 24 + 27 \right] = \frac{3}{8} [54]$$
$$I \approx \frac{162}{8} = 20.25$$

*Al igual que su contraparte, el resultado es numéricamente exacto al valor analítico, demostrando que este método integra perfectamente polinomios de hasta grado 3.*

### Código
[simpson38.py](../3-Codigos/simpson38.py)
Markdown
## Integración Numérica: Regla del Trapecio

### Naturaleza y Fundamento Matemático
La regla del trapecio es el método más elemental dentro de la familia de fórmulas de integración numérica de Newton-Cotes. Su principio geométrico es muy intuitivo: en lugar de aproximar el área bajo una curva utilizando rectángulos (como en las sumas de Riemann básicas), conecta dos puntos adyacentes de la función con una **línea recta**, formando así un trapecio.

Al utilizar un polinomio de primer grado (una recta) para aproximar el comportamiento de la función, este método es matemáticamente exacto solo para funciones lineales. Cuando se aplica a curvas complejas, genera un error de truncamiento considerable, ya que la recta ignora por completo la concavidad o convexidad de la curva real. Para mitigar este error sin cambiar de método, se aplica la **Regla del Trapecio Compuesta**, que consiste en dividir el intervalo de integración original en $n$ subintervalos más pequeños (múltiples trapecios delgados), lo que hace que la suma de sus áreas se adapte mejor al contorno real de la curva.

### Fórmulas y Operaciones

Dado un intervalo de integración $[a, b]$ dividido en $n$ subintervalos del mismo ancho:

1. **Cálculo del tamaño del paso ($h$):**
$$h = \frac{b - a}{n}$$

2. **Fórmula de la Regla del Trapecio Compuesta:**
La aproximación de la integral $I$ suma las evaluaciones en los extremos y suma el doble de todas las evaluaciones en los puntos interiores:
$$I \approx \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$

*Regla mnemotécnica: Los extremos del intervalo general se multiplican por 1, y todos los puntos de en medio se multiplican por 2.*

### Ejemplo Paso a Paso

Para evidenciar la diferencia de precisión geométrica con los métodos de Simpson, aproximaremos la misma integral definida de la función $f(x) = x^2$ en el intervalo de $a = 0$ a $b = 2$, utilizando $n = 2$ subintervalos.
*(Nota: Analíticamente, la integral exacta es $\int_{0}^{2} x^2 dx = \frac{x^3}{3} \Big|_0^2 = \frac{8}{3} \approx 2.6666...$)*

**Paso 1: Calcular $h$ y los puntos a evaluar**
$$h = \frac{2 - 0}{2} = 1$$
Los puntos $x$ espaciados por $h$ son idénticos a los del ejemplo de Simpson 1/3:
- $x_0 = 0 \implies f(0) = 0^2 = 0$
- $x_1 = 1 \implies f(1) = 1^2 = 1$
- $x_2 = 2 \implies f(2) = 2^2 = 4$

**Paso 2: Aplicar la fórmula del Trapecio Compuesto**
$$I \approx \frac{h}{2} \left[ f(x_0) + 2f(x_1) + f(x_2) \right]$$
$$I \approx \frac{1}{2} \left[ 0 + 2(1) + 4 \right]$$
$$I \approx \frac{1}{2} [6] = 3.0$$

*Análisis del error: El resultado es $3.0$, mientras que el real es $2.666...$. A diferencia de Simpson 1/3 (que dio el valor exacto), el trapecio sobreestimó el área porque la línea recta trazada por encima de la curva convexa de $x^2$ incluyó espacio extra (un error característico de los métodos lineales).*

### Código
[trapecio.py](../3-Codigos/trapecio.py)

Problemario Unidad 4 Esteban Romero Pérez
 > [!NOTE]
> Link de problemario
https://canva.link/byubmt1vql3punk
