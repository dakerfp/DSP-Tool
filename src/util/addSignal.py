from PySide.QtGui import QDialog, QLineEdit, QPushButton
from PySide.QtGui import QTextEdit, QErrorMessage, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QMessageBox
import os

class addSignal():
    def __init__(self, parent):
        
        self.parent = parent
        
        self.dialog = QDialog(self.parent.parent)
        
        mainLayout = QVBoxLayout()
        
        aux = QHBoxLayout()
        name = QLabel("Signal Name: ")
        self.nameBox = QLineEdit()
        aux.addWidget(name)
        aux.addWidget(self.nameBox)
        aux2 = QWidget()
        aux2.setLayout(aux)
        mainLayout.addWidget(aux2)   
        
                                       
        auxBox = QHBoxLayout()
        self.fileLabel = QLabel("File: ")
        button = QPushButton("...")
        button.clicked.connect(self.fileChoosing)
        auxBox.addWidget(self.fileLabel)
        auxBox.addWidget(button)
        auxWidget = QWidget()
        auxWidget.setLayout(auxBox)
        mainLayout.addWidget(auxWidget)
        
        
        hBox = QHBoxLayout()
        hBox.addWidget(QLabel("Sample Rate (Hz): "))
        self.sampleRate = QLineEdit()
        self.sampleRate.setText("60")
        hBox.addWidget(self.sampleRate)
        auxW = QWidget()
        auxW.setLayout(hBox)
        mainLayout.addWidget(auxW)      
        
        
        auxBox = QHBoxLayout()
        commentaryLabel = QLabel("Commentary: ")
        self.commentaryBox = QTextEdit()
        auxBox.addWidget(commentaryLabel)
        auxBox.addWidget(self.commentaryBox)
        auxWidget = QWidget()
        auxWidget.setLayout(auxBox)
        mainLayout.addWidget(auxWidget)
        
        
        buttonOk = QPushButton("Add Signal")
        buttonOk.clicked.connect(self.addSignalClicked)
        mainLayout.addWidget(buttonOk)
        
        self.dialog.setLayout(mainLayout)
        self.dialog.show()
        
    def fileChoosing(self):
                        
            filePicker = QFileDialog()
            self.fileName = filePicker.getOpenFileName(self.parent, 'Select File')[0]
            filePicker.destroy() 
            self.fileLabel.setText("File: " + self.fileName)            
            filePicker.destroy()
        
    def addSignalClicked(self):
                
        if self.fileName != "" and self.nameBox.text() != "":
            self.parent.parent.project.addSignal(self.nameBox.text(), self.fileName, self.commentaryBox.toPlainText(), self.sampleRate.text())
            self.dialog.setVisible(False)
            label = self.parent.parent.project.signalList[-1][0].getImage()
            
            if self.parent.parent.table.columnCount() == 0: self.parent.parent.table.setColumnCount(1)
            
            self.parent.parent.table.setRowCount(self.parent.parent.table.rowCount() + 1)
            
            self.parent.parent.table.setCellWidget(len(self.parent.parent.project.signalList)-1,0,label)
            self.parent.parent.table.resizeColumnsToContents()
            self.parent.parent.table.resizeRowsToContents()
            self.parent.parent.setLabels()
                            
            msg = QMessageBox(self.parent.parent)
            msg.setText("Signal added")
            msg.show()       
    
