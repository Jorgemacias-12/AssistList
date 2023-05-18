from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt

from src.gui.SendAssistance import SendAssistance
from src.gui.AssistanceViewer import AssistanceViewer

from src.utils.MessageBox import message_box
from src.utils.data import subjects
from src.utils.logging import BaseWindow, log
from src.utils.css import getCSS


class SubjectSelection(BaseWindow):

    send_assistance_window = None    
    login_window = None
    assistance_viewer_window = None

    def __init__(self, user):

        # Cargar la interfaz
        super().__init__("src/gui/SubjectSelection.ui")

        # Guardar la información del usuario
        self.user = user

        cucosta_image = QPixmap("resources/cucosta.png")

        self.lbl_cuc_logo.setPixmap(cucosta_image)

        self.vertical_layout = self.frm_subjects

        self.lbl_student_name.setText(f"Estudiante: {user['nombre']}")

        self.btn_log_off.clicked.connect(self.close_session)

        self.btn_assistance_viewer.clicked.connect(self.handle_assistance_viewer)

        for index, subject in subjects.items():

            container = QHBoxLayout()
            lbl_subject = QLabel(subject.capitalize())
            btn_subject = QPushButton("Seleccionar")

            lbl_subject.setStyleSheet(getCSS("src/styles/label.css"))
            btn_subject.setStyleSheet(getCSS("src/styles/button.css"))
            btn_subject.setCursor(Qt.PointingHandCursor)

            btn_subject.clicked.connect(
                lambda state, value=subject: self.handle_subject_selected(value))

            container.addWidget(lbl_subject)
            container.addWidget(btn_subject)

            self.vertical_layout.addLayout(container)

    def handle_subject_selected(self, subject):
        
        self.send_assistance_window = SendAssistance(self.user, subject)
        self.send_assistance_window.show()

        self.hide()

    def handle_assistance_viewer(self):

        self.hide()

        self.assistance_viewer_window = AssistanceViewer()
        self.assistance_viewer_window.show()

    def close_session(self):

        from src.gui.MainWindow import MainWindow

        self.hide()

        self.login_window = MainWindow()
        self.login_window.show()