from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt

from src.utils.MessageBox import message_box
from src.utils.data import subjects
from src.utils.logging import BaseWindow, log
from utils.css import getCSS

class SubjectSelection(BaseWindow):

    user = None

    def __init__(self, user):

        # Cargar la interfaz
        super().__init__("src/gui/SubjectSelection.ui")

        # Obtener el usuario
        self.user = user

        cucosta_image = QPixmap("resources/cucosta.png")

        self.lbl_cuc_logo.setPixmap(cucosta_image)

        self.vertical_layout = self.frm_subjects

        for index, subject in subjects.items():
            
            container = QHBoxLayout()
            lbl_subject = QLabel(subject.capitalize())
            btn_subject = QPushButton(subject.capitalize())

            lbl_subject.setStyleSheet(getCSS("src/styles/label.css"))
            btn_subject.setStyleSheet(getCSS("src/styles/button.css"))
            btn_subject.setCursor(Qt.PointingHandCursor)

            btn_subject.clicked.connect(lambda state, value=subject: self.handle_subject_selected(value))

            container.addWidget(lbl_subject)
            container.addWidget(btn_subject)

            self.vertical_layout.addLayout(container)

        pass

    def handle_subject_selected(self, subject):

        log(self.logger, f"Recibido en evento: {subject}")

        message_box("¡Atención!", f"{subject}", "info")

