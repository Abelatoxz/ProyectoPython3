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

archivo_usuarios = 'usuarios.txt'

if iniciar_sesion(archivo_usuarios):
    print("¡Bienvenido!")
else:
    pass

