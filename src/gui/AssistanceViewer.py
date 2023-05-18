
from src.utils.logging import BaseWindow

import os
import json
import calendar

from src.utils.data import subjects
from PyQt5.QtWidgets import QComboBox, QTableWidgetItem
from src.utils.css import getCSS
from src.utils.logging import log

FILENAME = "assistances.json"
DIRECTORY = os.path.join(os.getenv('APPDATA'), 'com.jamr.assistList')
FILEPATH = os.path.join(DIRECTORY, FILENAME)


class AssistanceViewer(BaseWindow):

    json_data = None

    COLUMN_SIZE = 200

    COLUMNS = 3

    month = None
    subject = None

    def __init__(self):

        super().__init__("src/gui/AssistanceViewer.ui")

        self.init_components()

        self.read_assistance()

        # self.insert_data()
        self.update_subject()
        self.update_month()
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

        self.lbl_error.hide()

    def update_assistances(self):

        try:

            month_data = self.json_data[self.subject][self.month]

            for column in range(self.COLUMNS):

                print(column)

                for row in range(len(month_data.keys())):

                    item = QTableWidgetItem("Joder")

                    self.tbl_assistances.setItem(row, column, item)
                # for row, day in month_data.items():
                    
                    # print(row, day)

                    # item = QTableWidgetItem(day)

                    # self.lbl_assistances.setItem(int(row), column, item)

        except Exception as ex:

            log(self.logger, f"No hay información disponible {ex}")

            self.lbl_error.setText(
                f"No hay registro de asistencias en el mes:  {ex}")

            self.lbl_error.show()

        # for i in range(len(self.json_data[self.subject][self.month]))

        pass

    def read_assistance(self):

        with open(FILEPATH, "r", encoding='utf-8') as json_file:

            self.json_data = json.load(json_file)

    def update_subject(self):

        self.subject = self.cmb_subject.currentText()
        self.update_assistances()

    def update_month(self):

        self.month = self.cmb_month.currentText()[0:3]
        self.update_assistances()

    # def insert_data(self):

    #     for row, item in enumerate(self.json_data):

    #         print(f"{row} - {item}")

    #     pass
