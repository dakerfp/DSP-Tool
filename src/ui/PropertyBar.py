from PySide.QtGui import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QScrollArea, QListWidget

class PropertyBar(QScrollArea):
    def __init__(self, parent):
    
        QScrollArea.__init__(self)
        self.parent = parent
        self.mainWidget = QListWidget()
        self.setWidget(self.mainWidget)
        self.setWidgetResizable(True)        
                
        self.setFixedHeight(130)
        
        self.setTitle()      
                   
                
    def setProperties(self):
    
        self.mainWidget.clear()
        self.setTitle() 
        
        if self.parent:
            for x in self.parent.project.experimentProperties:
                self.mainWidget.addItem("  " + x[0] + ": " + x[1])    
        
    def setTitle(self):
        self.mainWidget.addItem("Experiment Properties")
    
 
