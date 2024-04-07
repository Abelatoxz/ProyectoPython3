import tkinter as tk
from tkinter import messagebox
from repositorio import *

def obtener_hash_md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    intentos = 3
    while intentos != 0:
        with open(archivo_usuarios, 'r') as f:
            for line in f:
                usuario_guardado, contraseña_guardada = line.strip().split('|')
                if usuario == usuario_guardado and obtener_hash_md5(contraseña) == contraseña_guardada:
                    messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso.")
                    with open('usuario.txt', 'a') as f:
                        f.write(f"{usuario}|{obtener_hash_md5(contraseña)}\n")
                    return
            messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos.")
            intentos -= 1
    messagebox.showerror("Error de inicio de sesión", "Ha superado el número máximo de intentos.")

def mostrar_libro():
    isbn_a_buscar = entry_isbn.get()
    libro_encontrado = mostrar_libro(isbn_a_buscar, archivo_libros)
    if libro_encontrado:
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, f"Información del libro:\nISBN: {libro_encontrado[0]}\nTítulo: {libro_encontrado[1]}\nAutor: {libro_encontrado[2]}")
        resultado_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Libro no encontrado", "Libro no encontrado.")

def mostrar_todos_libros():
    libros = mostrar_todos_libros(archivo_libros)
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete("1.0", tk.END)
    for libro in libros:
        resultado_text.insert(tk.END, f"ISBN: {libro[0]}\nTítulo: {libro[1]}\nAutor: {libro[2]}\n\n")
    resultado_text.config(state=tk.DISABLED)

def agregar_libro():
    isbn = entry_nuevo_isbn.get()
    titulo = entry_nuevo_titulo.get()
    autor = entry_nuevo_autor.get()
    with open(archivo_libros, 'a') as f:
        f.write(f"{isbn}|{titulo}|{autor}\n")
    messagebox.showinfo("Libro agregado", "Libro agregado correctamente.")

def eliminar_libro():
    isbn = entry_eliminar_isbn.get()
    libros = []
    with open(archivo_libros, 'r') as f:
        for line in f:
            libro_info = line.strip().split('|')
            if libro_info[0] != isbn:
                libros.append(libro_info)
    with open(archivo_libros, 'w') as f:
        for libro in libros:
            f.write('|'.join(libro) + '\n')
    messagebox.showinfo("Libro eliminado", "Libro eliminado correctamente.")

def editar_libro():
    isbn = entry_editar_isbn.get()
    nueva_isbn = entry_nueva_isbn.get()
    nuevo_titulo = entry_nuevo_titulo_editar.get()
    nuevo_autor = entry_nuevo_autor_editar.get()
    libros = []
    with open(archivo_libros, 'r') as f:
        for line in f:
            libro_info = line.strip().split('|')
            if libro_info[0] == isbn:
                libros.append([nueva_isbn, nuevo_titulo, nuevo_autor])
            else:
                libros.append(libro_info)
    with open(archivo_libros, 'w') as f:
        for libro in libros:
            f.write('|'.join(libro) + '\n')
    messagebox.showinfo("Libro editado", "Libro editado correctamente.")

def cerrar_sesion():
    try:
        os.remove('usuario.txt')
    except FileNotFoundError:
        pass  # El archivo ya está eliminado o no existe
    exit()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Gestor de Librería")

frame_login = tk.Frame(root)
frame_login.pack()

label_usuario = tk.Label(frame_login, text="Usuario:")
label_usuario.grid(row=0, column=0, padx=5, pady=5)
entry_usuario = tk.Entry(frame_login)
entry_usuario.grid(row=0, column=1, padx=5, pady=5)

label_contraseña = tk.Label(frame_login, text="Contraseña:")
label_contraseña.grid(row=1, column=0, padx=5, pady=5)
entry_contraseña = tk.Entry(frame_login, show="*")
entry_contraseña.grid(row=1, column=1, padx=5, pady=5)

button_login = tk.Button(frame_login, text="Iniciar Sesión", command=iniciar_sesion)
button_login.grid(row=2, columnspan=2, padx=5, pady=5)

frame_menu = tk.Frame(root)

opcion_elegida = tk.StringVar()
opcion_elegida.set("")

menu_opciones = tk.OptionMenu(frame_menu, opcion_elegida, "Mostrar un libro por ISBN",
                                        "Mostrar todos los libros", "Agregar un libro", "Eliminar un libro",
                                        "Editar un libro", "Salir", "Cerrar Sesión")
menu_opciones.pack()

frame_menu.pack()

frame_resultado = tk.Frame(root)
resultado_text = tk.Text(frame_resultado, height=10, width=50)
resultado_text.pack()
frame_resultado.pack()

root.mainloop()
