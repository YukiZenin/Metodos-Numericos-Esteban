import tkinter as tk
from tkinter import messagebox, ttk
import math

def calcular_euler():
    try:
        f_str = entry_f.get()
        
        # Reemplazamos comas por puntos
        x = float(entry_x0.get().replace(',', '.'))
        y = float(entry_y0.get().replace(',', '.'))
        h = float(entry_h.get().replace(',', '.'))
        pasos = int(entry_pasos.get())
        
        for item in tabla.get_children():
            tabla.delete(item)
            
        tabla.insert("", "end", values=("0", f"{x:.4f}", f"{y:.4f}"))
        
        entorno_matematico = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        
        for i in range(1, pasos + 1):
            entorno_matematico['x'] = x
            entorno_matematico['y'] = y
            
            f_val = eval(f_str, {}, entorno_matematico)
            y = y + h * f_val
            x += h
            
            tabla.insert("", "end", values=(f"{i}", f"{x:.4f}", f"{y:.4f}"))
            
    except Exception as e:
        messagebox.showerror("Error de Cálculo", f"Revisa los datos ingresados.\nDetalle: {e}")

# ==========================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ==========================================
root = tk.Tk()
root.title("Método de Euler")
root.geometry("550x550")
root.configure(bg="#f4f6f9")  # Fondo azul grisáceo muy claro
root.resizable(False, False)  # Evitar que se deforme la ventana

# ==========================================
# ESTILOS (TEMA MODERNO)
# ==========================================
style = ttk.Style()
style.theme_use("clam")  # Tema más moderno que el clásico de Windows/Mac

# Estilo para los Labels y Frames
style.configure("TLabel", background="#f4f6f9", font=("Segoe UI", 10))
style.configure("TLabelframe", background="#f4f6f9")
style.configure("TLabelframe.Label", font=("Segoe UI", 11, "bold"), background="#f4f6f9", foreground="#2c3e50")

# Estilo para el Botón
style.configure("Accent.TButton", font=("Segoe UI", 11, "bold"), foreground="white", background="#2980b9", padding=8)
style.map("Accent.TButton", background=[("active", "#3498db")]) # Color al pasar el mouse

# Estilo para la Tabla (Treeview)
style.configure("Treeview", font=("Consolas", 10), rowheight=25, background="white", fieldbackground="white")
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#ecf0f1", foreground="#2c3e50")
style.map("Treeview", background=[("selected", "#3498db")])

# ==========================================
# ENCABEZADO
# ==========================================
header_lbl = tk.Label(root, text="Calculadora de Euler", font=("Segoe UI", 18, "bold"), bg="#f4f6f9", fg="#2c3e50")
header_lbl.pack(pady=(15, 5))

subtitle_lbl = tk.Label(root, text="Resuelve ecuaciones diferenciales ordinarias", font=("Segoe UI", 10), bg="#f4f6f9", fg="#7f8c8d")
subtitle_lbl.pack(pady=(0, 15))

# ==========================================
# TARJETA DE PARÁMETROS
# ==========================================
frame = ttk.LabelFrame(root, text=" Ingreso de Datos ")
frame.pack(padx=20, pady=5, fill="x")

# Usamos un grid con más padding (espaciado)
ttk.Label(frame, text="Función f(x, y):").grid(row=0, column=0, padx=(15, 5), pady=15, sticky="e")
entry_f = ttk.Entry(frame, width=35, font=("Consolas", 11))
entry_f.insert(0, "2*x - y")
entry_f.grid(row=0, column=1, columnspan=3, padx=(0, 15), pady=15, sticky="w")

ttk.Label(frame, text="x₀ (Inicial):").grid(row=1, column=0, padx=(15, 5), pady=10, sticky="e")
entry_x0 = ttk.Entry(frame, width=10, font=("Consolas", 11))
entry_x0.insert(0, "0.0")
entry_x0.grid(row=1, column=1, sticky="w", pady=10)

ttk.Label(frame, text="y₀ (Inicial):").grid(row=1, column=2, padx=(15, 5), pady=10, sticky="e")
entry_y0 = ttk.Entry(frame, width=10, font=("Consolas", 11))
entry_y0.insert(0, "1.0")
entry_y0.grid(row=1, column=3, sticky="w", pady=10, padx=(0, 15))

ttk.Label(frame, text="Tamaño paso (h):").grid(row=2, column=0, padx=(15, 5), pady=(10, 15), sticky="e")
entry_h = ttk.Entry(frame, width=10, font=("Consolas", 11))
entry_h.insert(0, "0.1")
entry_h.grid(row=2, column=1, sticky="w", pady=(10, 15))

ttk.Label(frame, text="Núm. de pasos:").grid(row=2, column=2, padx=(15, 5), pady=(10, 15), sticky="e")
entry_pasos = ttk.Entry(frame, width=10, font=("Consolas", 11))
entry_pasos.insert(0, "5")
entry_pasos.grid(row=2, column=3, sticky="w", pady=(10, 15), padx=(0, 15))

# ==========================================
# BOTÓN DE ACCIÓN
# ==========================================
btn = ttk.Button(root, text="⚡ Calcular Resultados", command=calcular_euler, style="Accent.TButton", cursor="hand2")
btn.pack(pady=15)

# ==========================================
# TABLA DE RESULTADOS
# ==========================================
tabla_frame = tk.Frame(root)
tabla_frame.pack(padx=20, pady=(0, 20), fill="both", expand=True)

columnas = ("Iteración", "x", "y (Euler)")
tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")

for c in columnas:
    tabla.heading(c, text=c)
    tabla.column(c, width=150, anchor="center")

# Añadir Scrollbar a la tabla
scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)

tabla.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
