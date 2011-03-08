
from PySide.QtCore import QUrl, Slot
from PySide.QtDeclarative import QDeclarativeView
from scripts.script import Module

class ScriptSelector(QDeclarativeView):
    def __init__(self, modules_path):
        QDeclarativeView.__init__(self)
        self.module = Module(modules_path)
        context = self.rootContext()
        print self.module.modules
        context.setContextProperty('plugins', self.module.toDict())
        self.setSource(QUrl('ui/qml/ScriptChooser.qml'))


    @Slot(int, int)
    def scriptSelected(self, scriptIndex, ):
	pass # TODO
