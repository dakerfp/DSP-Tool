from PySide.QtGui import QDialog, QLineEdit, QPushButton, QTextEdit, QErrorMessage, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QMessageBox
import os
from Project import Project

class createProject():
    def __init__(self, parent):
                
        directory = ""      
        
        dialog = QDialog(parent.parent)
        
        mainLayout = QVBoxLayout()
        
        aux = QHBoxLayout()
        name = QLabel("Project Name: ")
        textBox = QLineEdit()
        
        aux.addWidget(name)
        aux.addWidget(textBox)
        aux2 = QWidget()
        aux2.setLayout(aux)
        mainLayout.addWidget(aux2)
        
        def fileChoosing():
            global directory
            
            filePicker = QFileDialog()
            directory = filePicker.getExistingDirectory(parent, "Get Directory")
            directoryLabel.setText("Directory: " + directory)            
            filePicker.destroy()
        
        def okClicked():
            global directory
            
            if directory != "" and textBox.text() != "":
                try:
                    os.mkdir(directory + "/"+ textBox.text())
                    parent.parent.project = Project(directory + "/"+ textBox.text(), textBox.text())
                    parent.parent.project.save()
                    dialog.setVisible(False)
                    
                    parent.parent.fileMenu.saveProjectAction.setEnabled(True)
                    parent.parent.signalMenu.addSignalAction.setEnabled(True)
                    parent.parent.signalMenu.applyOperationAction.setEnabled(True)
                    
                    msg = QMessageBox(parent.parent)
                    msg.setText("Project created")
                    msg.show()
                                      
                                   
                except OSError:
                    msg = QErrorMessage(parent.parent)            
                    msg.showMessage("Project already exists")
                    
        auxBox = QHBoxLayout()
        directoryLabel = QLabel("Directory: ")
        button = QPushButton("...")
        button.clicked.connect(fileChoosing)
        auxBox.addWidget(directoryLabel)
        auxBox.addWidget(button)
        auxWidget = QWidget()
        auxWidget.setLayout(auxBox)
        mainLayout.addWidget(auxWidget) 
        
        buttonOk = QPushButton("Create Project")
        buttonOk.clicked.connect(okClicked)
        mainLayout.addWidget(buttonOk)
        
        dialog.setLayout(mainLayout)
        dialog.show() 
