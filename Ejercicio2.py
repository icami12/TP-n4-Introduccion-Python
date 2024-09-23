#Crear conjuntos de usuarios con los nombres: Marcela, David, Elvira, Juan, y Marcos; 
# y administradores con nombres Juan y Marcela.
conjuntos = {
    'usuarios': {"Marcela", "David", "Elvira", "Juan", "Marcos"},
    'admins': {"Juan", "Marcela"}
}

#Eliminar a Juan del conjunto de admins y Añadir a Marcos
conjuntos["admins"].discard("Juan")
conjuntos["admins"].add("Marcos")

#Mostrar todos los usuarios, indicando si cada uno es administrador o no
for user in conjuntos["usuarios"]:
    if(user in conjuntos["admins"]):
        print(f'{user} ES admin')
    else:
        print(f'{user} NO es admin')