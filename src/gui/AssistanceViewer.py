import traceback
from src.utils.logging import BaseWindow

import os
import json
import calendar

from src.utils.data import subjects
from PyQt5.QtWidgets import QComboBox, QTableWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from src.utils.css import getCSS
from src.utils.logging import log
from datetime import date

FILENAME = "assistances.json"
DIRECTORY = os.path.join(os.getenv('APPDATA'), 'com.jamr.assistList')
FILEPATH = os.path.join(DIRECTORY, FILENAME)


class AssistanceViewer(BaseWindow):

    json_data = None

    COLUMN_SIZE = 200

    COLUMNS = 3

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

        self.lbl_error.hide()

    def update_assistances(self):

        try:

            month_data = self.json_data[self.subject][self.month]

            month_data_size = len(month_data)
            day_data_size = len(month_data.items())

            total_data_size = month_data_size * day_data_size

            # Set the row and column count
            self.tbl_assistances.setRowCount(total_data_size)
            # self.tbl_assistances.setColumnCount(self.COLUMNS)

            print(month_data_size, day_data_size)

            row = 0

            for index, (key, data) in enumerate(month_data.items()):
                
                for student in data:
                    
                    row += 1
                    
                    for column in range(self.COLUMNS):
                        
                        if column == self.DAY_COLUMN:

                            self.tbl_assistances.setItem(row, column, self.create_item(key))

                        if column == self.STUDENT_CODE_COLUMN:

                            self.tbl_assistances.setItem(row, column, self.create_item(student["codigo de estudiante"]))

                        if column == self.STUDENT_FULLNAME_COLUMN:

                            self.tbl_assistances.setItem(row, column, self.create_item(student["nombre"]))


                        # print(f"{key} - {student}")

                #         self.tbl_assistances.setItem(
                #                     row, column, self.create_item(student["nombre"]))
                # # for column in range(self.COLUMNS):
                    
                #     for student in data:

                #         print(student["nombre"])

                    pass


            # for row, (key, data) in enumerate(month_data.items()):

                # for column in range(self.COLUMNS):

                    # print(column)

                # for item in data ()

            # for column in range(self.COLUMNS):

            #     for row, (key, data) in enumerate(month_data.items()):
                    
            #         for item in data:

            #             print (item)
                    
        except Exception as ex:

            log(self.logger, f"No hay información disponible {type(ex).__name__}")

            print(type(ex).__name__)

            self.lbl_error.setText(
                f"No hay registro de asistencias en el mes:  {ex}")

            traceback.print_exc()

            self.lbl_error.show()
            self.btn_close.show()

    def read_assistance(self):

        with open(FILEPATH, "r", encoding='utf-8') as json_file:

            self.json_data = json.load(json_file)

    def update_subject(self):

        self.subject = self.cmb_subject.currentText()
        self.update_assistances()

    def update_month(self):

        self.month = self.cmb_month.currentText()[0:3]
        self.update_assistances()

    def create_item(self, text):

        component = QTableWidgetItem(text)
        component.setForeground(QColor("black"))
        component.setBackground(QColor("white"))

        return component
    
    def handle_error_close(self):

        self.lbl_error.hide()
        self.btn_close.hide()
