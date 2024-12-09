# para referencia:

mylist = [1,2,3,4,5]
mylist.append(1) # agregar elemento al final de la lista

# como acceder a una lista o tupla por medio de iterators:
# for numero in numlist:
#     print(numero)

# como acceder a una lista o tupla por medio de indices:
# for i in range(0,len(numlist)): # range = [0,1,2,3,4]
#     print(i)

mytuple = (1,2,3,4,5)

mydict = {
    # llave: valor
    # la llave es inmutable, una lista no puede ser llave por ejemplo
    1: "1",
    "a": "2",
    (1,"a"): "3",
    2: 3,
    # la llave puede tener cualquier tipo de valor
}

# programa de calculadora:

def suma(nums: list[int]):
    result = 0
    for num in nums:
        result = result + num # otra forma: result += num
        
    print (result)
    return result

def rest(nums:list[int]):
    result= 0
    for num in nums:
        result = result - num
    
    print(result)
    return result

def main():
    print("1. to sum")
    print("2. to rest")
    option = input("option: ")
    nums = input("Nums to operate (separated by ,): ") # "1, 2, 3,4,5, 6, 7"
    numlist = nums.replace(" ", "").split(",") # list of str: ["1", "2", "3"]

    print(f"Operating the nums: {numlist}")

    nums= []
    for num in numlist:
        numero=int(num)
        nums.append(numero)

    if option == "1":
        suma(nums)
        # sum
    elif option == "2":
        rest(nums)
        # rest
    else:
        print("Invalid. Retry again")

main()