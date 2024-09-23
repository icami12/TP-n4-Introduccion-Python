#Implementar un programa que valide la entrada de un número entero y verifique su presencia en una lista.

listaEnteros = list(range(9))

#Repetir solicitud de igrese un número entero del 0 al 9 mientras el número ingresado no esté en el rango de la lista
#Notificar al usuario si el número está o no en la lista.

while True:
    varPorTeclado = int(input("Ingresar un numero del 0 al 9 : "))
    if(varPorTeclado in listaEnteros):
        print(f'El numero {varPorTeclado} SI está en la lista')
        break
    else:
        print(f'El numero {varPorTeclado} NO está en la lista')
    