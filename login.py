import hashlib

def obtener_hash_md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

def iniciar_sesion(archivo_usuarios):
    intentos = 0
    while intentos < 3:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        with open(archivo_usuarios, 'r') as f:
            for line in f:
                usuario_guardado, contraseña_guardada = line.strip().split('|')
                if usuario == usuario_guardado and obtener_hash_md5(contraseña) == contraseña_guardada:
                    print("Inicio de sesión exitoso.")
                    return True
            print("Usuario o contraseña incorrectos. Inténtelo de nuevo.")
            intentos += 1

    print("Ha superado el número máximo de intentos. Saliendo del programa.")
    return False

# Ejemplo de uso:
archivo_usuarios = 'usuarios.txt'

if iniciar_sesion(archivo_usuarios):
    # Aquí puedes agregar la lógica adicional una vez que el usuario ha iniciado sesión correctamente.
    print("¡Bienvenido!")
else:
    # Puedes manejar el comportamiento cuando el usuario no inicia sesión correctamente.
    pass

