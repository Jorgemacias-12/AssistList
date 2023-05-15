from PyQt5.QtCore import QFile, QTextStream


def getCSS(file):

    file = QFile(file)

    if file.open(QFile.ReadOnly | QFile.Text):

      stream = QTextStream(file)
      css = stream.readAll()
    
    return css