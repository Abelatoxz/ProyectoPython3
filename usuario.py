import hashlib
def iniciar_sesion(archivo_usuarios):


  with open(archivo_usuarios, 'r') as f:
    for line in f:
      usuario_guardado, contraseña_guardada = line.strip().split('|')
      return usuario_guardado , contraseña_guardada
            


usuario,contraseña = iniciar_sesion("usuarios.txt")
print(usuario,contraseña)
