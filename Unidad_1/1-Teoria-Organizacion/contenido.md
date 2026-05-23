# Unidad 1: Fundamentos Numéricos y Análisis de Errores

En esta unidad inicial, exploraremos los principios básicos de los métodos numéricos, centrados en las restricciones computacionales y las diversas clases de errores que emergen al realizar cálculos matemáticos aproximados mediante programación.

---

## Conceptos Clave: Clasificación de Errores

### 1. División por Cero (Localización de Raíces)

#### Fundamentos Teóricos
* Este fallo es característico de algoritmos abiertos, como el método de Newton-Raphson.
* Se desencadena cuando la derivada de la función se anula (o toma un valor ínfimo), induciendo una división por cero en el proceso iterativo.
* Geométricamente, el inconveniente radica en que la recta tangente adopta una posición completamente horizontal, impidiendo su intersección finita con el eje de las abscisas.

#### Fórmulas
**Ecuación iterativa de Newton-Raphson:**
$$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$

La ejecución falla inevitablemente si $f'(x_i) = 0$.

#### Evaluación del Error
* A medida que el valor de $f'(x_i)$ se acerca a cero, el resultado del cociente tiende a infinito, volviendo el error inmanejable.
* En sistemas de punto flotante, esto se refleja en resultados como `inf` o `nan`, los cuales paralizan el cálculo.
* También puede provocar un salto desproporcionado que aleja la aproximación del valor real.
* Este escenario no se clasifica como un error clásico de truncamiento o redondeo, sino como un **error de singularidad** inherente al algoritmo cuando la derivada desaparece.

