def suma (a: int,b: int)->int:
    result = a+b
    print(a, "+", b, "=", result)
    return result

def multiplicacion (a: int,b: int)->int:
    result =a*b
    print(a, "*", b, "=", result)
    return result

def division (a: int,b: int)->int:
    result =a/b
    print(a, "/", b, "=", result)
    return result

def resta (a: int,b: int)->int:
    result =a-b
    print(a, "-", b, "=", result)
    return result

def main():
    a = int (input("Numero A = "))
    b = int(input("Numero B = "))
    op = input("Operacion: 1 - suma, 2 - resta, 3 - multiplicacion, 4 - division = ")

    op = int(op)

    if op == 1:
        suma(a,b)
    elif op == 2:
        resta(a,b) 
    elif op == 3:
        multiplicacion(a,b)
    elif op == 4:
        division(a,b)
    else:
        print ("operacion invalida")
main()