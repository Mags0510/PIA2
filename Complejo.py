from cryptography.fernet import Fernet, MultiFernet

# Generamos las llaves para MultiFernet
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
f = MultiFernet([key1, key2])

# Lista para almacenar mensajes encriptados y desencriptados
mensajes = []

# Función para encriptar
def encrypt():
    mensaje = input("Inserte su mensaje a encriptar: ")
    token = f.encrypt(mensaje.encode())  # Se codifica el mensaje en bytes
    print("Mensaje encriptado:", token)
    mensajes.append((mensaje, token))  # Guardamos el mensaje original y encriptado
    return token

# Función para desencriptar
def decrypt(token):
    tokenD = f.decrypt(token).decode()  # Desencriptamos y decodificamos a string
    return tokenD

# Menú con opciones
def Menu():
    while True:
        print("\nBienvenido, seleccione la opción que desee:")
        print("1. Encriptar mi mensaje.")
        print("2. Desencriptar mi mensaje (solo si ya se encriptó algún mensaje).")
        print("3. Mostrar el mensaje encriptado y el desencriptado.")
        print("4. Mostrar mis últimos n mensajes.")
        print("5. Salir.")

        try:
            x = int(input("Ingrese una opción: "))
        except ValueError:
            print("Valor no válido, vuelva a intentar.")
            continue
        
        if x == 1:
            # Encripta el mensaje
            encrypt()

        elif x == 2:
            # Desencripta el último mensaje encriptado
            if mensajes:
                mensaje_original, token = mensajes[-1]
                print("Mensaje desencriptado:", decrypt(token))
            else:
                print("Aún no se ha encriptado ningún mensaje.")

        elif x == 3:
            # Muestra el mensaje encriptado y desencriptado
            if mensajes:
                mensaje_original, token = mensajes[-1]
                print("Mensaje encriptado:", token)
                print("Mensaje desencriptado:", decrypt(token))
            else:
                print("Aún no se ha encriptado ningún mensaje.")

        elif x == 4:
            # Muestra los últimos n mensajes
            if mensajes:
                try:
                    n = int(input("¿Cuántos mensajes desea ver?: "))
                    for i, (mensaje_original, token) in enumerate(mensajes[-n:], start=1):
                        print(f"Mensaje {i}:")
                        print(f"Encriptado: {token}")
                        print(f"Desencriptado: {decrypt(token)}")
                except ValueError:
                    print("Por favor ingrese un número válido.")
            else:
                print("No hay mensajes para mostrar.")

        elif x == 5:
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, vuelva a intentar.")

# Iniciar el menú
Menu()
