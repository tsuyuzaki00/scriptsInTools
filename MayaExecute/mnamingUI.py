import qt
from PySide2 import QtGui, QtCore, QtWidgets

class MNamingWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MNamingWindow, self).__init__(*args, **kwargs)
        main_layout = QtWidgets.QFormLayout(self)

        # create buttons
        auto_button = QtWidgets.QRadioButton("Auto", self)
        center_button = QtWidgets.QRadioButton("Center", self)
        left_button = QtWidgets.QRadioButton("Left", self)
        right_button = QtWidgets.QRadioButton("Right", self)
        auto_button.setChecked(True)
        select_label = QtWidgets.QLabel("SelectList",self)
        select_list = QtWidgets.QLineEdit(self)
        asset_label = QtWidgets.QLabel("AssetName",self)
        asset_name = QtWidgets.QLineEdit(self)
        variant_label = QtWidgets.QLabel("VariantName",self)
        variant_name = QtWidgets.QLineEdit(self)
        num_switch = QtWidgets.QCheckBox("", self)
        add_select_button = QtWidgets.QPushButton("Add")
        rename_button = QtWidgets.QPushButton("Rename")

        #setting buttons
        label_layout = QtWidgets.QHBoxLayout(self)
        label_layout.addWidget(select_label)
        label_layout.addWidget(asset_label)
        label_layout.addWidget(variant_label)
        main_layout.addRow(label_layout)

        rename_layout = QtWidgets.QHBoxLayout(self)
        rename_layout.addWidget(select_list)
        rename_layout.addWidget(asset_name)
        rename_layout.addWidget(variant_name)
        main_layout.addRow(rename_layout)

        side_layout = QtWidgets.QHBoxLayout(self)
        side_layout.addWidget(auto_button)
        side_layout.addWidget(left_button)
        side_layout.addWidget(center_button)
        side_layout.addWidget(right_button)
        main_layout.addRow("side", side_layout)

        num_switch_layout = QtWidgets.QVBoxLayout(self)
        num_switch_layout.addWidget(num_switch, True)
        main_layout.addRow("number",num_switch_layout)

        run_layout = QtWidgets.QHBoxLayout(self)
        run_layout.addWidget(add_select_button, True)
        run_layout.addWidget(rename_button, True)
        main_layout.addRow(run_layout)

def option():
    window = MNamingWindow(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.show()