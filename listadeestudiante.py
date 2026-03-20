estudiantes = ["Juan", "María", "Xavi","Ana", "camilo","juanes", "adriana","shayla"]
estudiantes.append("keiner")
estudiantes.append("marcos") # Agrega "marcos" al final de la lista
print(estudiantes) # ['Juan', 'María', 'Xavi', 'Ana', 'camilo', 'juanes', 'adriana', 'shayla', 'keiner', 'marcos']
print (len(estudiantes)) # 10
if "María" in estudiantes:
    print("María está en la lista de estudiantes.")
estudiantes.remove("camilo")
print(estudiantes) # ['Juan', 'María', 'Xavi', 'Ana', 'juanes', 'adriana', 'shayla', 'keiner', 'marcos']
print (len(estudiantes)) # 9 
estudiantes.append("edwin") # Agrega "edwin" al final de la lista
print(estudiantes) # ['Juan', 'María', 'Xavi', 'Ana', 'juanes', 'adriana', 'shayla', 'keiner', 'marcos', 'edwin']