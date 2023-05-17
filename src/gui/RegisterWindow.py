from src.utils.logging import BaseWindow
from src.utils.css import getCSS

from PyQt5.QtWidgets import QLabel, QLineEdit
from src.utils.MessageBox import message_box
from src.models.Register import Register

class RegisterWindow(BaseWindow):

    def __init__(self):

        super().__init__("src/gui/RegisterWindow.ui")

        self.btn_register.clicked.connect(self.register) 

        # Iterar en los controles para aplicar estilos en común
        # for component in self.frm_container:
        for i in range(self.frm_container.count()):

            component = self.frm_container.itemAt(i)
            widget = component.widget()

            if isinstance(widget, QLabel):

                widget.setStyleSheet(getCSS("src/styles/form-label.css"))

            if isinstance(widget, QLineEdit):

                widget.setStyleSheet(getCSS("src/styles/input.css"))

    def register(self):

        # Obtener información
        code = self.txt_student_code.text()
        full_name = self.txt_fullname.text()
        birthdate = self.de_birthdate.date().toString("dd/MM/yyyy")
        password = self.txt_password.text()

        # Validaciones aquí
        if not code:
            message_box(
        "¡Atención!", "Por favor, ingresa el código de estudiante", "info")
            return

        if not len(code) == 9:
            message_box(
                "¡Atención!", "código de estudiante no válido", "warning")
            return

        if not full_name:
            message_box("¡Atención!", "Por favor, ingresa el nombre completo", "info")
            return

        if not birthdate:
            message_box(
            "¡Atención!", "Por favor, selecciona una fecha de nacimiento", "info")
            return

        if not password:
            message_box("¡Atención!", "Por favor, ingresa la contraseña", "info")
            return

        # Crear objeto estudiante
        student = {
            "codigo de estudiante": code,
            "nombre": full_name,
            "cumpleaños": birthdate,
            "contraseña": password
        }

        register_manager = Register(student, code)
        
        message_box("¡Exito!", "Estudiante registrado exitosamente","info")