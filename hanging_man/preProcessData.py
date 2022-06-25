import re
import csv

# "how to split a text in words"
def split_words():
  with open("./data/data.txt", "r", encoding="utf-8") as f: # dir of the paragraph with the text to extract the words
    for line in f:
      words = line.split(" ")
  print(words)
  return words 
# i clear words with accent i searched "how to change a character for another in python "
def clear_accented_words(data):
  cleaned_data = []
  for word in data:
    new_word = word.maketrans('áéíóú', 'aeiou')
    c_word = word.translate(new_word)
    cleaned_data.append(c_word)
  print(cleaned_data)
  return cleaned_data

# i searched "Keep Only Letters From a String in Python"
def get_just_letters(data):
  cleaned_data = []
  for word in data:
    if "ñ" in word: # also i discard words with "ñ" i searched "Check if String Contains Substring in Python"
      continue
    else:
      c_word = re.sub(r'[^a-zA-Z]', '', word) # regularExpresions.sub(simbolsToDetect, simbolToChange, data)
      cleaned_data.append(c_word)
  print(cleaned_data)
  return cleaned_data

# clean uppercase and keep only lowercase i searche "how to change uppercase to lowercase in python"
def clear_uppercase(data):
  cleaned_data = []
  for word in data:
    c_word = word.lower()
    cleaned_data.append(c_word)
  print(cleaned_data)
  print(len(cleaned_data))

  return cleaned_data
# clear word with less than 4 words
def clear_short_words(data):
  cleaned_data = []
  for word in data:
    if len(word) <= 4:
      continue
    else:
      cleaned_data.append(word)
  print(cleaned_data)
  print(len(cleaned_data))

  return cleaned_data
cleaned_data = clear_short_words(clear_uppercase(get_just_letters(clear_accented_words(split_words()))))
# maybe could be better search "how to claer text with python"

#---------------------------------------------------------------

# lets analyse the data to get insights 
def count_words(data):
  info_words = {}
  level_words = {}
  words_sizes=[]
  for word in data:
    size = len(word)
    words_sizes.append(size)

  n_types = list(set(words_sizes))
  for i in n_types:
    info_words["words with "+str(i)+" letters"]= words_sizes.count(i)

  for ty in n_types:
    lis = []
    for w in data:
      if len(w) == ty:
        lis.append(w)
        level_words[len(w)] = lis

  return info_words, level_words

info_words, level_words = count_words(cleaned_data)

for key, value in info_words.items():
  print(key + "----"+ str(value))
for key, value in level_words.items():
  print(str(key) + "----"+ str(value))

# i searched "Python Dictionary to CSV"
import json
with open("./data/dict_of_words.json", "w", encoding="utf-8") as f: 
  json.dump(level_words, f)
        