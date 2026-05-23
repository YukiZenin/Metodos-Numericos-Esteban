# Importa la librería tkinter para crear interfaces gráficas
import tkinter as tk

# Importa las ventanas de mensajes (errores, alertas, etc.)
from tkinter import messagebox


# ---------------- MÉTODO JACOBI ----------------

# Función que implementa el método iterativo de Jacobi
def jacobi(A, b, x0, tol, max_iter):

    # Obtiene el número de ecuaciones (tamaño del vector b)
    n = len(b)

    # Copia los valores iniciales x0 al vector x
    x = x0[:]

    # Limpia el cuadro de resultados antes de comenzar
    resultado.delete("1.0", tk.END)

    # Ciclo de iteraciones hasta el máximo permitido
    for k in range(max_iter):

        # Crea un nuevo vector para guardar los nuevos valores de x
        x_new = [0]*n

        # Recorre cada ecuación
        for i in range(n):

            # Variable para acumular la suma de Aij*xj
            suma = 0

            # Recorre cada variable de la ecuación
            for j in range(n):

                # Evita usar el elemento diagonal Aii
                if i != j:

                    # Suma Aij*xj
                    suma += A[i][j] * x[j]

            # Aplica la fórmula del método de Jacobi
            x_new[i] = (b[i] - suma) / A[i][i]

        # Calcula el error máximo entre iteraciones
        error = max(abs(x_new[i] - x[i]) for i in range(n))

        # Muestra la iteración y el error en el cuadro de texto
        resultado.insert(tk.END, f"Iteración {k+1}: {x_new}   Error: {error}\n")

        # Si el error es menor que la tolerancia, termina el método
        if error < tol:

            # Indica que el método convergió
            resultado.insert(tk.END, f"\n✅ Convergió en {k+1} iteraciones\n")

            # Devuelve la solución aproximada
            return x_new

        # Actualiza los valores para la siguiente iteración
        x = x_new

    # Si termina el ciclo sin converger
    resultado.insert(tk.END, "\n❌ No convergió\n")

    # Devuelve el último resultado calculado
    return x


# ---------------- CREAR MATRIZ ----------------

# Función que genera dinámicamente la matriz en la interfaz
def crear_matriz():

    # Declara la variable como global para usarla en otras funciones
    global entradas_A

    # Elimina los widgets anteriores del frame
    for widget in frame_matriz.winfo_children():
        widget.destroy()

    # Intenta obtener el número de ecuaciones ingresado
    try:
        n = int(entry_n.get())

    # Si el usuario escribe algo inválido
    except:
        messagebox.showerror("Error", "Ingrese un número válido")
        return

    # Lista donde se guardarán las entradas de la matriz
    entradas_A = []

    # Crea las filas de la matriz
    for i in range(n):

        # Lista temporal para cada fila
        fila = []

        # Etiqueta que indica la fila
        tk.Label(frame_matriz, text=f"Fila {i+1}", bg="#1e1e2f", fg="white").grid(row=i, column=0, padx=5)

        # Crea las columnas de la matriz
        for j in range(n):

            # Crea una caja de texto para ingresar cada valor
            entry = tk.Entry(frame_matriz, width=6, justify="center")

            # Coloca la caja en la posición de la matriz
            entry.grid(row=i, column=j+1, padx=3, pady=3)

            # Guarda la entrada en la fila
            fila.append(entry)

        # Guarda la fila completa en la matriz
        entradas_A.append(fila)


# ---------------- EJECUTAR ----------------

# Función que toma los datos ingresados y ejecuta Jacobi
def ejecutar():

    try:

        # Obtiene el número de ecuaciones
        n = int(entry_n.get())

        # Construye la matriz A leyendo la interfaz
        A = []
        for i in range(n):
            fila = []
            for j in range(n):

                # Convierte cada valor a número decimal
                fila.append(float(entradas_A[i][j].get()))

            A.append(fila)

        # Obtiene el vector b separado por espacios
        b = list(map(float, entry_b.get().split()))

        # Obtiene los valores iniciales
        x0 = list(map(float, entry_x0.get().split()))

        # Obtiene la tolerancia
        tol = float(entry_tol.get())

        # Obtiene el número máximo de iteraciones
        max_iter = int(entry_iter.get())

        # Ejecuta el método de Jacobi
        solucion = jacobi(A, b, x0, tol, max_iter)

        # Muestra la solución final
        resultado.insert(tk.END, f"\n🎯 Solución aproximada: {solucion}")

    # Si ocurre algún error
    except Exception as e:

        # Muestra el error en una ventana
        messagebox.showerror("Error", str(e))


# ---------------- INTERFAZ ----------------

# Crea la ventana principal
ventana = tk.Tk()

# Título de la ventana
ventana.title("Método de Jacobi - Profesional")

# Tamaño de la ventana
ventana.geometry("800x650")

# Color de fondo
ventana.configure(bg="#1e1e2f")


# Título principal de la aplicación
titulo = tk.Label(
    ventana, 
    text="Método de Jacobi", 
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="#00f5ff"
)

# Coloca el título en la ventana
titulo.pack(pady=10)


# Texto que pide el número de ecuaciones
tk.Label(ventana, text="Número de ecuaciones:", bg="#1e1e2f", fg="white").pack()

# Caja de texto para ingresar el número de ecuaciones
entry_n = tk.Entry(ventana, justify="center")
entry_n.pack(pady=5)


# Botón para generar la matriz
tk.Button(
    ventana, 
    text="Crear Matriz", 
    command=crear_matriz,
    bg="#00f5ff",
    fg="black",
    font=("Arial", 10, "bold")
).pack(pady=5)


# Frame donde se colocará la matriz
frame_matriz = tk.Frame(ventana, bg="#1e1e2f")
frame_matriz.pack(pady=10)


# Texto para ingresar el vector b
tk.Label(ventana, text="Vector b (separado por espacios):", bg="#1e1e2f", fg="white").pack()

# Entrada para el vector b
entry_b = tk.Entry(ventana, width=40, justify="center")
entry_b.pack(pady=5)


# Texto para ingresar los valores iniciales
tk.Label(ventana, text="Valores iniciales x0:", bg="#1e1e2f", fg="white").pack()

# Entrada para x0
entry_x0 = tk.Entry(ventana, width=40, justify="center")
entry_x0.pack(pady=5)


# Texto para la tolerancia
tk.Label(ventana, text="Tolerancia:", bg="#1e1e2f", fg="white").pack()

# Entrada para tolerancia
entry_tol = tk.Entry(ventana, justify="center")
entry_tol.pack(pady=5)


# Texto para iteraciones máximas
tk.Label(ventana, text="Máximo de iteraciones:", bg="#1e1e2f", fg="white").pack()

# Entrada para iteraciones
entry_iter = tk.Entry(ventana, justify="center")
entry_iter.pack(pady=5)


# Botón que ejecuta el método de Jacobi
tk.Button(
    ventana,
    text="Ejecutar Jacobi",
    command=ejecutar,
    bg="#00ff88",
    fg="black",
    font=("Arial", 12, "bold")
).pack(pady=10)


# Caja de texto donde se mostrarán los resultados
resultado = tk.Text(
    ventana,
    height=12,
    width=90,
    bg="#0f0f1a",
    fg="#00ff88"
)

# Coloca la caja de resultados en la ventana
resultado.pack(pady=10)


# Inicia el ciclo principal de la interfaz gráfica
ventana.mainloop()