archivo = 'libros.txt'
libros = []
with open(archivo, 'r') as f:
    for line in f:
        libro_info = line.strip().split(',')
        if libro_info[0] == isbn
            return libro_info

print(libros)
