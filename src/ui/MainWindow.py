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

from PySide.QtCore import Signal, Slot
from PySide.QtGui import QMainWindow, QVBoxLayout, QMenu, QMenuBar

class DSPToolFileMenu(QMenu):
    """
    """
    def __init__(self, parent=None):
        QMenu.__init__(self, self.trUtf8("&Files"))
        self.parent = parent

        newProjectAction = self.addAction(self.trUtf8("&New Project"))
        newProjectAction.triggered.connect(self.createNewProject)

        quitAction = self.addAction(self.trUtf8("&Quit Program"))
        quitAction.triggered.connect(self.parent.close)

    @Slot()
    def createNewProject(self):
        """
        """
        pass


class DSPToolSignalsMenu(QMenu):
    """
    """
    def __init__(self, parent=None):
        QMenu.__init__(self, self.trUtf8("&Signals"))
        self.parent = parent


class DSPToolMainWindow(QMainWindow):
    """
    """

    def __init__(self):
        QMainWindow.__init__(self)

        menuBar = QMenuBar()

        self.fileMenu = DSPToolFileMenu(self)
        menuBar.addMenu(self.fileMenu)

        self.signalMenu = DSPToolSignalsMenu(self)
        menuBar.addMenu(self.signalMenu)

        self.setMenuBar(menuBar)


