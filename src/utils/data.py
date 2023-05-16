import random
import string
import json
import os

from src.utils.generation import generate_full_name
from src.utils.generation import generate_password
from src.utils.generation import generate_birthdate

DATA_FILENAME = "users.json"
DIRECTORY = os.path.join(os.getenv("APPDATA"), "com.jamr.assistList")
FILE_PATH = os.path.join(DIRECTORY, DATA_FILENAME)



def get_data():

   if not os.path.exists(f"{FILE_PATH}"):
      generate_data()

   with open(FILE_PATH, "r", encoding="utf-8") as json_file:

      user_dictionary = json.load(json_file)

      return user_dictionary

def generate_data():
    
    user_dictionary = {}

    for _ in range(5):

      key = ''.join(random.choices(string.digits, k=9))
      name = generate_full_name()
      birthday = generate_birthdate()
      password = generate_password()
      
      user_dictionary[key] = {'codigo de estudiante': key, 'nombre': name, 'cumpleaños': birthday, 'contraseña': password}

    # Create directory if it doesn't exist
    if not os.path.exists(DIRECTORY):
       
       os.makedirs(DIRECTORY)

    # Dump dictionary in a JSON
    with open(FILE_PATH, 'w', encoding='utf-8') as json_file:
       
       json.dump(user_dictionary, json_file, ensure_ascii=False)


subjects = {
   0: "Probabilidad y estadistica",
   1: "Estructuras de datos",
   2: "Arquitectura de computadoras",
   3: "Redes de computadoras",
   4: "Liderazgo y emprendimiento",
   5: "Métodos numericos",
}