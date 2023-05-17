import os
import json
import logging

from datetime import date
from src.utils.logging import log
from src.utils.MessageBox import message_box

class Assistance():

    FILENAME = "assistances.json"
    DIRECTORY = os.path.join(os.getenv("APPDATA"), "com.jamr.assistList")
    FILEPATH = os.path.join(DIRECTORY, FILENAME)

    def __init__(self, subject, user):

        self.subject = subject
        self.user = user
        
        #  Obtener el mes y día
        month = date.today().strftime("%B")
        day = str(date.today().day)

        # Construir objeto de asistencias
        data = {
            f"{self.subject}": {
                month: {
                    day: [
                        user
                    ]
                }
            }
        }
        
        # Comprobar si existe archivo
        fileExists = os.path.exists(self.FILEPATH)

        if fileExists:

            #  Comprobar si existe ya la matería dentro del archivo
            if self.subject in data:

                self.append_data(self.user)
            
        else:
            self.write_data(data)


    def append_data(self, user):

        # Obtener el diccionario del json
        json_data = self.read_data()

        #  Obtener el mes y día
        month = date.today().strftime("%B")
        day = str(date.today().day)

        #  Comprobar si existe la matería [key]
        if not self.subject in json_data:

            json_data.setdefault(self.subject, {})

        #  Si no se ha tomado asistencia en el mes
        if not month in json_data[self.subject]:

            json_data[self.subject].setdefault(month, {})

        #  Si no existe el día (no se ha registrado asistencia)
        if not day in json_data[self.subject][month]:
            
            json_data[self.subject][month].setdefault(day, [])

        if user in json_data[self.subject][month][day]: 
            message_box("¡Atención!", "Ya tienes asistencia en la matería", "warning")
            return

        assistances = json_data[self.subject][month][day]
        assistances.append(user)

        self.write_data(json_data)

    def read_data(self):

        with open(self.FILEPATH, "r", encoding='utf-8') as json_file:

            data = json.load(json_file)

        return data            

    def write_data(self, data):

        #  Escribir nuevos contenidos al archivo
        with open(self.FILEPATH, "w", encoding='utf-8') as json_file:

            json.dump(data, json_file, ensure_ascii=False)
