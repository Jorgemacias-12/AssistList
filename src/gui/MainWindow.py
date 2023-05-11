from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

from src.utils.MessageBox import message_box
from src.utils.data import generate_data

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        loadUi("src/gui/MainWindow.ui", self)

        self.btn_init.clicked.connect(self.btn_init_on_click)

        username_image = QPixmap("resources/username.png")
        self.lbl_img_username.setPixmap(username_image)

    def btn_init_on_click(self):

        username = self.txt_username.text()
        password = self.txt_password.text()

        if username == "" and password == "":
            message_box("¡Atención!", "Por favor introduzca sus datos para iniciar sesión", "warning")
            return

        if username == "":
            message_box("¡Atención!", "El campo de usuario se encuentra vacío", "warning")
            return

        if password == "":
            message_box("¡Atención!", "El campo de contraseña se encuentra vacío", "warning")
            return
            
        message_box("Información", f"{username}/{password}", "info")

        generate_data()