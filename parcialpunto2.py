"""Gestión simple de inventario de productos con menú interactivo.

Funciones separadas para cada operación:
- agregar_producto(inventario)
- ver_inventario(inventario)
- buscar_producto(inventario)
- actualizar_cantidad(inventario)
- eliminar_producto(inventario)

Los productos se almacenan en un diccionario en memoria. Las cantidades
y precios deben ser números positivos. El menú se repite hasta salir.
"""

from typing import Dict, Any


def agregar_producto(inventario: Dict[str, Dict[str, Any]]) -> None:
    """Pide nombre, cantidad y precio, valida y añade al inventario."""
    nombre = input("jabon: ").strip()
    if not nombre:
        print("Nombre jabon. Operación cancelada.")
        return
    try:
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
    except ValueError:
        print("Cantidad inválida. Debe ser un número entero.")
        return
    try:
        precio = float(input("Precio (por unidad): "))
        if precio <= 0:
            print("El precio debe ser un número positivo.")
            return
    except ValueError:
        print("Precio inválido. Debe ser un número.")
        return

    clave = nombre.lower()
    inventario[clave] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    print(f"Producto '{nombre}' agregado/actualizado correctamente.")


def ver_inventario(inventario: Dict[str, Dict[str, Any]]) -> None:
    """Muestra todos los productos con cantidad, precio y valor total por producto."""
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\nInventario:")
    print(f"{'Producto':30} {'Cant.':>6} {'Precio':>10} {'Total':>12}")
    print("-" * 60)
    total_general = 0.0
    for item in inventario.values():
        nombre = item['nombre']
        cantidad = item['cantidad']
        precio = item['precio']
        total = cantidad * precio
        total_general += total
        print(f"{nombre:30} {cantidad:6d} {precio:10.2f} {total:12.2f}")
    print("-" * 60)
    print(f"Valor total del inventario: {total_general:.2f}\n")


def buscar_producto(inventario: Dict[str, Dict[str, Any]]) -> None:
    """Busca un producto por nombre e imprime sus datos si existe."""
    nombre = input("Nombre del producto a buscar: ").strip()
    if not nombre:
        print("Nombre vacío. Operación cancelada.")
        return
    clave = nombre.lower()
    item = inventario.get(clave)
    if item:
        total = item['cantidad'] * item['precio']
        print(f"Producto: {item['nombre']}")
        print(f"Cantidad: {item['cantidad']}")
        print(f"Precio: {item['precio']:.2f}")
        print(f"Valor total: {total:.2f}")
    else:
        print("Producto no encontrado.")


def actualizar_cantidad(inventario: Dict[str, Dict[str, Any]]) -> None:
    """Actualiza la cantidad de un producto existente."""
    nombre = input("Nombre del producto a actualizar: ").strip()
    if not nombre:
        print("Nombre vacío. Operación cancelada.")
        return
    clave = nombre.lower()
    item = inventario.get(clave)
    if not item:
        print("Producto no encontrado.")
        return
    try:
        nueva_cantidad = int(input("Nueva cantidad: "))
        if nueva_cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
    except ValueError:
        print("Cantidad inválida. Debe ser un número entero.")
        return
    item['cantidad'] = nueva_cantidad
    print(f"Cantidad de '{item['nombre']}' actualizada a {nueva_cantidad}.")


def eliminar_producto(inventario: Dict[str, Dict[str, Any]]) -> None:
    """Elimina un producto por nombre si existe."""
    nombre = input("Nombre del producto a eliminar: ").strip()
    if not nombre:
        print("Nombre vacío. Operación cancelada.")
        return
    clave = nombre.lower()
    if clave in inventario:
        del inventario[clave]
        print(f"Producto '{nombre}' eliminado.")
    else:
        print("Producto no encontrado.")


def menu() -> None:
    """Bucle del menú principal hasta que el usuario elija salir."""
    inventario: Dict[str, Dict[str, Any]] = {}
    while True:
        print("\nMenú:\n1. Agregar producto\n2. Ver inventario\n3. Buscar producto\n4. Actualizar cantidad\n5. Eliminar producto\n6. Salir")
        opcion = input("Seleccione una opción (1-6): ").strip()
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            ver_inventario(inventario)
        elif opcion == '3':
            buscar_producto(inventario)
        elif opcion == '4':
            actualizar_cantidad(inventario)
        elif opcion == '5':
            eliminar_producto(inventario)
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == '__main__':
    menu()
