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
