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
    mayusculas = string.ascii_uppercase      # A-Z
    minusculas = string.ascii_lowercase      # a-z
    numeros = string.digits                  # 0-9
    especiales = "!@#$%"                     # Caracteres especiales
    
    # Combinar todos los caracteres
    todos_caracteres = mayusculas + minusculas + numeros + especiales
    
    # Generar contraseña aleatoria
    contraseña = [
        random.choice(mayusculas),           # Al menos 1 mayúscula
        random.choice(minusculas),           # Al menos 1 minúscula
        random.choice(numeros),              # Al menos 1 número
        random.choice(especiales)            # Al menos 1 carácter especial
    ]
    
    # Completar el resto de la contraseña con caracteres aleatorios
    for i in range(longitud - 4):
        contraseña.append(random.choice(todos_caracteres))
    
    # Mezclar la contraseña para que no siempre tenga el mismo patrón
    random.shuffle(contraseña)
    
    # Convertir la lista a string
    contraseña_final = ''.join(contraseña)
    
    # Mostrar la contraseña generada
    print("\n" + "-"*50)
    print(f"✓ Contraseña generada: {contraseña_final}")
    print("-"*50)
    
    # Preguntar si desea generar otra contraseña
    while True:
        respuesta = input("\n¿Desea generar otra contraseña? (sí/no): ").lower().strip()
        if respuesta in ["sí", "si", "s", "yes", "y"]:
            break
        elif respuesta in ["no", "n"]:
            print("\n✓ ¡Gracias por usar el generador! ¡Hasta luego!")
            exit()
        else:
            print("❌ Ingrese 'sí' o 'no'.")