#### Criterios de Uso
* **Aparición:** Surge al aplicar Newton-Raphson cerca de mínimos, máximos locales o puntos de inflexión (donde $f'(x) = 0$).
* **Prevención:** Es vital confirmar que $|f'(x_i)| > \epsilon$ (un umbral de tolerancia) antes de iterar, o bien, recurrir a alternativas como el método de bisección en áreas problemáticas.
* **Restricciones:** Todos los métodos abiertos comparten esta vulnerabilidad; es imperativo validar siempre la derivada.

#### Caso Práctico
Evaluando la función $f(x) = x^3 - 2x + 2$, con derivada $f'(x) = 3x^2 - 2$.

Arrancando desde $x_0 = 0$:
* $f(0) = 0 - 0 + 2 = 2$
* $f'(0) = 0 - 2 = -2$
* $x_1 = 0 - (2 / -2) = \mathbf{1.0}$

Arrancando desde $x_0 = 0.8165$ (zona donde $f'(x) \approx 0$):
* $f(0.8165) \approx 0.9098$
* $f'(0.8165) = 3(0.8165)^2 - 2 \approx \mathbf{0.0003}$ (prácticamente cero)
* $x_1 = 0.8165 - (0.9098 / 0.0003) \approx \mathbf{-3032} \rightarrow$ ¡Divergencia extrema!

El ejemplo ilustra cómo la proximidad de la derivada a cero ocasiona una **falla catastrófica** del método.

**Código fuente:** [`Div_por_0.py`](3-Codigos/Div_por_0.py)

---

### 2. Error de Truncamiento (Ecuaciones Diferenciales)

#### Fundamentos Teóricos
* Se demuestra habitualmente con métodos numéricos como el de Euler.
* Al discretizar un proceso continuo, si el tamaño de paso ($h$) es excesivo, el error se engrosa iteración tras iteración debido al descarte (truncamiento) de los términos de orden superior en las series matemáticas.
* Representa la brecha entre la respuesta exacta y la estimación numérica generada al emplear una cantidad limitada de términos.

#### Fórmulas
**Regla del método de Euler:**
$$y_{i+1} = y_i + f(x_i, y_i) \cdot h$$

**Error de truncamiento local (vía Serie de Taylor):**
$$E_t = \frac{h^2}{2} y''(\xi)$$

#### Evaluación del Error
* **Error local:** $O(h^2)$ — surge de omitir los términos de segundo orden en adelante en el desarrollo de Taylor.
* **Error global:** $O(h)$ — representa la suma de los errores a través de $N = (b-a)/h$ iteraciones.
* Disminuir el paso $h$ atenúa el error, pero incrementa la carga operativa y corre el riesgo de sumar errores de redondeo.

#### Criterios de Uso
* **Aparición:** Presente en cualquier técnica numérica que discretice modelos continuos (ej. Euler, Runge-Kutta, diferencias finitas).
* **Minimización:** Se logra acortando la longitud del paso $h$ o implementando esquemas de mayor orden matemático (Taylor de orden 2, RK4).
* **Restricciones:** Achicar $h$ de forma ilimitada no garantiza una mayor exactitud, ya que propicia la acumulación de errores de redondeo.

#### Caso Práctico
Resolviendo $dy/dx = -y$, partiendo de $y(0) = 1$. Su solución analítica es: $y(x) = e^{-x}$.

**Usando $h = 0.5$:**
* $y_1 = 1 + 0.5(-1) = \mathbf{0.5}$ | Valor Real: $e^{-0.5} \approx 0.6065$ | Margen de error: $0.1065$
* $y_2 = 0.5 + 0.5(-0.5) = \mathbf{0.25}$ | Valor Real: $e^{-1} \approx 0.3679$ | Margen de error: $0.1179$

**Usando $h = 0.1$:**
* $y_1 = 1 + 0.1(-1) = \mathbf{0.9}$ | Valor Real: $e^{-0.1} \approx 0.9048$ | Margen de error: $0.0048$
* $y_2 = 0.9 + 0.1(-0.9) = \mathbf{0.81}$ | Valor Real: $e^{-0.2} \approx 0.8187$ | Margen de error: $0.0087$

Es evidente que al achicar $h$ (de 0.5 a 0.1), la precisión del método mejora de forma drástica.

**Código fuente:** [`Error_trunca.py`](3-Codigos/Error_trunca.py)

---

### 3. Subdesbordamiento Aritmético (Underflow)

#### Fundamentos Teóricos
* Este fenómeno irrumpe cuando el resultado de un cálculo es tan diminuto que supera la resolución de la máquina, forzándola a redondear el valor a `0.0`.
* Si esta variable posteriormente actúa como denominador, provocará una caída crítica del sistema.
* Su origen yace en las fronteras de almacenamiento del estándar de punto flotante IEEE 754.

#### Fórmulas
La cifra positiva más diminuta que soporta el formato de doble precisión (64 bits) es:
$$x_{min} \approx 2.225 \times 10^{-308}$$

Cualquier número por debajo de esta barrera colapsará a `0.0` (mediante underflow gradual o abrupto, dependiendo del sistema).

#### Evaluación del Error
* **Clasificación:** Se cataloga como un error de representación.
* Se distingue de los errores de truncamiento o redondeo convencional; constituye una **barrera física del hardware** frente a valores infinitesimales.
* Al llevar un valor existente a cero, la magnitud del error puede representar el 100%.
* Utilizar un registro bajo underflow como divisor detona una **división por cero** colateral.

#### Criterios de Uso
* **Aparición:** Frecuente al operar con exponenciales muy negativas, cálculos factoriales o multiplicaciones de múltiples fracciones minúsculas.
* **Prevención:** Se recomienda emplear escalas logarítmicas para variables minúsculas y corroborar siempre que los denominadores sean distintos de cero antes de proceder.
* **Restricciones:** Constituye una limitante intrínseca a la memoria finita en cualquier entorno de programación.

#### Caso Práctico
Ejemplo en Python utilizando precisión doble:

```python
x = 1e-300
y = x * 1e-10   # y = 1e-310 → aún representable (como número subnormal)
z = x * 1e-20   # z = 1e-320 → ¡COLAPSO POR UNDERFLOW! → z = 0.0

# Al intentar dividir:
resultado = 1.0 / z  # Error fatal: división por cero
