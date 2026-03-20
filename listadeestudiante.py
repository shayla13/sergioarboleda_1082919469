estudiantes= ["Juan", "María", "Pedro", "Ana", "Luis" , "sergio" , "Sofia", "Diego"]
estudiantes.append("Miguel")
estudiantes.append("Lucía") # Agrega "Lucía" al final de la lista
print(estudiantes) #  ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'sergio', 'Sofia', 'Diego', 'Miguel', 'Lucía']
print (len(estudiantes)) # 10
if "Ana" in estudiantes:
    print("Ana está en la lista de estudiantes.")
    estudiantes.remove("Ana") 
print(estudiantes) # ['Juan', 'María', 'Pedro', 'Luis', 'sergio', 'Sofia', 'Diego', 'Miguel', 'Lucía']
print (len(estudiantes)) # 9
estudiantes. append("Ana") # Agrega "Ana" al final de la lista
print(estudiantes) # ['Juan', 'María', 'Pedro', 'Luis', 'sergio', 'Sofia', 'Diego', 'Miguel', 'Lucía', 'Ana']

