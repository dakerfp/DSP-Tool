import numpy as np
import os
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PySide.QtGui import QLabel, QPixmap
from matplotlib.figure import Figure

class Signal(object):
    '''
    '''
    def __init__(self, name, path, commentary, project, arrayNumPy = None):
        
        object.__init__(self)
        
        self.name = name
        self.fileName = path
        self.commentary = commentary
        if not os.access(project.path + "/TempSignals/", os.EX_OK): os.mkdir(project.path + "/TempSignals/")
        self.fileImage = project.path + "/TempSignals/" + name
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
        axes.plot(self.signal_read())
                 
        canvas = FigureCanvas(figure)
        
        figure.set_figwidth(6)
        figure.set_figheight(2)

        figure.savefig(self.fileImage)
        
        fig = QLabel()
        fig.setPixmap(QPixmap(self.fileImage))
        fig.setFixedSize(600, 200)
        
        return fig
        
