import os, json
from PySide2 import QtWidgets, QtCore, QtGui
from mainEdit import qt
import pymel.core as pm

class OptionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)

        dialog = QtWidgets.QColorDialog(self)
        result = dialog.exec_()
        if result:
            colorChange(dialog.selectedColor())

def colorChange(radio):
    sel = pm.selected()
    shapes = pm.listRelatives(sel[0:], type='nurbsCurve')
    for shape in shapes:
        pm.setAttr(shape + '.overrideEnabled', 1)
        pm.setAttr(shape + '.overrideRGBColors', 1)
        pm.setAttr(shape + '.overrideColorRGB', radio.redF(), radio.greenF(), radio.blueF(), type = 'double3')


def main():
    window = OptionWidget(qt.getMayaWindow())
    window.show()
