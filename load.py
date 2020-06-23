from PyQt5.QtWidgets import QMainWindow, QFileDialog, QFileDialog
from PyQt5.QtCore import QFile

import numpy as np

class FileOperation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_opened = 0
        self.data = np.zeros(0)
        self.file_name = None
        self.file_type = None
    
    def openFile(self):
        self.file_name, self.file_type = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.txt *.csv)')
        self.data = np.loadtxt(self.file_name, delimiter= ',')
        print(window.file_name, window.file_type)

    def saveFile(self):
        self.file_save = QFileDialog.getSaveFileName(self, 'Save File', './', 'Files (*.txt *.csv)')

if __name__ == '__main__':
    from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout

    app = QApplication([])
    window = FileOperation()
    window.central_widget = QWidget()

    window.button_open = QPushButton('Open', window.central_widget)
    window.button_save = QPushButton('Save', window.central_widget)

    window.button_open.clicked.connect(window.openFile)
    window.button_save.clicked.connect(window.saveFile)

    window.layout = QVBoxLayout(window.central_widget)
    window.layout.addWidget(window.button_open)
    window.layout.addWidget(window.button_save)
    window.setCentralWidget(window.central_widget)

    window.show()

    print(window.file_name, window.file_type)

    app.exit(app.exec_()) 