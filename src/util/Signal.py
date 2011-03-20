import numpy as np
import os
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PySide.QtGui import QLabel, QPixmap
from matplotlib.figure import Figure

class Signal(object):
    '''
    '''
    def __init__(self, name, path, commentary, project, sampleRate, arrayNumPy = None):
        
        object.__init__(self)
        
        self.properties = []
        self.name = name
        self.fileName = path
        self.commentary = commentary
        self.sampleRate = int(sampleRate)
        if sys.platform == "linux2":
            if not os.access(project.path + "/TempSignals/", os.EX_OK): os.mkdir(project.path + "/TempSignals/")
            self.fileImage = project.path + "/TempSignals/" + name
        elif sys.platform == "win32":
            if not os.access(project.path + "\TempSignals\\", os.F_OK): os.mkdir(project.path + "\TempSignals\\")
            self.fileImage = project.path + "\TempSignals\\" + name

        if arrayNumPy: self.writeFile(arrayNumPy, path)
          
                
    def writeFile(self, array, path):
        signalFile = open (path, "w")
        for x in array:
            signalFile.write(str(x) + "\n")
        signalFile.close()
     
     
    def signal_read(self):
        """
        """
        signal = []
        for row in open(self.fileName):
            signal.append(float(row))

        return np.array(signal)
        
    def set_Name(self):
        nameList = self.fileName.split("/")[-1].split(".")    
        self.name = ".".join(nameList[:-1]) + ".png"
        
    def getImage(self):
    
        figure = Figure()
        axes = figure.add_subplot(111)
        
        yAxes = self.signal_read()
        xAxes = [1]
                
        aux = 1
        for x in range (0, len(yAxes)-1):
            aux += 1.0/self.sampleRate
            xAxes.append(aux)
            
        
        axes.plot(xAxes, yAxes)
                 
        canvas = FigureCanvas(figure)
        
        figure.set_figwidth(6)
        figure.set_figheight(2)

        figure.savefig(self.fileImage)
        
        fig = QLabel()
        fig.setPixmap(QPixmap(self.fileImage))
        fig.setFixedSize(600, 200)
        
        return fig
        
    def addProperty (self, Name, Value):
        self.properties.append((Name,Value))
        
