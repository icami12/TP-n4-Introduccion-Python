#Almacenar los datos en un diccionario llamado usuario_info.
usuario_info = {
    'nombre': '',
    'edad': '',
    'direcc': '',
    'telefono': ''
}

users = {
    'user1': usuario_info.copy(),
    'user2': usuario_info.copy(),
    #'user3': usuario_info.copy()
}

#Solicitar datos: nombre, edad, dirección y teléfono.
i = 0
for user in users:
    i+=1
    print(f'Ingresar datos del usuario {i}')
    users[user]["nombre"] = (str(input("Nombre: ")))
    users[user]["edad"] = str(input("Edad: "))
    users[user]["direcc"] = str(input("Dirección: "))
    users[user]["telefono"] = str(input("Teléfono: "))

#Mostrar la información ingresada para cada usuario en formato clave-valor.
for user, info in users.items():
    print(f'\nDatos del {user}:')
    for clave, valor in info.items():
        print(f'{clave.capitalize()}: {valor}')
    
    #print(f'User {user}')
    #print(f'Nombre: {users[user]["nombre"]}')
    #print(f'Edad: {users[user]["edad"]}')
    #print(f'Dirección: {users[user]["direcc"]}')
    #print(f'Teléfono: {users[user]["telefono"]}')
