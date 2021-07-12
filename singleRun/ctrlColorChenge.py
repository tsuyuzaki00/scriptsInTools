import os, json
from PySide2 import QtWidgets, QtCore, QtGui
from ..MayaLibrary import qt
import pymel.core as pm
class Settings(object):
    def __init__(self):
        temp = __name__.split('.')
        self.__filename = os.path.join(
			os.getenv('MAYA_APP_DIR'),
			temp[0],
			temp[-1]+'.json'
			)
        self.reset()
        self.read()
        
    def read(self):
        if os.path.exists(self.__filename):
            with open(self.__filename, 'r') as f:
                saveData = json.load(f)
                #self.guide = saveData['guide']
                #self.geometry = saveData['geometry']
                #self.joint = saveData['joint']
                #self.ctrl = saveData['ctrl']
                #self.camera = saveData['camera']
                #self.light = saveData['light']
    
    def reset(self):
        self.guide = False
        self.geometry = True
        self.joint = False
        self.ctrl = False
        self.camera = False
        self.light = False
        
    def save(self):
        saveData = { #'guide':self.guide,
                    #'geometry':self.geometry
                    #'joint':self.joint
                    #'ctrl':self.ctrl
                    #'camera':self.camera
                    #'light':self.light
                    }
        if not os.path.exists(self.__filename):
            os.makedirs(os.path.dirname(self.__filename))
        with open(self.__filename, 'w') as f:
            json.dump(saveData, f)

settings = Settings()

class OptionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)
        mainLayout = QtWidgets.QFormLayout(self)
        self.setWindowTitle('ctrlColorChenge')

        yellow = QtWidgets.QRadioButton('Yellow', self)
        mainGreen = QtWidgets.QRadioButton('Green', self)
        subGreen = QtWidgets.QRadioButton('DarkGreen', self)
        
        mainRed = QtWidgets.QRadioButton('Red', self)
        pink = QtWidgets.QRadioButton('Pink', self)
        subRed = QtWidgets.QRadioButton('DarkRed', self)
        
        mainBlue = QtWidgets.QRadioButton('Blue', self)
        cyan = QtWidgets.QRadioButton('Cyan', self)
        subBlue = QtWidgets.QRadioButton('DarkBlue', self)
        
        purple = QtWidgets.QRadioButton('Purple', self)
        magenta = QtWidgets.QRadioButton('Magenta', self)
        crimson = QtWidgets.QRadioButton('Crimson', self)
        yellow.setChecked(True)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(yellow, True)
        acrossLayout.addWidget(mainGreen, True)
        acrossLayout.addWidget(subGreen, True)
        mainLayout.addRow('Center Color', acrossLayout)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(mainBlue, True)
        acrossLayout.addWidget(cyan, True)
        acrossLayout.addWidget(subBlue, True)
        mainLayout.addRow('Left Color', acrossLayout)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(mainRed, True)
        acrossLayout.addWidget(pink, True)
        acrossLayout.addWidget(subRed, True)
        mainLayout.addRow('Right Color', acrossLayout)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(magenta, True)
        acrossLayout.addWidget(purple, True)
        acrossLayout.addWidget(crimson, True)
        mainLayout.addRow('other Color', acrossLayout)

        self.__across = QtWidgets.QButtonGroup(self)
        self.__across.addButton(yellow, 0)
        self.__across.addButton(mainGreen, 1)
        self.__across.addButton(subGreen, 2)

        self.__across.addButton(mainBlue, 3)
        self.__across.addButton(cyan, 4)
        self.__across.addButton(subBlue, 5)

        self.__across.addButton(mainRed, 6)
        self.__across.addButton(pink, 7)
        self.__across.addButton(subRed, 8)
        
        self.__across.addButton(magenta, 9)
        self.__across.addButton(purple, 10)
        self.__across.addButton(crimson, 11)

        self.num = self.__across.checkedId()

        button = QtWidgets.QPushButton('chengeColor')

        widthLayout = QtWidgets.QHBoxLayout(self)
        widthLayout.addWidget(button, True)
        mainLayout.addRow(widthLayout)

        button.clicked.connect(self.chenge)

    def chenge(self):
        self.num = self.__across.checkedId()
        colorChange(self.num)

def colorChange(radio):
    sel = pm.selected()
    shapes = pm.listRelatives(sel[0:], type='nurbsCurve')
    for shape in shapes:
        pm.setAttr(shape + '.overrideEnabled', 1)
        if radio == 0:
            pm.setAttr(shape + '.overrideColor', 17)#Yellow
        elif radio == 1:
            pm.setAttr(shape + '.overrideColor', 14)#Green
        elif radio == 2:
            pm.setAttr(shape + '.overrideColor', 7)#DarkGreen
        elif radio == 3:
            pm.setAttr(shape + '.overrideColor', 6)#Blue
        elif radio == 4:
            pm.setAttr(shape + '.overrideColor', 18)#Cyan
        elif radio == 5:
            pm.setAttr(shape + '.overrideColor', 5)#DarkBlue
        elif radio == 6:
            pm.setAttr(shape + '.overrideColor', 13)#Red
        elif radio == 7:
            pm.setAttr(shape + '.overrideColor', 20)#Pink
        elif radio == 8:
            pm.setAttr(shape + '.overrideColor', 4)#DarkRed
        elif radio == 9:
            pm.setAttr(shape + '.overrideColor', 9)#Magenta
        elif radio == 10:
            pm.setAttr(shape + '.overrideColor', 30)#Purple
        elif radio == 11:
            pm.setAttr(shape + '.overrideColor', 31)#Crimson
            

def main():
    window = OptionWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.show()
