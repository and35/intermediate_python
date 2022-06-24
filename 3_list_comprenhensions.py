def run ():
    # forma normal 
    lista = []
    for a in range(1, 101):
        a = a**2
        if a % 3 != 0:
            lista.append(a)
    print(lista)
    
    print("-"*60)
    # con list comprehensions
    lista2 = [a**2 for a in range(1, 101) if a % 3 != 0]
    print(lista2)

    print("-"*60)
    # ejercicio de la clase 
    lista3 = [a for a in range(1, 10000) if a % 4 == 0 and a % 6 == 0 and a % 9 == 0]
    print(lista3)
if __name__ == "__main__": 
    run()