# funcion para evaluar palabras palindromas 
def run ():
    #version normal
    def palindromo1(text):
        print(text, " - ", text[::-1]) # text[::-1]= slice= [inicio:final:pasos] = retorna todo en reversa 
        return  text == text[::-1]
    palindromo1("metal")
    palindromo1("reconocer")# es una palabra palindroma 

    #version lambda 
    palindromo2 = lambda text: text == text[::-1]
    print(palindromo2("zorro"))
    print(palindromo2("oro"))
    
if __name__ == "__main__": 
    run()