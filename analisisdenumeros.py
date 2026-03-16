# Inicializar variables
numeros = []
suma = 0
cantidad_pares = 0
cantidad_impares = 0

print("\n" + "="*50)
print("        ANÁLISIS DE NÚMEROS")
print("="*50)
print("\nIngrese números uno por uno.")
print("Cuando desee terminar, ingrese 0.")
print("-"*50)

# Bucle para capturar números
while True:
    try:
        numero = int(input("\nIngrese un número (0 para terminar): "))
        
        # Si ingresa 0, terminar la captura
        if numero == 0:
            break
        
        # Agregar el número a la lista
        numeros.append(numero)
        
        # Acumular la suma
        suma += numero
        
        # Contar pares e impares
        if numero % 2 == 0:
            cantidad_pares += 1
        else:
            cantidad_impares += 1
        
        print(f"✓ Número registrado: {numero}")
    
    except ValueError:
        print("❌ Por favor, ingrese un número entero válido.")

# Validar que se ingresaron números
if len(numeros) == 0:
    print("\n❌ No ingresó ningún número. El programa terminará.")
else:
    # Calcular estadísticas
    cantidad_total = len(numeros)
    promedio = suma / cantidad_total
    numero_mayor = max(numeros)
    numero_menor = min(numeros)
    
    # Mostrar resultados
    print("\n" + "="*50)
    print("        RESULTADOS DEL ANÁLISIS")
    print("="*50)
    print(f"\nCantidad total de números: {cantidad_total}")
    print(f"Suma de todos los números: {suma}")
    print(f"Promedio de los números: {promedio:.2f}")
    print(f"Número mayor: {numero_mayor}")
    print(f"Número menor: {numero_menor}")
    print(f"Cantidad de números pares: {cantidad_pares}")
    print(f"Cantidad de números impares: {cantidad_impares}")
    print("\n" + "="*50)
    print("✓ ¡Análisis completado!")
    print("="*50)