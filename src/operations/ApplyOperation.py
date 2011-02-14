from PySide.QtGui import QListWidget, QListWidgetItem, QScrollArea, QMainWindow, QPushButton, QVBoxLayout, QDialog, QWidget
from os import listdir
import sys

def applyOperation(parent):
   
    window = QWidget()
    window.setParent(parent)
    window.activateWindow()
        
    operationList = QListWidget()
    
    filesList = listdir(sys.path[0] + "/operations/List/")
    
    filesList = [el for el in filesList if el.endswith(".py")]
    
    for el in filesList:
        el = ".".join(el.split(".")[:-1])
        label = QListWidgetItem()
        label.setText(el)
        operationList.addItem(label)       
    
    scrollWidget = QScrollArea()
    scrollWidget.setWidget(operationList)
    scrollWidget.setWidgetResizable(True)
    
    layout = QVBoxLayout()
    
    button = QPushButton("Ok")
    button.clicked.connect(doingTheOperation)
    
    layout.addWidget(scrollWidget)
    layout.addWidget(button)   
    
    window.setLayout(layout)
    
    window.setVisible(True)
    window.show()

def doingTheOperation():
    return None
