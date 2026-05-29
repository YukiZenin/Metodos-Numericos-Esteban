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

### Fórmulas y Criterios
Dado un intervalo inicial $[a, b]$:
    
1. **Punto medio (raíz estimada):**
   La estimación actual de la raíz $x_r$ siempre se calcula en el punto central del intervalo de trabajo:
   $$x_r = \frac{a + b}{2}$$

2. **Evaluación de subintervalos:**
   Una vez calculado $x_r$, se debe determinar en qué mitad quedó atrapada la raíz real multiplicando $f(a)$ por $f(x_r)$:
   * Si $f(a) \cdot f(x_r) < 0$: La raíz se encuentra en la primera mitad. El nuevo límite superior será $b = x_r$.
   * Si $f(a) \cdot f(x_r) > 0$: La raíz se encuentra en la segunda mitad. El nuevo límite inferior será $a = x_r$.
   * Si $f(a) \cdot f(x_r) = 0$: Felicidades, $x_r$ es la raíz exacta, y el algoritmo se detiene.

3. **Criterio de paro (Tolerancia):**
   El bucle iterativo se detiene cuando el tamaño de la mitad del intervalo cae por debajo de una tolerancia de error predefinida ($tol$):
   $$\frac{b - a}{2} \le tol$$

### Ejercicio Resuelto
**Enunciado:** Encuentra una raíz de la función $f(x) = x^2 - 3$ en el intervalo inicial $[1, 2]$. Realiza 2 iteraciones a mano para acercarte a la solución.

**Solución paso a paso:**
**1. Comprobación inicial del intervalo:**
   * $f(1) = (1)^2 - 3 = -2$
   * $f(2) = (2)^2 - 3 = 1$
   * Al ser de signos opuestos ($f(1) \cdot f(2) = -2 < 0$), confirmamos que hay una raíz en $[1, 2]$.

**2. Iteración 1:**
   * Calculamos el punto medio: $x_{r1} = \frac{1 + 2}{2} = 1.5$
   * Evaluamos la función en $x_{r1}$: $f(1.5) = (1.5)^2 - 3 = 2.25 - 3 = -0.75$
   * Verificamos los signos: Evaluamos el producto del límite inferior y el medio: $f(1) \cdot f(1.5) = (-2) \cdot (-0.75) = +1.5 > 0$.
   * Como el producto es positivo (mismo signo), la raíz **no** está ahí. Está en la segunda mitad. Actualizamos el límite inferior: $a = 1.5$.
   * Nuestro nuevo intervalo de trabajo se reduce a: $[1.5, 2]$

**3. Iteración 2:**
   * Calculamos el nuevo punto medio: $x_{r2} = \frac{1.5 + 2}{2} = 1.75$
   * Evaluamos la función en $x_{r2}$: $f(1.75) = (1.75)^2 - 3 = 3.0625 - 3 = 0.0625$
   * Verificamos los signos: Evaluamos $f(1.5) \cdot f(1.75) = (-0.75) \cdot (0.0625) < 0$.
   * Como el producto es negativo (cambio de signo), la raíz está en esta primera mitad. Actualizamos el límite superior: $b = 1.75$.
   * Nuestro nuevo intervalo para la Iteración 3 sería: $[1.5, 1.75]$

**Resultado después de 2 iteraciones:** La aproximación actual de la raíz es $x_r = 1.75$ (bastante cerca del valor analítico real de $\sqrt{3} \approx 1.732$).
### Código
 
[biseccion.py](../3-Código/biseccion.py)

## 2. Método de Falsa Posición (Regula Falsi)

### Naturaleza y Fundamento Matemático
La Regula Falsi es también un método cerrado que requiere un intervalo $[a, b]$ donde haya un cambio de signo. Sin embargo, intenta ser más inteligente que la bisección. En lugar de asumir ciegamente que la raíz está en el centro exacto del intervalo, la Falsa Posición une los puntos $(a, f(a))$ y $(b, f(b))$ con una línea recta (una secante). El punto donde esta línea recta cruza el eje $X$ se toma como la nueva estimación $x_r$.

