from thompson import *


def conversion(cadena):
    cadena2 = ""
    operadores_concatenacion = [")", "*", "+", "?"]
    for c in range(len(cadena)):
        cadena2 += cadena[c]    
        if c < len(cadena)-1:
        
            if cadena[c] in operadores_concatenacion and verificador(cadena[c+1]):
                cadena2 += "ß"
            elif verificador(cadena[c]) and cadena[c+1] == "(":
                print(c)
                cadena2 += "ß"

            elif verificador(cadena[c]) and verificador(cadena[c+1]):
                cadena2 += "ß"

            elif cadena[c]== ")" and cadena[c+1]=="(":
                cadena2 += "ß"

            elif cadena[c] =="+" and cadena[c+1] == "(":
                cadena2 += "ß"
            
            elif cadena[c] =="*" and cadena[c+1] == "(":
                cadena2 += "ß"

            elif cadena[c] =="?" and cadena[c+1] == "(":
                cadena2 += "ß"

    return cadena2


def verificador(caracter):
    operadores = ['*', '+','?', 'ß', "|", "(", ")"]
    return caracter not in operadores


bandera = True
while bandera:
    parentesis_abiertos = 0
    parentesis_cerrados = 0
    ex = input("Ingrese la expresion deseada --> ")
    for string in ex:
        if string == "(":
            parentesis_abiertos = parentesis_abiertos +1

        elif string == ")":
            parentesis_cerrados = parentesis_cerrados+1


    if parentesis_abiertos == parentesis_cerrados:
        bandera = False
    else:
        print("La cantidad de parentesis abietos no es la misma que los cerrados")



afn = None
afd = None
alpha = "abcdefghijklmnopqrstuvwxyz0123456789E"
operadores = "*|+?()"

print("  ------------------------------ ")
print("           Menu                  ")
print("  ------------------------------ ")
print("")



while True:

    print("1. AFN - Algoritmo de Thompson")
    print("2. Salir")

    opcion = input("Elige una opcion del menu: ")
    
    c = conversion(ex)
    print(c)


    if opcion == "1":
        a = Thompson(c)
        afn = a.compilar()
        a.graficar()
    elif opcion == "2":
        print("Listoo")
        break

