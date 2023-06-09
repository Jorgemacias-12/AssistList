import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit

from src.utils.MessageBox import message_box
from src.utils.data import get_data
from src.utils.logging import BaseWindow, log

from src.gui.SubjectSelection import SubjectSelection
from src.gui.RegisterWindow import RegisterWindow

class MainWindow(BaseWindow):

    CHB_CHECKED = 2

    user_data = get_data()

    subject_selector_window = None
    register_window = None

    def __init__(self):

        super().__init__("src/gui/MainWindow.ui")

        self.btn_init.clicked.connect(self.btn_init_on_click)

        username_image = QPixmap("resources/username.png")
        self.lbl_img_username.setPixmap(username_image)

        self.chb_password.stateChanged.connect(self.show_password)
        self.btn_register.clicked.connect(self.handle_register)

    def show_password(self, state):

        if state == self.CHB_CHECKED:
            self.chb_password.setText("Esconder contraseña")
            self.txt_password.setEchoMode(QLineEdit.Normal)
        else:
            self.chb_password.setText("Mostrar contraseña")
            self.txt_password.setEchoMode(QLineEdit.Password)

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
            

        user = None

        # obtener el usuario 
        try:
            user = self.user_data[username] 
        except KeyError as error:
            
            message_box("¡Atención!", "El nombre de usuario no existe o no es válido", "info")
            
            log(self.logger, error.__str__())

            return

        log(self.logger, f"Se ha invocado btn_init con user {user}")


        # Autenticación e invocar el siguiente frame

        # Obviando la autenticación del nombre de usuario
        # Solo se necesita comprobar la contraseña
        log(self.logger, f"Propiedades del usuario: {user}")

        if password != user["contraseña"]:
            
            message_box("¡Error!", "Contraseña o nombre de usuario no coinciden", "warning")

        if password == user["contraseña"]:

            # Invocar al frame aquí
            self.subject_selector = SubjectSelection(user)
            self.subject_selector.show()

            self.hide()

    def handle_register(self):

        self.hide()

        self.register_window = RegisterWindow()
        self.register_window.show()
