from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
Icon = "Icon.png"
Title = "SisGrab Beta"

class Pantalla_Menu(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        hlay = QHBoxLayout(self)
        vlay = QVBoxLayout()
        hlay.addLayout(vlay)
        hlay.addItem(QSpacerItem(687, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.button1 = QPushButton("Ingresar al Sistema de Grabados", self)
        button2 = QPushButton("Información", self)
        button3 = QPushButton("Opciones", self)
        button4 = QPushButton("Salir", self)
        vlay.addWidget(self.button1)
        vlay.addWidget(button2)
        vlay.addWidget(button3)
        vlay.addWidget(button4)
        button4.clicked.connect(QCoreApplication.instance().quit)

class Pantalla_Prueba(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        hlay = QHBoxLayout(self)
        label = QLabel("label", self)
        hlay.addWidget(label)

class MainW(QWidget):
    def __init__(self):
        super(MainW, self).__init__()
        self.setWindowTitle(Title)
        self.setWindowIcon(QIcon(Icon))
        self.resize(600,200)
        self.pantalla_menu = Pantalla_Menu(self)
        self.pantalla_prueba = Pantalla_Prueba(self)
        self.stack = QStackedWidget(self)
        ix_pantalla_menu = self.stack.addWidget(self.pantalla_menu)
        ix_pantalla_prueba = self.stack.addWidget(self.pantalla_prueba)

        self.pantalla_menu.button1.clicked.connect(lambda: self.stack.setCurrentIndex(ix_pantalla_prueba))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainW()