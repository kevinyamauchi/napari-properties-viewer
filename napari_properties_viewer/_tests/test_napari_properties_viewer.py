import numpy as np
from napari_properties_viewer.qt_properties_table import QtPropertiesTable
import napari
from qtpy.QtWidgets import QWidget


def test_qt_properties_table():
    # create a viewer with a points layer
    points_data = np.random.random((10, 2))
    points_properties = {'probability': np.random.random((10,))}
    layer_name = 'points_layer'
    viewer = napari.view_points(points_data, properties=points_properties, name=layer_name)

    properties_widget = QtPropertiesTable(viewer)
    assert isinstance(properties_widget, QWidget)
    assert properties_widget.selected_layer == layer_name



