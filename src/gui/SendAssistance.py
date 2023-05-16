from PyQt5.QtWidgets import QLabel

from src.utils.logging import BaseWindow, log
from src.utils.css import getCSS
from src.models.Assistance import Assistance
from src.utils.MessageBox import message_box

class SendAssistance(BaseWindow):

    subject_selection_window = None
    
    user = None

    def __init__(self, user, subject):
        
        super().__init__("src/gui/SendAssistance.ui")

        self.user = user
        self.subject = subject

        log(self.logger, f"{self.user},{user}")

        #  Mostrar la matería seleccionada
        self.lbl_selected_subject.setText(f"Materia seleccionada: {self.subject}")

        self.btn_exit.clicked.connect(self.handle_exit)
        self.btn_register_assistance.clicked.connect(self.handle_save_assistance)

        for index, user_info in self.user.items():
            
            if index == "contraseña": 
                continue
                
            lbl_user_info = QLabel(f"{index.title()}: {user_info}")

            lbl_user_info.setStyleSheet(getCSS("src/styles/label.css"))

            self.vrm_user_info.addWidget(lbl_user_info)

    def handle_exit(self):
        
        self.hide()

        from src.gui.SubjectSelection import SubjectSelection

        self.subject_selection_window = SubjectSelection(self.user)
        self.subject_selection_window.show()

        log(self.logger, f"Se ha invocado {__name__}")

    def handle_save_assistance(self):
        
        message_box("¡Info!", "Se ha registrado la asistencia exitosamente", "info")

        assistance_manager = Assistance(self.subject, self.user)
