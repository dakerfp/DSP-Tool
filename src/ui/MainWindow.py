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
import os
import pickle
import numpy as np
import scipy as sp
from .util import Project
import scipy.signal as sig
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from .util.addSignal import addSignal
from .util.openProject import openProject
from .util.createProject import createProject
from PySide.QtCore import Signal, Slot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PySide.QtGui import QDialog, QLineEdit, QPushButton, QTextEdit, QErrorMessage, QTableWidget, QTableWidget, QMessageBox
from PySide.QtGui import QMainWindow, QVBoxLayout, QMenu, QMenuBar, QFileDialog, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPixmap, QScrollArea


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
        
        self.saveProjectAction = self.addAction(self.trUtf8("&Save Project"))
        self.saveProjectAction.triggered.connect(self.saveProject)
        self.saveProjectAction.setEnabled(False)
        
        quitAction = self.addAction(self.trUtf8("&Quit Program"))
        quitAction.triggered.connect(self.parent.close)

    @Slot()
    def createNewProject(self):
        """
        """
        create = createProject(self)  
        
                        
    @Slot()
    def openProject(self):
        """
        """
        openP = openProject(self)
        
    
    @Slot()
    def saveProject(self):
        """
        """
        self.parent.project.save()
        
        msg = QMessageBox(self.parent)
        msg.setText("Project Saved")
        msg.show()


class DSPToolSignalsMenu(QMenu):
    """
    """
    def __init__(self, parent=None):
        QMenu.__init__(self, "&Signals")
        self.parent = parent
        
        self.addSignalAction = self.addAction(self.trUtf8("&Add Signal"))
        
        self.addSignalAction.triggered.connect(self.addSignal)
        self.addSignalAction.setEnabled(False)
        
        self.applyOperationAction = self.addAction(self.trUtf8("&Apply Operation"))
        self.applyOperationAction.triggered.connect(self.applyOperation)    
        self.applyOperationAction.setEnabled(False)
    
    def applyOperation(self):
        ApplyOperation.applyOperation(self.parent)
    
    def addSignal(self):
        """
        """
        add = addSignal(self)
        
class DSPToolMainWindow(QMainWindow):
    """
    """

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.project = None
        
        menuBar = QMenuBar()

        self.fileMenu = DSPToolFileMenu(self)
        menuBar.addMenu(self.fileMenu)

        self.signalMenu = DSPToolSignalsMenu(self)
        menuBar.addMenu(self.signalMenu)

        self.setMenuBar(menuBar)
        
        self.mainWidget=QTableWidget()
        self.mainWidget.setRowCount(0)
        self.mainWidget.setColumnCount(0)
              
        scrollWidget = QScrollArea()
        scrollWidget.setWidget(self.mainWidget)
        scrollWidget.setWidgetResizable(True)
        
        self.setCentralWidget(scrollWidget)
        
    def refreshTable(self):
        i = 0
        for x in self.project.signalList:
            j=0
            self.mainWidget.setRowCount(self.mainWidget.rowCount()+1)
            for y in x:
                print "entrou"                
                if self.mainWidget.columnCount() < j+1: self.mainWidget.setColumnCount(self.mainWidget.columnCount()+1)
                label = y.getImage()
                self.mainWidget.setCellWidget(i,j,label)
                self.mainWidget.resizeColumnsToContents()
                self.mainWidget.resizeRowsToContents()
                j+=1            
            i+=1    
