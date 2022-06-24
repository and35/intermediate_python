import math as m
# calcudora de raiz cuadradas
def run ():
    try: # 1 se intentara 
        n = input("dame tu numero para calcular su raiz cuadrada: ")
        n = float(n)
        if n < 0: # 2 crearemos un error 
            raise ValueError("no podemos calcular la raiz de un numero negativo" , "( mensaje raise)")
        print("la raiz es: ", m.sqrt(n), "( mensaje try)")

    # si colocamos el error exacto esperado (ValueError), podemos personalizar el mensaje del mismo 
    except ValueError as ev: # 3 si hay otro error se ejecutara esto 
        print("tuvimos el siguiente error: ", ev, "( mensaje exeption)") 
    finally: # 4 haya error o no se ejecutara esto
        print("pase lo que pase nosotros guardamos tu numero: ", n, " (mensaje finally)")
if __name__ == "__main__": 
    run()