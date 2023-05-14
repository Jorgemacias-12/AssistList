from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from datetime import datetime

import os
import logging
import subprocess
import platform

class BaseWindow(QMainWindow):
    
    LOGGER_FOLDER_NAME = f"com.jamr.assistList/logs/{datetime.now().strftime('%B')}"

    def __init__(self, ui_path):

        super().__init__()

        loadUi(ui_path, self)

        appdata_path = os.getenv("APPDATA")

        logger_folder_path = os.path.join(appdata_path, self.LOGGER_FOLDER_NAME)

        if not os.path.exists(logger_folder_path):
            os.makedirs(logger_folder_path)

        log_filename = os.path.join(
            logger_folder_path, f"{datetime.today().strftime('%d-%m-%Y')}.log")

        logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s: %(message)s')

        self.logger = logging.getLogger(__name__)

        self.initial_log()

    def initial_log(self):
        
        username = os.getlogin()
        processor_name = subprocess.check_output(
            ["wmic", "cpu", "get", "name"]).decode().strip().split("\n")[1]
        architecture = platform.architecture()[0]
        os_version = platform.version()
        operating_system = platform.system()

        # Imprimir información del sistema en un formato ordenado
        # Solo si la clase es ChatbotWindow
        if type(self).__name__ == "MainWindow":
            self.logger.info("\n")
            self.logger.info("+{:-^60}+".format(""))
            self.logger.info("|{:^60}|".format(
                "AssistList Inicializado"))
            self.logger.info("+{:-^60}+".format(""))
            self.logger.info("|{:^60}|".format("Información del sistema"))
            self.logger.info("+{:-^60}+".format(""))
            self.logger.info("| {:<20} | {:<35} |".format(
                "Nombre de usuario", username))
            self.logger.info("| {:<20} | {:<35} |".format(
                "Procesador", processor_name))
            self.logger.info("| {:<20} | {:<35} |".format(
                "Arquitectura", architecture))
            self.logger.info("| {:<20} | {:<35} |".format(
                "Versión del SO", os_version))
            self.logger.info("| {:<20} | {:<35} |".format(
                "Sistema Operativo", operating_system))
            self.logger.info("+{:-^60}+".format(""))

        # Imprimir que frame fue inicializado
        log(self.logger, f"Inicializar frame: {type(self).__name__}")


def log(logger, message):

    logger.info("+{:-^{width}}+".format("", width=len(message) + 25))
    logger.info("| {:<20} | {:{width}} |".format(
        "Mensaje", message, width=len(message)))
    logger.info("+{:-^{width}}+".format("", width=len(message) + 25))
