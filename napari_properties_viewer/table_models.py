from qtpy.QtCore import QAbstractTableModel, Qt

from .utils import str2prop


class ListTableModel(QAbstractTableModel):
    """Model for the QTableView widget. The table should be stored as a 2D List

    Based on this tutorial:
    https://www.learnpyqt.com/tutorials/qtableview-modelviews-numpy-pandas/
    """
    def __init__(self, data):
        super(ListTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Note: self._data[index.row()][index.column()] will also work
            value = self._data[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]


class DictTableModel(QAbstractTableModel):
    """Dictionary model for the QTableView widget. The table should be stored as a dictionary
    where each key a column name and the values are all rows in that column stored as an array.
    This model is directly compatible with the napari layer properties
    """
    def __init__(self, data):
        super(DictTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role in [Qt.DisplayRole, Qt.EditRole]:
            keys = list(self._data.keys())
            col = self._data[keys[index.column()]]
            value = col[index.row()]
            return str(value)

    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role != Qt.EditRole:
            return False

        keys = list(self._data.keys())
        col = self._data[keys[index.column()]]
        row = index.row()
        converted_value = str2prop(value, col.dtype)
        if converted_value is not None:
            col[row] = converted_value
            self.dataChanged.emit(index, index)
            return True
        else:
            return False

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def rowCount(self, index):

        if len(self._data) > 0:
            keys = list(self._data.keys())
            n_rows = len(self._data[keys[0]])
        else:
            n_rows = 0
        return n_rows

    def columnCount(self, index):
        return len(self._data)

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if len(self._data.keys()) > 0:
                    keys = list(self._data.keys())
                    header = str(keys[section])
                else:
                    header = ''
                return header

            if orientation == Qt.Vertical:
                return str(section)
