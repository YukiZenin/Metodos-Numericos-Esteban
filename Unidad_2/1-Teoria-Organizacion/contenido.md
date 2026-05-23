# Análisis Profundo de Métodos Numéricos para Aproximación de Raíces

En el campo del análisis numérico, encontrar las raíces de una función (los valores de $x$ para los cuales $f(x) = 0$) es fundamental para resolver ecuaciones complejas que no tienen soluciones analíticas directas. Dado que las computadoras no pueden despejar variables algebraicamente en funciones no lineales complejas, recurrimos a algoritmos iterativos. Estos métodos comienzan con estimaciones iniciales y las refinan cíclicamente hasta converger a un valor con una tolerancia de error aceptable.

Existen dos grandes familias de métodos: los **Métodos Cerrados** (o de intervalo), que garantizan la convergencia acorralando la raíz, y los **Métodos Abiertos**, que son mucho más rápidos pero corren el riesgo de divergir si la estimación inicial no es adecuada.

---

## 1. Método de Bisección (Búsqueda Binaria de Raíces)

### Naturaleza y Fundamento Matemático
El método de bisección es el algoritmo de búsqueda de raíces más fundamental, robusto y confiable. Pertenece a la familia de los métodos cerrados y se basa directamente en el **Teorema del Valor Intermedio (Teorema de Bolzano)**. Este teorema postula que si una función continua $f(x)$ toma valores de signo opuesto en los extremos de un intervalo $[a, b]$ (es decir, $f(a) \cdot f(b) < 0$), entonces obligatoriamente la curva debe cruzar el eje $X$ al menos una vez dentro de ese intervalo. 

El algoritmo funciona evaluando el punto medio del intervalo: $x_r = \frac{a + b}{2}$. Una vez evaluado $f(x_r)$, el algoritmo determina en qué mitad se produjo el cambio de signo y descarta la otra mitad. Este proceso divide el espacio de búsqueda a la mitad en cada iteración.

### Ventajas, Desventajas y Comportamiento
La principal ventaja de la bisección es que su convergencia está **100% garantizada** siempre que la función sea continua y el intervalo inicial contenga una raíz. Sin embargo, su principal defecto es la velocidad. Posee una convergencia estrictamente **lineal**, lo que significa que gana precisión de forma muy gradual. Es el equivalente numérico de buscar una palabra en un diccionario partiendo el libro siempre por la mitad; es seguro, pero computacionalmente costoso para sistemas que requieren respuestas en milisegundos.

### Código
 
[biseccion.py](../3-Código/biseccion.py)

## 2. Método de Falsa Posición (Regula Falsi)

### Naturaleza y Fundamento Matemático
La Regula Falsi es también un método cerrado que requiere un intervalo $[a, b]$ donde haya un cambio de signo. Sin embargo, intenta ser más inteligente que la bisección. En lugar de asumir ciegamente que la raíz está en el centro exacto del intervalo, la Falsa Posición une los puntos $(a, f(a))$ y $(b, f(b))$ con una línea recta (una secante). El punto donde esta línea recta cruza el eje $X$ se toma como la nueva estimación $x_r$.

Matemáticamente, asume que si $f(a)$ está mucho más cerca de cero que $f(b)$, es muy probable que la raíz real esté más cerca de $a$ que de $b$. La fórmula de interpolación lineal se calcula y el intervalo se reduce manteniendo los límites que encierran el cambio de signo.

### Ventajas, Desventajas y Comportamiento
Para curvas suaves, este método llega a la raíz mucho más rápido que la bisección. No obstante, tiene un talón de Aquiles grave: el **estancamiento**. Si la función tiene una curvatura muy pronunciada (convexa o cóncava), uno de los extremos del intervalo puede quedarse fijo mientras el otro avanza milimétricamente iteración tras iteración. En estos casos patológicos, la Falsa Posición puede volverse incluso más lenta que la bisección pura, requiriendo algoritmos modificados para obligar al límite estancado a moverse.

### Código

[falsaposicion.py](../3-Código/falsaposicion.py)

## 3. Método de Newton-Raphson

### Naturaleza y Fundamento Matemático
El método de Newton-Raphson es el estándar de oro en los métodos abiertos. A diferencia de los métodos cerrados, no requiere un intervalo, sino un único punto inicial $x_0$. Se fundamenta en el cálculo diferencial y la expansión de la Serie de Taylor. El algoritmo traza una línea tangente a la curva de la función en el punto evaluado, guiándose por su pendiente (la primera derivada, $f'(x)$). Donde esa línea tangente toca el eje $X$, se establece el nuevo punto $x_1$.

La ecuación iterativa es limpia y poderosa: $x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$. La línea tangente proyecta de forma muy precisa dónde la curva interceptará el eje horizontal.

### Ventajas, Desventajas y Comportamiento
Su velocidad es inigualable: posee convergencia **cuadrática**. Esto significa que la cantidad de decimales correctos aproximadamente se duplica en cada iteración. 
Sin embargo, su extrema velocidad viene con grandes riesgos. Si la estimación inicial está muy lejos, o si el algoritmo se topa con un punto donde la pendiente es casi horizontal (derivada cercana a cero), la tangente disparará el nuevo punto hacia el infinito, provocando divergencia. Además, requiere conocer la derivada matemática exacta de la función, lo cual en sistemas computacionales complejos (como datos tabulados o físicas simuladas) a menudo es imposible o computacionalmente costoso.

### Código
[newton.py](../3-Código/newton.py)
## 4. Método de la Secante

### Naturaleza y Fundamento Matemático
El método de la Secante nació para solucionar el mayor problema de Newton-Raphson: la necesidad de calcular derivadas analíticas. La computadora aproxima la derivada mediante diferencias finitas utilizando los dos últimos puntos calculados. En lugar de una línea tangente pura, traza una secante entre $x_{i}$ y $x_{i-1}$. 

Al sustituir la derivada exacta por una aproximación ($\frac{f(x_{i}) - f(x_{i-1})}{x_{i} - x_{i-1}}$), el algoritmo hereda la velocidad de los métodos basados en pendientes sin exigir que el desarrollador programe la función derivada. Requiere dos valores iniciales, pero, a diferencia de la bisección, no es necesario que estos encierren la raíz.

### Ventajas, Desventajas y Comportamiento
Tiene una convergencia **superlineal** (específicamente, su tasa de convergencia está relacionada con el número áureo, $\approx 1.618$). Es casi tan rápido como Newton-Raphson, pero requiere menos carga de procesamiento por iteración al no evaluar derivadas. 
Su desventaja radica en la vulnerabilidad computacional (Cancelación Catastrófica): a medida que el algoritmo converge, $f(x_{i})$ y $f(x_{i-1})$ se vuelven valores casi idénticos. Al restarlos en el denominador para calcular la pendiente, la computadora se enfrenta a una pérdida masiva de precisión binaria que puede generar divisiones por cero o resultados inestables si la tolerancia de parada es demasiado microscópica.

### Código
 
[secante.py](../3-Código/secante.py)

Problemario Unidad 2 Esteban Romero Pérez
 > [!NOTE]
> Link de problemario
https://docs.google.com/spreadsheets/d/1VNMoedVZJlIWm8WSi1sSmhbi1NH4llUu/edit?usp=sharing&ouid=105987244672104551759&rtpof=true&sd=true
