import suma
import suma_avanzada
import multiplicacion
import divicion
import resta

def menu():
    print("HOLA, bienvenido a la calculadora")
    print("Presiona 1 para sumar dos numeros")
    print("Presiona 2 para sumar mas de dos numeros")
    print("Presiona 3 para restar dos numeros")
    print("Presiona 4 para multiplicar dos numeros")
    print("Presiona 5 para dividir dos numeros")
    print("Presiona 6 para salir")
    opcion=int(input("Presiona el numero"))
    if opcion == 1:
        a= float(input("Ingresa el primer numero"))
        b= float(input("Ingresa el segundo numero"))
        print(f"El resultado es: {suma.suma(a,b)}")
    elif opcion ==2:
        n = int(input("Ingrese la cantidad de números a sumar: "))
        numeros = []
        for i in range(n):
            num = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(num)
        print(f"Resultado: {suma_avanzada.suma_avanzada(numeros)}")
    elif opcion==3:
        a= float(input("Ingresa el primer numero"))
        b= float(input("Ingresa el segundo numero"))
        print(f"El resultado es: { resta.resta(a,b)}")
    elif opcion==4:
        a= float(input("Ingresa el primer numero"))
        b= float(input("Ingresa el segundo numero"))
        print(f"El resultado es: {multiplicacion.multiplicacion(a,b)}")
    elif opcion==5:
        a= float(input("Ingresa el primer numero"))
        b= float(input("Ingresa el segundo numero"))
        print(f"El resultadoes: {divicion.dividir(a,b)}")
    elif opcion ==6:
        print ("saliendo")
    else :
        pirnt("Por favor ingresa un valor valido")
menu()