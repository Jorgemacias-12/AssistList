from PyQt5.QtWidgets import QMessageBox


def message_box(title, body, icon):
    
    icon_lookup = {
        "info": QMessageBox.Information,
        "warning": QMessageBox.Warning,
        "question": QMessageBox.Question,
        "critical": QMessageBox.Critical
    }

    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(body)
    # Lookup the icon value
    msg_box.setIcon(icon_lookup.get(icon, QMessageBox.Information))
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()