Matemáticamente, asume que si $f(a)$ está mucho más cerca de cero que $f(b)$, es muy probable que la raíz real esté más cerca de $a$ que de $b$. La fórmula de interpolación lineal se calcula y el intervalo se reduce manteniendo los límites que encierran el cambio de signo.

### Ventajas, Desventajas y Comportamiento
Para curvas suaves, este método llega a la raíz mucho más rápido que la bisección. No obstante, tiene un talón de Aquiles grave: el **estancamiento**. Si la función tiene una curvatura muy pronunciada (convexa o cóncava), uno de los extremos del intervalo puede quedarse fijo mientras el otro avanza milimétricamente iteración tras iteración. En estos casos patológicos, la Falsa Posición puede volverse incluso más lenta que la bisección pura, requiriendo algoritmos modificados para obligar al límite estancado a moverse.

### Fórmulas y Criterios
Dado un intervalo inicial $[a, b]$:
    
1. **Estimación de la raíz ($x_r$):**
   Utilizando semejanza de triángulos o la ecuación de la recta secante, la fórmula para encontrar el punto donde la recta cruza el eje X es:
   $$x_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$$

2. **Evaluación de subintervalos:**
   El criterio para actualizar el intervalo es idéntico al de la bisección:
   * Si $f(a) \cdot f(x_r) < 0$: La raíz se encuentra entre $a$ y $x_r$. El nuevo límite superior será $b = x_r$.
   * Si $f(a) \cdot f(x_r) > 0$: La raíz se encuentra entre $x_r$ y $b$. El nuevo límite inferior será $a = x_r$.
   * Si $f(a) \cdot f(x_r) = 0$: $x_r$ es la raíz exacta.

3. **Criterio de paro (Tolerancia):**
   Dado que uno de los límites puede quedarse estancado (fijo) mientras el otro se acerca a la raíz, el error se suele calcular por la diferencia entre la estimación actual y la anterior:
   $$|x_r^{nuevo} - x_r^{anterior}| \le tol$$

### Ejercicio Resuelto
**Enunciado:** Encuentra la raíz de la función $f(x) = x^2 - 3$ en el intervalo inicial $[1, 2]$ mediante el método de falsa posición. Realiza 2 iteraciones.

**Solución paso a paso:**
**1. Comprobación y evaluación inicial:**
   * $a = 1 \implies f(1) = (1)^2 - 3 = -2$
   * $b = 2 \implies f(2) = (2)^2 - 3 = 1$
   * Existe un cambio de signo ($-2 \cdot 1 < 0$).

**2. Iteración 1:**
   * Aplicamos la fórmula de falsa posición:
     $$x_r = 2 - \frac{1(1 - 2)}{-2 - 1} = 2 - \frac{1(-1)}{-3} = 2 - \frac{-1}{-3} = 2 - \frac{1}{3} \approx 1.6667$$
   * Evaluamos la función en el nuevo punto: $f(1.6667) = (1.6667)^2 - 3 = 2.7778 - 3 = -0.2222$
   * Verificamos los signos: $f(1) \cdot f(1.6667) = (-2) \cdot (-0.2222) > 0$.
   * Como el producto es positivo, la raíz está en el subintervalo superior. Actualizamos el límite inferior: $a = 1.6667$ (y su función es $f(a) = -0.2222$).
   * Nuevo intervalo: $[1.6667, 2]$.

**3. Iteración 2:**
   * Aplicamos nuevamente la fórmula con los nuevos valores:
     $$x_r = 2 - \frac{1(1.6667 - 2)}{-0.2222 - 1} = 2 - \frac{1(-0.3333)}{-1.2222} = 2 - \frac{-0.3333}{-1.2222} \approx 2 - 0.2727 = 1.7273$$
   * Evaluamos la función: $f(1.7273) = (1.7273)^2 - 3 \approx -0.0164$ (estamos ya muy cerca de cero).

**Resultado después de 2 iteraciones:** La aproximación actual es $x_r = 1.7273$. *(Nota: ¡Fíjate que con solo 2 iteraciones hemos llegado mucho más cerca de la raíz real $\sqrt{3} \approx 1.7320$ que con la bisección en el mismo número de pasos!)*
### Código

[falsaposicion.py](../3-Código/falsaposicion.py)

