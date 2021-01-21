from qtpy.QtCore import Qt
from qtpy.QtWidgets import QWidget, QComboBox, QTableView, QVBoxLayout

from .table_models import DictTableModel


class QtPropertiesTable(QWidget):
    def __init__(
        self,
        viewer: 'napari.viewer.Viewer',
        parent=None,
    ):
        super(QtPropertiesTable, self).__init__(parent)

        self.viewer = viewer

        # create the table widget
        self.table = QTableView()

        # Create a combobox for selecting layers
        self.layer_combo_box = QComboBox(self)
        self.selected_layer = None
        self.layer_combo_box.currentIndexChanged.connect(self.on_layer_selection)
        self.update_layer_combobox()

        self.viewer.layers.events.inserted.connect(self.add_layer)
        self.viewer.layers.events.removed.connect(self.remove_layer)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.layer_combo_box)
        self.vbox_layout.addWidget(self.table)

        self.setLayout(self.vbox_layout)

    def update_layer_combobox(self):

        layer_names = [layer.name for layer in self.viewer.layers if hasattr(layer, 'properties')]
        self.layer_combo_box.addItems(layer_names)

        if self.selected_layer is None:
            self.selected_layer = layer_names[0]
        index = self.layer_combo_box.findText(
            self.selected_layer, Qt.MatchExactly
        )
        self.layer_combo_box.setCurrentIndex(index)

    def add_layer(self, event):
        layer_name = event.value.name
        layer = self.viewer.layers[layer_name]
        if hasattr(layer, 'properties'):
            self.layer_combo_box.addItem(layer_name)

    def remove_layer(self, event):
        layer_name = event.value.name

        index = self.layer_combo_box.findText(
            layer_name, Qt.MatchExactly
        )
        # findText returns -1 if the item isn't in the ComboBox
        # if it is in the ComboBox, remove it
        if index != -1:
            self.layer_combo_box.removeItem(index)

            # get the new layer selection
            index = self.layer_combo_box.currentIndex()
            layer_name = self.layer_combo_box.itemText(index)
            if layer_name != self.selected_layer:
                self.selected_layer = layer_name

    def on_layer_selection(self, index: int):
        if index != -1:
            layer_name = self.layer_combo_box.itemText(index)
            selected_layer = self.viewer.layers[layer_name]
            if hasattr(selected_layer, 'properties'):
                layer_properties = selected_layer.properties
                self.table_model = DictTableModel(layer_properties)
                self.table.setModel(self.table_model)
                self._connect_layer_events(layer_name)
            else:
                print('no properties')
        else:
            self.table_model = DictTableModel({})
            self.table.setModel(self.table_model)

    def update_table(self, event):
        selected_layer = self.viewer.layers[self.selected_layer]
        layer_properties = selected_layer.properties

        # todo: implement set_data method and events
        self.table_model = DictTableModel(layer_properties)
        self.table.setModel(self.table_model)

    def _connect_layer_events(self, layer_name):
        layer = self.viewer.layers[layer_name]
        layer.events.properties.connect(self.update_table)

    def _disconnect_layer_events(self):
        layer = self.viewer.layers[self.selected_layer]
        layer.events.properties.disconnect(self.update_table)