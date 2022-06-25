from pyfiglet import Figlet
from termcolor import colored, cprint
import os 
import json
import random
import time


p_red = lambda x: cprint(x, "red") # 'on_yellow', attrs=['bold']
p_green = lambda x: cprint(x, "green")
p_blue = lambda x: cprint(x, "blue")
p_orange = lambda x: cprint(x, "yellow")
p_title = lambda x: cprint(x, "green", attrs=['bold'])
p_sub_red = lambda x: cprint(x, "white", "on_red", attrs=['bold', "underline"])

# https://1lineart.kulaone.com/#/
b_0 = """
   ______
   |    |
   |  
   |  
  / \  
"""
b_1 = """
   ______
   |    |
   |  (̾●̮̮̃̾•̃̾)
   |  
  / \  
"""
b_2 = """
   ______
   |    |
   |  (̾●̮̮̃̾•̃̾)
   |    |
  / \  
"""
b_4 = """
   ______
   |    |
   |  (̾●̮̮̃̾•̃̾)
   |  --|--
  / \  
"""
b_3 = """
   ______
   |    |
   |  (̾●̮̮̃̾•̃̾)
   |  --|
  / \  
"""
b_5 = """
   ______
   |    |
   |  (- ̮̮̃-̃)
   |  --|--
  / \  / \    Has muerto!!!
"""
body = [b_0, b_1 ,b_2, b_3, b_4, b_5]



def check_input():
   # input open 
    true_input = False
    while true_input == False: 
      shot = input("ingresa una letra: ")
      if len(shot) != 1:
        print("solo se permite una letra de entrada!") 
      elif not shot.isalpha():
        print("solo se permiten letras de entrada! ")
      else: 
        true_input = True
        return shot

def show_function(advance, lifes, score):
    if lifes > 0:
        print(body[5-lifes])
    else: 
       p_red(body[5-lifes])
    concat_advance = ""
    for l in advance:
        concat_advance += l
        concat_advance += " "
    p_orange(concat_advance)
    
    p_green("vidas: " + lifes * "♡")
    
    p_blue("puntuaje de partida: " + str(sum(score)))

def tablero(word):
  l_word = list(word)
  lifes = 5
  size = len(l_word)
  score = []
  for i in range(size):
    score.append(0)
  advance = list("_"*size)
  show_function(advance, lifes, score)
  p_blue("adivina la palabra oculta, tiene " + str(size) + " letras")
  while True:
    
    shot = check_input() # input check function 
    if shot in l_word:
      for i_, lt in enumerate(l_word):
        if lt == shot:
          advance[i_] = shot
          score[i_] = 1
    else:
      lifes -= 1
    os.system("clear")
    show_function(advance, lifes, score)
    

    if lifes == 0:
      p_orange("la palabra era:" + str(word))
      time.sleep(3.5)

      break
    if sum(score) == size:
        f = Figlet(font='standard')
        p_orange(f.renderText('Has ganado!'))
        time.sleep(3.5)
        break
  return sum(score) + lifes - 2 # global score  
def load_dict_words():
    # Opening JSON file
    with open("./data/dict_of_words.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # ajustamos valores 
    levels = []
    data_dict= {}
    for key, value in data.items():
        data_dict[int(key)] = list(value)
        levels.append(key)
    return data_dict, levels

def game ():
    global_score = 0
    while True:
        data_dict, levels = load_dict_words()

        # banner del juego
        f = Figlet(font='standard') #slant, banner3-D, isometric2
        p_title(f.renderText('juego del ahorcado'))
        p_sub_red("by Andres Gutierrez Castillo. Mex. 2022")
        
        #choose a level
        p_blue("puntuaje total: "+str(global_score))
        print("tenemos palabras con diferentes numero de letras para que puedas escoger, entre mas letras \n tenga una palabra mas dificl te sera encontrarla.")
        while True:
            print("\n niveles disponibles: ", levels)
            n_level = input ("escoge la dificultad escribiendo un numero de la lista de arriba: ")
            if n_level in levels:
                break
            else: 
                p_red("debes escoger algun numero de la lista, intenta de nuevo")
        palabras = data_dict[int(n_level)]
        
        word = random.choice(palabras)
        score = tablero(word)
        global_score += score
def run (): 
    game()
    """data_dict, levels = load_dict_words()
    for key, value in data_dict.items():
        print(type(value))"""

if __name__ == "__main__": 
    run()