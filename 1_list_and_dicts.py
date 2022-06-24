"""buenas practicas es:
    - crear una funcion principal 
    - creamos un entry point, que inice la funcion con el codigo deseado. 
"""
def run ():
    l_normal =[1,"hola",True]
    d_normal = {"nombre": "andres", "apellido": "gutierrez"}

    super_list = [
        {"nombre": "elon", "apellido": "musk"},
        {"nombre": "marie", "apellido": "curie"}
    ]
    super_dict={
        "nombre": ["elon", "marie"],
        "pais": ["USA", "polonia"],
    }
    for key, value in super_dict.items():
        print(key + "----"+ str(value))
    # pass #si no tiene nada ponemos esta linea 
if __name__ == "__main__": # entry point 
    run()