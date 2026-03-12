import random
import string

# Bucle principal del programa
while True:
    print("\n" + "="*50)
    print("     GENERADOR DE CONTRASEÑAS ALEATORIAS")
    print("="*50)
    
    # Pedir y validar la longitud de la contraseña
    while True:
        try:
            longitud = int(input("\nIngrese la longitud de la contraseña (8-20): "))
            if 8 <= longitud <= 20:
                break
            else:
                print("❌ La longitud debe estar entre 8 y 20. Intente de nuevo.")
        except ValueError:
            print("❌ Por favor, ingrese un número válido.")
    
    # Definir caracteres disponibles
    mayuscula