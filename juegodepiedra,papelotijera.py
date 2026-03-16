import random

# Contadores de victorias
victorias_usuario = 0
victorias_computadora = 0
empates = 0

# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]

# Bucle principal del juego
while True:
    print("\n" + "="*50)
    print("      PIEDRA, PAPEL O TIJERA")
    print("="*50)
    print(f"\nMarcador:")
    print(f"Tú: {victorias_usuario} | Computadora: {victorias_computadora} | Empates: {empates}")
    print("\n¿Qué eliges?")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    
    # Pedir elección del usuario
    while True:
        eleccion_usuario = input("\nIngrese su elección (piedra/papel/tijera) o 'salir': ").lower().strip()
        
        if eleccion_usuario == "salir":
            print("\n" + "="*50)
            print("          MARCADOR FINAL")
            print("="*50)
            print(f"Tú: {victorias_usuario} victorias")
            print(f"Computadora: {victorias_computadora} victorias")
            print(f"Empates: {empates}")
            print("\n✓ ¡Gracias por jugar! ¡Hasta luego!")
            print("="*50)
            exit()
        
        if eleccion_usuario in opciones:
            break
        else:
            print("❌ Opción inválida. Ingrese 'piedra', 'papel', 'tijera' o 'salir'.")
    
    # Elección aleatoria de la computadora
    eleccion_computadora = random.choice(opciones)
    
    # Mostrar elecciones
    print("\n" + "-"*50)
    print(f"Tu elección: {eleccion_usuario.upper()}")
    print(f"Elección de la computadora: {eleccion_computadora.upper()}")
    print("-"*50)
    
    # Determinar el ganador
    if eleccion_usuario == eleccion_computadora:
        print("\n🤝 ¡EMPATE! Ambos eligieron lo mismo.")
        empates += 1
    
    # Piedra gana a tijera
    elif eleccion_usuario == "piedra" and eleccion_computadora == "tijera":
        print("\n🎉 ¡GANASTE! Piedra aplasta tijera.")
        victorias_usuario += 1
    
    # Papel gana a piedra
    elif eleccion_usuario == "papel" and eleccion_computadora == "piedra":
        print("\n🎉 ¡GANASTE! Papel cubre piedra.")
        victorias_usuario += 1
    
    # Tijera gana a papel
    elif eleccion_usuario == "tijera" and eleccion_computadora == "papel":
        print("\n🎉 ¡GANASTE! Tijera corta papel.")
        victorias_usuario += 1
    
    # Computadora gana
    else:
        print("\n💻 ¡PERDISTE! La computadora te venció.")
        victorias_computadora += 1
    
    # Pregunta si quiere jugar otra vez
    while True:
        jugar_otra_vez = input("\n¿Deseas jugar otra vez? (sí/no): ").lower().strip()
        if jugar_otra_vez in ["sí", "si", "s", "yes", "y"]:
            break
        elif jugar_otra_vez in ["no", "n"]:
            print("\n" + "="*50)
            print("          MARCADOR FINAL")
            print("="*50)
            print(f"Tú: {victorias_usuario} victorias")
            print(f"Computadora: {victorias_computadora} victorias")
            print(f"Empates: {empates}")
            print("\n✓ ¡Gracias por jugar! ¡Hasta luego!")
            print("="*50)
            exit()
        else:
            print("❌ Ingrese 'sí' o 'no'.")