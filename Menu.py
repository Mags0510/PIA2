import os
import sys

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Análisis de Tráfico (trafico.py)")
    print("2. Detección de Intrusos (deteccion.py)")
    print("3. Consulta en Shodan (API_Shodan.py)")
    print("4. Reporte de IP Abuse (API_IPABUSE.py)")
    print("5. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        print("\nAbriendo tráfico...")
        os.system("python3 trafico.py")
    elif opcion == "2":
        print("\nAbriendo detección...")
        os.system("python3 deteccion.py")
    elif opcion == "3":
        print("\nAbriendo Shodan...")
        os.system("python3 API_Shodan.py")
    elif opcion == "4":
        print("\nAbriendo IP Abuse...")
        os.system("python3 API_IPABUSE.py")
    elif opcion == "5":
        print("\nAbriendo Complejo...")
        os.system("python3 Complejo.py")
    elif opcion == "6":
        print("Saliendo del programa...")
        sys.exit(0)
    else:
        print("Opción inválida. Intente de nuevo.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
