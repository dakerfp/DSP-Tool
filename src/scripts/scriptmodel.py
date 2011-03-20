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

from PySide.QtCore import Qt, QModelIndex, QAbstractItemModel

from script import Script, Plugin, Module

class ScriptModel(QAbstractItemModel):


    def __init__(self, pluginsPath, parent=None):
        super(ScriptModel, self).__init__(parent)
        self.rootItem = Module(pluginsPath)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if parent.isValid():
            return len(parent.internalPointer())
        else:
            return len(self.rootItem)

    def columnCount(self, parent):
        return 3

    def data(self, index, role):
        if not index.isValid() or role != Qt.DisplayRole:
            return None

        col = index.column()

        item = index.internalPointer()

        print item, index

        if col == 0:
            return item.name
        elif col == 1:
            return item.doc
        elif col == 2:
            return len(item)
        else:
            return None

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem[row]
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return "Module"
            elif section == 1:
                return "Summary"
            elif section == 2:
                return "len"


    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row, 0, parentItem.parent)


if __name__ == '__main__':
    from PySide import QtGui
    import sys

    app = QtGui.QApplication(sys.argv)

    rootpath = "/home/dakerfp/work/dsp-tool/src/scripts/plugins"
    model = ScriptModel(rootpath)
    print repr(model.rootItem)
    model.row = 0

    view = QtGui.QTreeView()
    view.setModel(model)
    view.setWindowTitle("Select Script")
    view.resize(900,600)
    view.show()

    sys.exit(app.exec_())


