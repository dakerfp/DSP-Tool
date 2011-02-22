from PySide.QtGui import QErrorMessage, QFileDialog, QMessageBox
import os, pickle
from Project import Project

class openProject():
    def __init__(self, parent):
        
        try:
            filePicker = QFileDialog()
            fileName = filePicker.getOpenFileName(parent, "Open File", "DSPToolProjects (*.dsp)")
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
         
            
        except:
            #tratar melhor
            msg = QErrorMessage(parent.parent)            
            msg.showMessage("Invalid File")
