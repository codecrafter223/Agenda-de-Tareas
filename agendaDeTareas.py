from tkinter import *

root = Tk()
root.title("Agenda de Tareas")
root.geometry("400x400")

# Frame principal
frame = Frame(root)
frame.pack(pady=10)

# Frame para la lista de tareas
lista_frame = Frame(frame)
lista_frame.pack(pady=10)

# Crear un Canvas y un Frame para la lista de tareas
canvas = Canvas(lista_frame)
scrollbar = Scrollbar(lista_frame, orient="vertical", command=canvas.yview)
tareas_frame = Frame(canvas)

# Configurar el scrollbar para que funcione con el canvas
tareas_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=tareas_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Empaquetar el canvas y el scrollbar
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# Lista para almacenar las tareas (Checkbuttons)
tareas = []  # Lista para almacenar las variables y referencias de los Checkbuttons

# Función para cambiar el color del Checkbutton y marcarlo
def cambiar_color(var, check):
    if var.get() == 1:  # Si la tarea está marcada
        check.config(bg="green", fg="white", font=("Arial", "10", "overstrike"))  # Cambiar color y tachar
    else:
        check.config(bg=root.cget("bg"), fg="black", font=("Arial", "10"))  # Restablecer al color original

# Función para agregar un Checkbutton
def agregar():
    tarea = tarea_entry.get()  # Obtener el texto del Entry
    if tarea:  # Verificar que el Entry no esté vacío
        var = IntVar()  # Crear una variable de control para el Checkbutton
        check = Checkbutton(tareas_frame, text=tarea, variable=var, anchor="w", 
                            command=lambda: cambiar_color(var, check))
        check.pack(fill="x", padx=10, pady=2)  # Colocar el Checkbutton en tareas_frame y alinearlo
        tareas.append((check, var))  # Guardar la referencia del Checkbutton y su variable en la lista
        tarea_entry.delete(0, END)  # Limpiar el Entry después de agregar

def eliminar():
    for check, var in tareas[:]:  # Iterar sobre una copia de la lista de tareas
        if var.get() == 1:  # Verificar si la tarea está marcada
            check.pack_forget()  # Eliminar el Checkbutton de la interfaz
            tareas.remove((check, var))  # Eliminar de la lista de tareas

# Etiquetas
tarea_label = Label(frame, text="Escribe una tarea")
tarea_label.pack()

# Entrada
tarea_entry = Entry(frame, width=30)
tarea_entry.pack(pady=10)

# Botones
agregar_boton = Button(frame, text="Agregar tarea", command=agregar)
agregar_boton.pack(pady=5)

eliminar_boton = Button(frame, text="Eliminar tarea seleccionada", command=eliminar)
eliminar_boton.pack(pady=5)

root.mainloop()
