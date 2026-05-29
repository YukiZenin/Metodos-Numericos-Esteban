import tkinter as tk
from tkinter import messagebox, ttk
import math

def calcular_rk4():
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
        
        # Función auxiliar para evaluar la ecuación limpiamente
        def evaluar_f(x_val, y_val):
            entorno_matematico['x'] = x_val
            entorno_matematico['y'] = y_val
            return eval(f_str, {}, entorno_matematico)
        
        for i in range(1, pasos + 1):
            # Calculamos las 4 pendientes (k1, k2, k3, k4)
            k1 = evaluar_f(x, y)
            k2 = evaluar_f(x + h/2, y + (h/2) * k1)
            k3 = evaluar_f(x + h/2, y + (h/2) * k2)
            k4 = evaluar_f(x + h, y + h * k3)
            
            # Aplicamos la fórmula de Runge-Kutta
            y = y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
            x += h
            
            tabla.insert("", "end", values=(f"{i}", f"{x:.4f}", f"{y:.4f}"))
            
    except Exception as e:
        messagebox.showerror("Error de Cálculo", f"Revisa los datos ingresados.\nDetalle: {e}")

# ==========================================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ==========================================
root = tk.Tk()
root.title("Método de Runge-Kutta (RK4)")
# Ajustamos la altura de nuevo ya que quitamos la derivada
root.geometry("550x550")
root.configure(bg="#f4f6f9")
root.resizable(False, False)

# ==========================================
# ESTILOS (TEMA MODERNO)
# ==========================================
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#f4f6f9", font=("Segoe UI", 10))
style.configure("TLabelframe", background="#f4f6f9")
style.configure("TLabelframe.Label", font=("Segoe UI", 11, "bold"), background="#f4f6f9", foreground="#2c3e50")

# Color naranja para Runge-Kutta
style.configure("Accent.TButton", font=("Segoe UI", 11, "bold"), foreground="white", background="#e67e22", padding=8)
style.map("Accent.TButton", background=[("active", "#d35400")]) 

style.configure("Treeview", font=("Consolas", 10), rowheight=25, background="white", fieldbackground="white")
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#ecf0f1", foreground="#2c3e50")
style.map("Treeview", background=[("selected", "#e67e22")])

# ==========================================
# ENCABEZADO
# ==========================================
header_lbl = tk.Label(root, text="Calculadora Runge-Kutta", font=("Segoe UI", 18, "bold"), bg="#f4f6f9", fg="#2c3e50")
header_lbl.pack(pady=(15, 5))

subtitle_lbl = tk.Label(root, text="Runge-Kutta de 4to Orden (RK4) para EDOs", font=("Segoe UI", 10), bg="#f4f6f9", fg="#7f8c8d")
subtitle_lbl.pack(pady=(0, 15))

# ==========================================
# TARJETA DE PARÁMETROS
# ==========================================
frame = ttk.LabelFrame(root, text=" Ingreso de Datos ")
frame.pack(padx=20, pady=5, fill="x")

ttk.Label(frame, text="Función f(x, y):").grid(row=0, column=0, padx=(15, 5), pady=15, sticky="e")
entry_f = ttk.Entry(frame, width=35, font=("Consolas", 11))
entry_f.insert(0, "x - y") 
entry_f.grid(row=0, column=1, columnspan=3, padx=(0, 15), pady=15, sticky="w")

ttk.Label(frame, text="x₀ (Inicial):").grid(row=1, column=0, padx=(15, 5), pady=10, sticky="e")
entry_x0 = ttk.Entry(frame, width=10, font=("Consolas", 11))
entry_x0.insert(0, "0.0")
entry_x0.grid(row=1, column=1, sticky="w", pady=10)

ttk.Label(frame, text="y₀ (Inicial):").grid(row=1, column=2, padx=(15, 5), pady=10, sticky="e")
entry_y0 = ttk.Entry(frame, width=10, font=("Consolas", 11))
entry_y0.insert(0, "2.0")
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
btn = ttk.Button(root, text="⚡ Calcular Resultados", command=calcular_rk4, style="Accent.TButton", cursor="hand2")
btn.pack(pady=15)

# ==========================================
# TABLA DE RESULTADOS
# ==========================================
tabla_frame = tk.Frame(root)
tabla_frame.pack(padx=20, pady=(0, 20), fill="both", expand=True)

columnas = ("Iteración", "x", "y (RK4)")
tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")

for c in columnas:
    tabla.heading(c, text=c)
    tabla.column(c, width=150, anchor="center")

scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)

tabla.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