## 3. Método de Newton-Raphson

### Naturaleza y Fundamento Matemático
El método de Newton-Raphson es el estándar de oro en los métodos abiertos. A diferencia de los métodos cerrados, no requiere un intervalo, sino un único punto inicial $x_0$. Se fundamenta en el cálculo diferencial y la expansión de la Serie de Taylor. El algoritmo traza una línea tangente a la curva de la función en el punto evaluado, guiándose por su pendiente (la primera derivada, $f'(x)$). Donde esa línea tangente toca el eje $X$, se establece el nuevo punto $x_1$.

La ecuación iterativa es limpia y poderosa: $x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$. La línea tangente proyecta de forma muy precisa dónde la curva interceptará el eje horizontal.

### Ventajas, Desventajas y Comportamiento
Su velocidad es inigualable: posee convergencia **cuadrática**. Esto significa que la cantidad de decimales correctos aproximadamente se duplica en cada iteración. 
Sin embargo, su extrema velocidad viene con grandes riesgos. Si la estimación inicial está muy lejos, o si el algoritmo se topa con un punto donde la pendiente es casi horizontal (derivada cercana a cero), la tangente disparará el nuevo punto hacia el infinito, provocando divergencia. Además, requiere conocer la derivada matemática exacta de la función, lo cual en sistemas computacionales complejos (como datos tabulados o físicas simuladas) a menudo es imposible o computacionalmente costoso.

### Fórmulas y Criterios
1. **Fórmula de iteración:**
   Conociendo un valor actual $x_i$, el valor para la siguiente iteración $x_{i+1}$ se calcula así:
   $$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$

2. **Criterio de paro (Tolerancia):**
   El proceso iterativo se detiene cuando la diferencia entre la nueva aproximación y la anterior es menor que una tolerancia dada:
   $$|x_{i+1} - x_i| \le tol$$

### Ejercicio Resuelto
**Enunciado:** Encuentra una raíz de la función $f(x) = x^2 - 3$. Utiliza el valor inicial $x_0 = 1.5$ y realiza 2 iteraciones.

**Solución paso a paso:**
**1. Preparación previa:**
   * Función: $f(x) = x^2 - 3$
   * Derivada de la función: $f'(x) = 2x$
   * Valor inicial: $x_0 = 1.5$

**2. Iteración 1:**
   * Evaluamos la función y su derivada en $x_0$:
     $$f(1.5) = (1.5)^2 - 3 = 2.25 - 3 = -0.75$$
     $$f'(1.5) = 2(1.5) = 3$$
   * Aplicamos la fórmula de Newton-Raphson:
     $$x_1 = 1.5 - \frac{-0.75}{3} = 1.5 - (-0.25) = 1.5 + 0.25 = 1.75$$
   * La nueva aproximación es $x_1 = 1.75$.

**3. Iteración 2:**
   * Evaluamos la función y su derivada en el nuevo punto $x_1$:
     $$f(1.75) = (1.75)^2 - 3 = 3.0625 - 3 = 0.0625$$
     $$f'(1.75) = 2(1.75) = 3.5$$
   * Aplicamos la fórmula:
     $$x_2 = 1.75 - \frac{0.0625}{3.5} = 1.75 - 0.017857... \approx 1.73214$$

**Resultado después de 2 iteraciones:** La aproximación es $x_2 \approx 1.73214$. Como puedes ver, en solo dos pasos estamos ya logrando una exactitud altísima respecto al valor real ($\sqrt{3} \approx 1.73205$).
### Código
[newton.py](../3-Código/newton.py)
## 4. Método de la Secante

### Naturaleza y Fundamento Matemático
El método de la Secante nació para solucionar el mayor problema de Newton-Raphson: la necesidad de calcular derivadas analíticas. La computadora aproxima la derivada mediante diferencias finitas utilizando los dos últimos puntos calculados. En lugar de una línea tangente pura, traza una secante entre $x_{i}$ y $x_{i-1}$. 

Al sustituir la derivada exacta por una aproximación ($\frac{f(x_{i}) - f(x_{i-1})}{x_{i} - x_{i-1}}$), el algoritmo hereda la velocidad de los métodos basados en pendientes sin exigir que el desarrollador programe la función derivada. Requiere dos valores iniciales, pero, a diferencia de la bisección, no es necesario que estos encierren la raíz.

### Ventajas, Desventajas y Comportamiento
Tiene una convergencia **superlineal** (específicamente, su tasa de convergencia está relacionada con el número áureo, $\approx 1.618$). Es casi tan rápido como Newton-Raphson, pero requiere menos carga de procesamiento por iteración al no evaluar derivadas. 
Su desventaja radica en la vulnerabilidad computacional (Cancelación Catastrófica): a medida que el algoritmo converge, $f(x_{i})$ y $f(x_{i-1})$ se vuelven valores casi idénticos. Al restarlos en el denominador para calcular la pendiente, la computadora se enfrenta a una pérdida masiva de precisión binaria que puede generar divisiones por cero o resultados inestables si la tolerancia de parada es demasiado microscópica.

### Fórmulas y Criterios
1. **Fórmula de iteración:**
   Partiendo de la fórmula de Newton-Raphson, se sustituye la derivada $f'(x_i)$ por la aproximación de diferencias finitas:
   $$f'(x_i) \approx \frac{f(x_i) - f(x_{i-1})}{x_i - x_{i-1}}$$
   
   Al sustituir y reordenar términos, obtenemos la fórmula matemática de la secante:
   $$x_{i+1} = x_i - f(x_i) \frac{x_i - x_{i-1}}{f(x_i) - f(x_{i-1})}$$

2. **Criterio de paro (Tolerancia):**
   El proceso iterativo se detiene cuando la diferencia absoluta entre la nueva estimación y la inmediatamente anterior cae por debajo de la tolerancia requerida:
   $$|x_{i+1} - x_i| \le tol$$

### Ejercicio Resuelto
**Enunciado:** Encuentra una raíz de la función $f(x) = x^2 - 3$. Utiliza los valores iniciales $x_0 = 1$ y $x_1 = 2$. Realiza 2 iteraciones paso a paso.

**Solución paso a paso:**
**1. Preparación y evaluación inicial:**
   * Función: $f(x) = x^2 - 3$
   * Valores iniciales: $x_0 = 1, \quad x_1 = 2$
   * Evaluamos la función en estos puntos:
     $$f(x_0) = f(1) = (1)^2 - 3 = -2$$
     $$f(x_1) = f(2) = (2)^2 - 3 = 1$$

**2. Iteración 1 (Cálculo de $x_2$):**
   * Aplicamos la fórmula de la secante usando $x_0$ y $x_1$:
     $$x_2 = 2 - (1) \frac{2 - 1}{1 - (-2)}$$
     $$x_2 = 2 - \frac{1}{3} \approx 1.6667$$
   * Evaluamos la función en el nuevo punto:
     $$f(x_2) = f(1.6667) = (1.6667)^2 - 3 = 2.7778 - 3 = -0.2222$$

**3. Iteración 2 (Cálculo de $x_3$):**
   * Ahora desplazamos nuestros puntos de trabajo. Usaremos $x_1 = 2$ y el nuevo $x_2 = 1.6667$.
   * Aplicamos la fórmula de la secante nuevamente:
     $$x_3 = 1.6667 - (-0.2222) \frac{1.6667 - 2}{-0.2222 - 1}$$
     $$x_3 = 1.6667 - (-0.2222) \frac{-0.3333}{-1.2222}$$
     $$x_3 = 1.6667 - (-0.2222)(0.2727)$$
     $$x_3 = 1.6667 - (-0.0606) = 1.6667 + 0.0606 = 1.7273$$

**Resultado después de 2 iteraciones:** La nueva aproximación es $x_3 = 1.7273$. *(Nota: Tras solo dos iteraciones, ya estamos a milésimas de la raíz analítica $\sqrt{3} \approx 1.7320$).*
### Código
 
[secante.py](../3-Código/secante.py)

Problemario Unidad 2 Esteban Romero Pérez
 > [!NOTE]
> Link de problemario
https://docs.google.com/spreadsheets/d/1VNMoedVZJlIWm8WSi1sSmhbi1NH4llUu/edit?usp=sharing&ouid=105987244672104551759&rtpof=true&sd=true
