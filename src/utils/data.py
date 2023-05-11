import random
import string
import json
import os

from src.utils.generation import generate_full_name
from src.utils.generation import generate_password

DATA_FILENAME = "users.json"
DIRECTORY = os.path.join(os.getenv("APPDATA"), "com.jamr.assistList")
FILE_PATH = os.path.join(DIRECTORY, DATA_FILENAME)

def generate_data():
    
    user_dictionary = {}

    for _ in range(5):

      key = ''.join(random.choices(string.digits, k=9))
      name = generate_full_name()
      password = generate_password()

      user_dictionary[key] = {'nombre': name, 'contraseña': password}

    # Print generated users

    # Only for debug purposes
    # for key, user in user_dictionary.items():
    #   print(f"Clave: {key}")
    #   print(f"Nombre: {user['nombre']}")
    #   print(f"Contraseña: {user['contraseña']}")
    #   print("------------------------")

    # Create directory if it doesn't exist
    if not os.path.exists(DIRECTORY):
       
       os.makedirs(DIRECTORY)

    # Dump dictionary in a JSON
    with open(FILE_PATH, 'w', encoding='utf-8') as json_file:
       
       json.dump(user_dictionary, json_file, ensure_ascii=False)