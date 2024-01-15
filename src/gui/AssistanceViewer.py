import traceback
from src.utils.logging import BaseWindow

import os
import json
import calendar

from src.utils.data import subjects
from PyQt5.QtWidgets import QComboBox, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from src.utils.css import getCSS
from src.utils.logging import log
from src.utils.MessageBox import message_box
from datetime import date

ASSISTANCES_FILENAME = "assistances.json"
ASSISTANCES_LOCATION_DIRECTORY = os.path.join(os.getenv('APPDATA'), 'com.jamr.assistList')
ASSISTANCES_FILEPATH = os.path.join(ASSISTANCES_LOCATION_DIRECTORY, ASSISTANCES_FILENAME)


class AssistanceViewer(BaseWindow):

    json_data = None

    COLUMN_SIZE = 200

    TABLE_COLUMNS_COUNT = 3

    DAY_COLUMN = 0
    STUDENT_CODE_COLUMN = 1
    STUDENT_FULLNAME_COLUMN = 2

    month = None
    subject = None

    def __init__(self):

        super().__init__("src/gui/AssistanceViewer.ui")

        #  use actual month
        self.month = date.today().strftime("%B")
        
        self.init_components()
        
        # Get the first subject to use it to show data
        self.subject = self.cmb_subject.currentText();

        self.read_assistance()
        
        self.update_assistances()

    def init_components(self):

        for i in range(self.frm_filter_controls.count()):

            component = self.frm_filter_controls.itemAt(i)
            widget = component.widget()

            if isinstance(widget, QComboBox):

                widget.setStyleSheet(getCSS("src/styles/combobox.css"))

        # Incrementar tamaño de las columnas
        for column in range(self.tbl_assistances.columnCount()):

            self.tbl_assistances.setColumnWidth(column, self.COLUMN_SIZE)

        for subject in subjects.values():

            self.cmb_subject.addItem(subject)

        for month in calendar.month_name[1:]:

            self.cmb_month.addItem(month)

        self.cmb_subject.currentIndexChanged.connect(self.update_subject)
        self.cmb_month.currentIndexChanged.connect(self.update_month)
        self.btn_close.clicked.connect(self.handle_error_close)

        self.tbl_assistances.setEditTriggers(QTableWidget.NoEditTriggers)
        
        self.lbl_error.hide()

    def update_assistances(self):
        
        self.tbl_assistances.setRowCount(0)

        try:
            if self.json_data is None:
                message_box("¡Error!", "El archivo de asistencias no existe", "critical")

                return
            
            # Get data from assistance.json using current subject and month
            # The subject is obtained in the constructor of this frame and
            # The same procress is used in the month.
            month_data = self.json_data[self.subject][self.month]
                                    
            # Get how many data is being loaded.
            total_data_length = sum(len(data) for data in month_data.values())
            
            # Set row and column count into the table component
            self.tbl_assistances.setColumnCount(self.TABLE_COLUMNS_COUNT)
            
            
            # Iterate through the month_data variable to get the students
            for day, students in month_data.items():
                for student in students: # get student
                    # Get current rowCount and increase it with the insertRow method
                    row_position = self.tbl_assistances.rowCount()
                    self.tbl_assistances.insertRow(row_position)
                    
                    self.tbl_assistances.setItem(row_position, 0, QTableWidgetItem(day))
                    
                    # Get values of the student
                    for col, (key, value) in enumerate(student.items()):
                        item = QTableWidgetItem(str(value))
                        self.tbl_assistances.setItem(row_position, col + 1, item) 
        except KeyError as ex: 
            
            log(self.logger, f"No hay información disponile: {type(ex).__name__}")

            self.lbl_error.setText(f"No hay información disponible en el mes: {self.month}")

            traceback.print_exc()
            
            self.lbl_error.show()
            self.btn_close.show()
            
    def read_assistance(self):
        try:
            with open(ASSISTANCES_FILEPATH, "r", encoding='utf-8') as json_file:
                self.json_data = json.load(json_file);            
        except FileNotFoundError as e:                  
            log(self.logger, f"{type(e).__name__}: {e}")
        
    def update_subject(self):

        self.subject = self.cmb_subject.currentText()
        self.update_assistances()

    def update_month(self):

        self.month = self.cmb_month.currentText()
        self.update_assistances()

    def create_item(self, text):

        component = QTableWidgetItem(text)
        component.setForeground(QColor("black"))
        component.setBackground(QColor("white"))

        return component
    
    def handle_error_close(self):

        self.lbl_error.hide()
        self.btn_close.hide()
