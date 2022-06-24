def run ():
    # utilizando assert para corroborar si una variables es numero en una calculadora
    a = input("dame un numero a: ")   
    b = input("dame un numero b: ")    

    assert a.isnumeric() and b.isnumeric(), "debes ingresar valores numericos"
    print(a, "+ ", b, " = ", int(a)+int(b))
if __name__ == "__main__": 
    run()