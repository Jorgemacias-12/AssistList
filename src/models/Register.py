import os
import json
import logging

from datetime import date

from src.utils.MessageBox import message_box


class Register():

    FILENAME = "users.json"
    DIRECTORY = os.path.join(os.getenv('APPDATA'), 'com.jamr.assistList')
    FILEPATH = os.path.join(DIRECTORY, FILENAME)

    def __init__(self, student, student_code):

        # Obtener mes y día
        month = date.today().strftime("%B")
        day = str(date.today().day)

        # Cargar información de los usuari9os 
        users = self.read_data()

        if student_code in users:
            
            message_box("¡Atención!", "Usuario ya existente", "warning")
            return

        users.setdefault(student_code, student)

        self.write_data(users)

    def read_data(self):

        with open(self.FILEPATH, "r", encoding='utf-8') as json_file:

            data = json.load(json_file)

        return data

    def write_data(self, data):

        with open(self.FILEPATH, "w", encoding='utf-8') as json_file:

            json.dump(data, json_file, ensure_ascii=False)