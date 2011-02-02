
import sys
from PySide.QtGui import QApplication
from ui.MainWindow import DSPToolMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # TODO: QApplication.translate()

    window = DSPToolMainWindow()
    window.resize(800,600)
    window.show()

    sys.exit(app.exec_())
