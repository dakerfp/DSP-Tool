from PySide.QtGui import QErrorMessage, QFileDialog, QMessageBox
import os, pickle
from Project import Project

class openProject():
    def __init__(self, parent):
        
        try:
            filePicker = QFileDialog()
            fileName = filePicker.getOpenFileName(parent, "Open File")
            
                        
            if fileName[0] != "":
                f = open (fileName[0], "r")
                parent.parent.project = pickle.load(f)
                f.close()
                filePicker.destroy()
                
                      
                parent.parent.fileMenu.saveProjectAction.setEnabled(True)
                parent.parent.signalMenu.addSignalAction.setEnabled(True)
                parent.parent.signalMenu.applyOperationAction.setEnabled(True)
                
                msg = QMessageBox(parent.parent)
                msg.setText("Project opened")
                msg.show()
                
                parent.parent.refreshTable()
                parent.parent.refreshProperties()
         
                
        except:
            #tratar melhor
            msg = QMessageBox(parent.parent)            
            msg.setText("Invalid File")
            msg.show()


