from PySide.QtGui import QDialog, QLineEdit, QPushButton, QTextEdit, QErrorMessage, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QMessageBox
import os

class addSignal():
    def __init__(self, parent):
        
        dialog = QDialog(parent.parent)
        
        mainLayout = QVBoxLayout()
        
        aux = QHBoxLayout()
        name = QLabel("Signal Name: ")
        nameBox = QLineEdit()
        aux.addWidget(name)
        aux.addWidget(nameBox)
        aux2 = QWidget()
        aux2.setLayout(aux)
        mainLayout.addWidget(aux2)
        
        def fileChoosing():
            global fileName
            
            filePicker = QFileDialog()
            fileName = filePicker.getOpenFileName(parent, 'Select File')[0]
            filePicker.destroy() 
            fileLabel.setText("File: " + fileName)            
            filePicker.destroy()
        
        def addSignalClicked():
            global directory
            
            if fileName != "" and nameBox.text() != "":
                parent.parent.project.addSignal(nameBox.text(), fileName, commentaryBox.toPlainText())
                dialog.setVisible(False)
                label = parent.parent.project.signalList[-1][0].getImage()
                
                if parent.parent.mainWidget.columnCount() == 0: parent.parent.mainWidget.setColumnCount(1)
                
                parent.parent.mainWidget.setRowCount(parent.parent.mainWidget.rowCount() + 1)
                
                parent.parent.mainWidget.setCellWidget(len(parent.parent.project.signalList)-1,0,label)
                parent.parent.mainWidget.resizeColumnsToContents()
                parent.parent.mainWidget.resizeRowsToContents()
                                
                msg = QMessageBox(parent.parent)
                msg.setText("Signal added")
                msg.show()
                
                                       
        auxBox = QHBoxLayout()
        fileLabel = QLabel("File: ")
        button = QPushButton("...")
        button.clicked.connect(fileChoosing)
        auxBox.addWidget(fileLabel)
        auxBox.addWidget(button)
        auxWidget = QWidget()
        auxWidget.setLayout(auxBox)
        mainLayout.addWidget(auxWidget)
        
        auxBox = QHBoxLayout()
        commentaryLabel = QLabel("Commentary: ")
        commentaryBox = QTextEdit()
        auxBox.addWidget(commentaryLabel)
        auxBox.addWidget(commentaryBox)
        auxWidget = QWidget()
        auxWidget.setLayout(auxBox)
        mainLayout.addWidget(auxWidget)
        
        
        buttonOk = QPushButton("Add Signal")
        buttonOk.clicked.connect(addSignalClicked)
        mainLayout.addWidget(buttonOk)
        
        dialog.setLayout(mainLayout)
        dialog.show()  
        
