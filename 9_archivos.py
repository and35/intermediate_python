def read():
    l = []
    with open("./my_files/numbers.txt", "r") as f:
        for a in f: # un archivo de texto puede ser tratado como un iterable, linea x linea 
            l.append(int(a))
    print(l)
def write():
    names=["einstein", "alan", "andrés", "marie", "jane"]
    with open("./my_files/names.txt", "w", encoding="utf-8") as f:
        for a in names:
            f.write(a + "\n")

def run ():
    write()
if __name__ == "__main__": 
    run()