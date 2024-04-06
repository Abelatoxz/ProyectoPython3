def mostrar_libro(isbn, archivo):
    try: 
       with open(archivo, 'r') as f:
            for line in f:
                libro_info = line.strip().split('|')
                if libro_info[0] == isbn:
                    return libro_info
            return None
    except:
        print("No se encontro el archivo")

def mostrar_todos_libros(archivo):
    libros = []
    try:
        with open(archivo, 'r') as f:
            for line in f:
                libros.append(line.strip().split('|'))
            return libros
    except:
        print("No se encontro el archivo")

def agregar_libro(archivo):
    isbn = input("Ingrese el ISBN del libro: ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el nombre del autor del libro: ")
    with open(archivo, 'a') as f:
        f.write(f"{isbn}|{titulo}|{autor}\n")
    print("Libro agregado correctamente.")

def eliminar_libro(archivo):
    isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
    libros = []
    with open(archivo, 'r') as f:
        for line in f:
            libro_info = line.strip().split('|')
            if libro_info[0] != isbn:
                libros.append(libro_info)
    with open(archivo, 'w') as f:
        for libro in libros:
            f.write('|'.join(libro) + '\n')
    print("Libro eliminado correctamente.")

def editar_libro(archivo):
    isbn = input("Ingrese el ISBN del libro que desea editar: ")
    nueva_isbn = input("Ingrese el nuevo ISBN del libro: ")
    nuevo_titulo = input("Ingrese el nuevo título del libro: ")
    nuevo_autor = input("Ingrese el nuevo autor del libro: ")
    libros = []
    with open(archivo, 'r') as f:
        for line in f:
            libro_info = line.strip().split('|')
            if libro_info[0] == isbn:
                libros.append([nueva_isbn, nuevo_titulo, nuevo_autor])
            else:
                libros.append(libro_info)
    with open(archivo, 'w') as f:
        for libro in libros:
            f.write('|'.join(libro) + '\n')
    print("Libro editado correctamente.")

import hashlib

def obtener_hash_md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

def iniciar_sesion(archivo_usuarios):
    intentos = 3
    while intentos != 0 :
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        with open(archivo_usuarios, 'r') as f:
            for line in f:
                usuario_guardado, contraseña_guardada = line.strip().split('|')
                if usuario == usuario_guardado and obtener_hash_md5(contraseña) == contraseña_guardada:
                    print("Inicio de sesión exitoso.")
                    return True
            print("Usuario o contraseña incorrectos. Inténtelo de nuevo.", "Te quedan: ",intentos - 1)
            intentos -= 1

    print("Ha superado el número máximo de intentos. Saliendo del programa.")
    return False



