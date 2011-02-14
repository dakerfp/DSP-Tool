"""
DSP-Tool

This file is part of the DSP-Tool application.

This application is free software; you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or (at
your option) any later version.

This application is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this application;  If not, see <http://www.gnu.org/licenses/>.
"""


import numpy as np
import scipy as sp
import scipy.signal as sig
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PySide.QtCore import Signal, Slot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PySide.QtGui import QMainWindow, QVBoxLayout, QMenu, QMenuBar, QFileDialog, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPixmap, QScrollArea
from Signal import DSPToolSignal
from .operations import ApplyOperation

class DSPToolFileMenu(QMenu):
    """
    """
    def __init__(self, parent=None):
        QMenu.__init__(self, "&Files")
        self.parent = parent

        newProjectAction = self.addAction(self.trUtf8("&New Project"))
        newProjectAction.triggered.connect(self.createNewProject)
        
        openProjectAction = self.addAction(self.trUtf8("&Open Project"))
        openProjectAction.triggered.connect(self.openProject)

        quitAction = self.addAction(self.trUtf8("&Quit Program"))
        quitAction.triggered.connect(self.parent.close)

    @Slot()
    def createNewProject(self):
        """
        """
                
    @Slot()
    def openProject(self):
        """
        """
        pass
    
    @Slot()
    def saveProject(self):
        """
        """
        pass


class DSPToolSignalsMenu(QMenu):
    """
    """
    def __init__(self, parent=None):
        QMenu.__init__(self, "&Signals")
        self.parent = parent
        
        addSignalAction = self.addAction(self.trUtf8("&Add Signal"))
        addSignalAction.triggered.connect(self.addSignal)
        
        applyOperationAction = self.addAction(self.trUtf8("&Apply Operation"))
        applyOperationAction.triggered.connect(self.applyOperation)    
    
    
    def applyOperation(self):
        ApplyOperation.applyOperation(self.parent)
    
    def addSignal(self):
        """
        """
        filePicker = QFileDialog()
        fileName = filePicker.getOpenFileName(self, 'Select File')
        filePicker.destroy()        
                
        if fileName:
            signal = DSPToolSignal(fileName[0])
            
            self.parent.signalsList.append(signal)
            
            figure = Figure()
            axes = figure.add_subplot(111)
            axes.plot(signal.signal_read())
                     
            canvas = FigureCanvas(figure)
            
            figure.set_figwidth(6)
            figure.set_figheight(2)

            figure.savefig(signal.name)
            
            fig = QLabel()
            fig.setPixmap(QPixmap(signal.name))
            fig.setFixedSize(600, 200)               

            
            layout = self.parent.mainLayout.addWidget(fig)
            
class DSPToolMainWindow(QMainWindow):
    """
    """

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.signalsList = []

        menuBar = QMenuBar()

        self.fileMenu = DSPToolFileMenu(self)
        menuBar.addMenu(self.fileMenu)

        self.signalMenu = DSPToolSignalsMenu(self)
        menuBar.addMenu(self.signalMenu)

        self.setMenuBar(menuBar)
        
        self.mainWidget=QWidget(self)
        
      
        
        scrollWidget = QScrollArea()
        scrollWidget.setWidget(self.mainWidget)
        scrollWidget.setWidgetResizable(True)
        
        self.setCentralWidget(scrollWidget)
        
        self.mainLayout=QVBoxLayout(self.mainWidget)
        


