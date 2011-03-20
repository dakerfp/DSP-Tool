
from PySide.QtCore import QUrl, Slot
from PySide.QtDeclarative import QDeclarativeView
from scripts.script import Module
from threading import Lock

class ScriptSelector(QDeclarativeView):

    def __init__(self, modules_path):
        QDeclarativeView.__init__(self)
        self.module = Module(modules_path)
        context = self.rootContext()
        print self.module.modules
        context.setContextProperty('plugins', self.module.toDict())
        self.setSource(QUrl('ui/qml/ScriptChooser.qml'))
        self.rootObject().scriptSelected.connect(self.onScriptSelected)
        self.__lock = Lock()

    @Slot(int, int)
    def onScriptSelected(self, moduleIndex, scriptIndex):
        self.hide()
        with self.__lock:
            if self.callback:
                self.callback(self.module[moduleIndex][scriptIndex])
                self.callback = None

    def selectScript(self, callback):
        self.show()
        self.callback = callback
