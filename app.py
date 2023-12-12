import sys
from typing import Self

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow
)

from qdarktheme import load_stylesheet

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        
        base = QWidget()
        layout = QVBoxLayout()

        font = QFont()
        font.setPixelSize(90)
        base.setFont(font)
                
        button_paciente = QPushButton("PACIENTE")
        button_medico = QPushButton("MÉDICO")
        msg_opcao = QLabel("ESCOLHA UMA OPÇÃO", 
        alignment=Qt.AlignHCenter)

        
        
        
        
        layout.addWidget(msg_opcao)
        layout.addWidget(button_paciente)
        layout.addWidget(button_medico)

        base.setLayout(layout)
        self.setCentralWidget(base)
        

    

if __name__ == "__main__":
    app = QApplication()
    # setando dark theme
    app.setStyleSheet(load_stylesheet())

    janela = MyWindow()
    janela.resize(800, 600)
    janela.show()

    sys.exit(app.exec())