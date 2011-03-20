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
import sys
import pickle
import numpy as np
import scipy as sp
from util.Project import Project
from SideBar import SideBar
from PropertyBar import PropertyBar
import scipy.signal as sig
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from util.addSignal import addSignal
from util.openProject import openProject
from util.createProject import createProject
from PySide.QtCore import Signal, Slot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PySide.QtGui import QDialog, QErrorMessage, QTableWidget, QMessageBox
from PySide.QtGui import QMainWindow, QVBoxLayout, QMenu, QMenuBar, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QScrollArea


class DSPToolFileMenu(QMenu):
    """
    """
    def __init__(self, parent=None):
        QMenu.__init__(self, "&Files")
        self.parent = parent
        
        self.setWindowTitle("DSP-Tool")

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
        
        self.initializeUI()
        self.platform = sys.platform
		
    def refreshTable(self):
        '''
        '''        
        for i in range(0, len(self.project.signalList)):
            self.table.setRowCount(self.table.rowCount()+1)
            for j in range (0, len(self.project.signalList[i])):                        
                if self.table.columnCount() < j+1: self.table.setColumnCount(self.table.columnCount()+1)
                label = self.project.signalList[i][j].getImage()
                self.table.setCellWidget(i,j,label)
                self.table.resizeColumnsToContents()
                self.table.resizeRowsToContents()
        self.setLabels()
    
    def setLabels(self):
        '''
        '''
        self.table.setHorizontalHeaderLabels(self.project.horizontalLabels)
        self.table.setVerticalHeaderLabels(self.project.verticalLabels)
    
    def oneClickedEvent(self):
        index =  self.table.selectedIndexes()[0]
        i = index.row()
        j = index.column()
        self.sideBar.setProperties(self.project.signalList[i][j])
    
    def refreshProperties(self):
        self.propertyBar.setProperties()
		
    def initializeUI(self):
    
        self.mainWidget = QWidget()
        
        #Size
        self.resize(1024,768)       
        
        #MenuBar
        menuBar = QMenuBar()
        self.fileMenu = DSPToolFileMenu(self)
        menuBar.addMenu(self.fileMenu)
        self.signalMenu = DSPToolSignalsMenu(self)
        menuBar.addMenu(self.signalMenu)
        self.setMenuBar(menuBar)
                
        #Table Widget
        self.table = QTableWidget()
        self.table.setFixedWidth(824)        
        scrollTable = QScrollArea()
        scrollTable.setWidget(self.table)
        scrollTable.setWidgetResizable(True)
        
        #Side and Property Bar
        self.sideBar = SideBar()
        self.propertyBar = PropertyBar(self)
        
        #Layouts
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.table)               
        hLayout.addWidget(self.sideBar)        
        hWidget = QWidget()
        hWidget.setLayout(hLayout)               
        vLayout = QVBoxLayout()
        vLayout.addWidget(hWidget)       
        vLayout.addWidget(self.propertyBar)
        self.mainWidget.setLayout(vLayout)
        self.setCentralWidget(self.mainWidget)
        
        #Signals
        self.table.cellClicked.connect(self.oneClickedEvent)  
    
