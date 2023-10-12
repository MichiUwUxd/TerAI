import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import scrolledtext
from tkinter import filedialog
from tkcalendar import Calendar
import os
import psutil
import time

# Funciones para abrir aplicaciones
def open_calculator():
    calculator_window = tk.Toplevel(root)
    calculator_window.title("Calculadora")
    
    def click(event):
        text = event.widget.cget("text")
        
        if text == "=":
            try:
                result = str(eval(screen.get()))
                screen.set(result)
            except Exception as e:
                screen.set("EBP+++")
        elif text == "C":
            screen.set("")
        else:
            screen.set(screen.get() + text)

    screen = tk.StringVar()
    entry = tk.Entry(calculator_window, textvar=screen, font="lucida 20 bold")
    entry.pack(fill="both", ipadx=8, padx=10, pady=10)

    button_frame = tk.Frame(calculator_window)
    button_frame.pack()

    buttons = [
        "7", "8", "9", "+",
        "4", "5", "6", "-",
        "1", "2", "3", "*",
        "C", "0", "=", "/"
    ]

    i = 0
    for button in buttons:
        b = tk.Button(button_frame, text=button, font="lucida 15 bold", padx=10, pady=10)
        b.grid(row=i // 4, column=i % 4)
        b.bind("<Button-1>", click)
        i += 1

def open_notepad():
    notepad_window = tk.Toplevel(root)
    notepad_window.title("Bloc de Notas")

    def save():
        filename = askstring("Guardar", "Nombre del archivo:")
        if filename:
            # Agregar la extensión ".txt" si no se especifica
            if not filename.endswith(".txt"):
                filename += ".txt"
            
            content = text.get("1.0", "end-1c")
            with open(filename, "w") as file:
                file.write(content)
            messagebox.showinfo("Informe", f"Archivo '{filename}' guardado exitamente.")

    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Todos los archivos", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text.delete("1.0", "end")
                text.insert("1.0", content)

    text = scrolledtext.ScrolledText(notepad_window)
    text.pack()

    save_button = tk.Button(notepad_window, text="Guardar", command=save, padx=5, pady=5)
    save_button.pack()

    open_button = tk.Button(notepad_window, text="Abrir", command=open_file, padx=5, pady=5)
    open_button.pack()

def open_calendar():
    calendar_window = tk.Toplevel(root)
    calendar_window.title("Calendario")

    def show_selected_date():
        selected_date = calendar.get_date()
        date_label.config(text=f"Fecha seleccionada: {selected_date}")

    calendar = Calendar(calendar_window, font="lucida 12 bold")
    calendar.pack(pady=10)

    show_date_button = tk.Button(calendar_window, text="Mostrar Fecha Seleccionada", command=show_selected_date, padx=5, pady=5)
    show_date_button.pack()

    date_label = tk.Label(calendar_window, text="", font="lucida 12 bold")
    date_label.pack(pady=10)

def open_file_manager():
    file_manager_window = tk.Toplevel(root)
    file_manager_window.title("Gestor de Archivos")

    def open_file_dialog():
        file_path = filedialog.askopenfilename(filetypes=[("Todos los archivos", "*.*")])
        if file_path:
            file_label.config(text=f"Archivo seleccionado: {file_path}")

    file_open_button = tk.Button(file_manager_window, text="Abrir Archivo", command=open_file_dialog, padx=5, pady=5)
    file_open_button.pack()

    file_label = tk.Label(file_manager_window, text="", font="lucida 12 bold")
    file_label.pack(pady=10)

def open_task_manager():
    task_manager_window = tk.Toplevel(root)
    task_manager_window.title("Gestor de Tareas y Rendimiento")

    def get_performance():
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        performance_label.config(text=f"Uso de CPU: {cpu_usage}%  Uso de memoria: {memory_usage}%")
        root.after(1000, get_performance)

    performance_label = tk.Label(task_manager_window, text="", font=("lucida", 12, "bold"))
    performance_label.pack(pady=10)
    get_performance()

def shutdown():
    confirmation = messagebox.askquestion("Advertencia", "Estas seguro de que deseas apagar el sistema?")
    if confirmation == "Si":
        root.quit()

# Configuración de la ventana principal con fondo celeste
root = tk.Tk()
root.title("TerAI - Python")
root.geometry("800x600")
root.configure(bg="lightblue")

# Botones para abrir aplicaciones
calculator_button = tk.Button(root, text="Calculadora", font=("lucida", 20, "bold"), padx=10, pady=10, command=open_calculator)
calculator_button.pack()

notepad_button = tk.Button(root, text="Bloc de Notas", font=("lucida", 20, "bold"), padx=10, pady=10, command=open_notepad)
notepad_button.pack()

calendar_button = tk.Button(root, text="Calendario", font=("lucida", 20, "bold"), padx=10, pady=10, command=open_calendar)
calendar_button.pack()

file_manager_button = tk.Button(root, text="Gestor de Archivos", font=("lucida", 20, "bold"), padx=10, pady=10, command=open_file_manager)
file_manager_button.pack()

task_manager_button = tk.Button(root, text="Rendimiento", font=("lucida", 20, "bold"), padx=10, pady=10, command=open_task_manager)
task_manager_button.pack()

shutdown_button = tk.Button(root, text="Apagar", font=("lucida", 20, "bold"), padx=10, pady=10, command=shutdown)
shutdown_button.pack()

root.mainloop()
