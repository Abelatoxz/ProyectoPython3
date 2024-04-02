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
    with open(archivo, 'r') as f:
        for line in f:
            libros.append(line.strip().split('|'))
    return libros

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

