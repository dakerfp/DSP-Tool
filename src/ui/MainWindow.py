
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


