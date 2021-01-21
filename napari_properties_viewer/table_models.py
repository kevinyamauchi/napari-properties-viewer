from qtpy.QtCore import QAbstractTableModel, Qt


class ArrayTableModel(QAbstractTableModel):

    def __init__(self, data):
        super(ArrayTableModel, self).__init__()
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

    def __init__(self, data):
        super(DictTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            keys = list(self._data.keys())
            col = self._data[keys[index.column()]]
            value = col[index.row()]
            return str(value)

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
                keys = list(self._data.keys())
                return str(keys[section])

            if orientation == Qt.Vertical:
                return str(section)
