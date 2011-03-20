from PySide.QtGui import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QScrollArea, QListWidget
from util.Signal import Signal

class SideBar(QScrollArea):
    
    def __init__(self):
    
        QScrollArea.__init__(self)
        self.mainWidget = QListWidget()
        self.setWidget(self.mainWidget)
        self.setWidgetResizable(True)        
                
        self.setFixedWidth(200)
        
        self.setTitle()      
                   
                
    def setProperties(self, signal):
    
        self.mainWidget.clear()
        self.setTitle()
        
        
        for x in signal.properties:
            self.mainWidget.addItem("  " + x[0] + ": " + x[1])    
        
    def setTitle(self):
        self.mainWidget.addItem("Signal Properties")
        
         
