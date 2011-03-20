from PySide.QtGui import QDialog, QLineEdit, QPushButton, QTextEdit, QErrorMessage, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QMessageBox
import os
from Project import Project

class createProject():
    def __init__(self, parent):
        
        self.parent = parent
        
        self.directory = ""      
        
        self.dialog = QDialog(parent.parent)
        
        mainLayout = QVBoxLayout()
        
        aux = QHBoxLayout()
        name = QLabel("Project Name: ")
        self.textBox = QLineEdit()
        
        aux.addWidget(name)
        aux.addWidget(self.textBox)
        aux2 = QWidget()
        aux2.setLayout(aux)
        mainLayout.addWidget(aux2)       
        
                    
        auxBox = QHBoxLayout()
        self.directoryLabel = QLabel("Directory: ")
        button = QPushButton("...")
        button.clicked.connect(self.fileChoosing)
        auxBox.addWidget(self.directoryLabel)
        auxBox.addWidget(button)
        auxWidget = QWidget()
        auxWidget.setLayout(auxBox)
        mainLayout.addWidget(auxWidget) 
        
        buttonOk = QPushButton("Create Project")
        buttonOk.clicked.connect(self.okClicked)
        mainLayout.addWidget(buttonOk)
        
        self.dialog.setLayout(mainLayout)
        self.dialog.show()
        
    def fileChoosing(self):
                
        filePicker = QFileDialog()
        self.directory = filePicker.getExistingDirectory(self.parent, "Get Directory")
        self.directoryLabel.setText("Directory: " + self.directory)            
        filePicker.destroy()
        
    def okClicked(self):
               
        if self.directory != "" and self.textBox.text() != "":
            try:
                if self.parent.parent.platform == "linux2":
                    os.mkdir(self.directory + "/"+ self.textBox.text())
                    self.parent.parent.project = Project(self.directory + "/"+ self.textBox.text(), self.textBox.text(), "linux2")
                                                
                elif self.parent.parent.platform == "win32":
                    os.mkdir(self.directory + "\\"+ self.textBox.text())
                    self.parent.parent.project = Project(self.directory + "\\"+ self.textBox.text(), self.textBox.text(), "win32")
                                                                                                    
                self.parent.parent.project.save()
                self.dialog.setVisible(False)
                
                self.parent.parent.fileMenu.saveProjectAction.setEnabled(True)
                self.parent.parent.signalMenu.addSignalAction.setEnabled(True)
                self.parent.parent.signalMenu.applyOperationAction.setEnabled(True)
                
                msg = QMessageBox(self.parent.parent)
                msg.setText("Project created")
                msg.show()
                                  
                               
            except OSError:
                msg = QErrorMessage(self.parent.parent)            
                msg.showMessage("Project already exists")
