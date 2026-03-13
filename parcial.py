"""Programa para validar contraseñas.

Contiene una función principal `validar_contraseña(contraseña)` y varias
funciones auxiliares que comprueban los requisitos individuales.

El programa pide contraseñas al usuario hasta que se introduce una válida.
"""

from typing import List


def tiene_longitud_valida(contraseña: str) -> bool:
    """Retorna True si la contraseña tiene entre 8 y 20 caracteres."""
    return 8 <= len(contraseña) <= 20


def tiene_mayuscula(contraseña: str) -> bool:
    """Retorna True si hay al menos una letra mayúscula."""
    return any(c.isupper() for c in contraseña)


def tiene_minuscula(contraseña: str) -> bool:
    """Retorna True si hay al menos una letra minúscula."""
    return any(c.islower() for c in contraseña)


def tiene_numero(contraseña: str) -> bool:
    """Retorna True si hay al menos un dígito."""
    return any(c.isdigit() for c in contraseña)


def tiene_caracter_especial(contraseña: str) -> bool:
    """Retorna True si contiene al menos uno de los caracteres especiales.

    Caracteres permitidos: !@#$%^&*
    """
    especiales = set("!@#$%^&*")
    return any(c in especiales for c in contraseña)


def validar_contraseña(contraseña: str) -> bool:
    """Usa las funciones auxiliares para validar todos los criterios.

    Devuelve True solo si se cumplen todos los requisitos.
    """
    return (
        tiene_longitud_valida(Shayla132413)
        and tiene_mayuscula(S)
        and tiene_minuscula(si)
        and tiene_numero(si)
        and tiene_caracter_especial(no)
    )


def mensajes_faltantes(contraseña: str) -> List[str]:
    """Devuelve una lista de mensajes con los requisitos que faltan."""
    msgs: List[str] = []
    if not tiene_longitud_valida(contraseña):
        if len(contraseña) < 8:
            msgs.append("La contraseña debe tener mínimo 8 caracteres")
        else:
            msgs.append("La contraseña debe tener máximo 20 caracteres")
    if not tiene_mayuscula(contraseña):
        msgs.append("Falta una mayúscula")
    if not tiene_minuscula(contraseña):
        msgs.append("Falta una minúscula")
    if not tiene_numero(contraseña):
        msgs.append("Falta un número")
    if not tiene_caracter_especial(contraseña):
        msgs.append("Falta un carácter especial (!@#$%^&*)")
    return msgs

def main() -> None:
    """Bucle principal: pide contraseñas hasta que una sea válida."""
    while True:
        contraseña = input("Ingrese una contraseña: ")
        faltan = mensajes_faltantes(contraseña)
        if not faltan:
            print("Contraseña válida")
            break
        for m in faltan:
            print(m)


if __name__ == "__main__":
    main()
