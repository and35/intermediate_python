import math as m

def run ():
    d = {}
    for i in range(1, 100):
        d[i] = i**2
    print(d)
    
    # el mismo ejercicio pero ahora guardando en diccionarios 
    d={}
    print("-"*60)
    for i in range(1, 100):
        if i % 3 != 0:
            d[i] = i**2
    print(d)

    #con dicts comprenhensions
    d = {}
    print("-"*60)
    d = {i : i**2 for i in range(1,101) if i%3 != 0} 
    print(d)

    # reto 
    d = {}
    print("-"*60)
    d = {i : m.sqrt(i) for i in range(1,1001)} 
    print(d)
if __name__ == "__main__": 
    run()