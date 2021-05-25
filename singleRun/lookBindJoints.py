from ..MayaLibrary import qt, getNameSplits as gns
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm

def listBindJoints(sels):
    getNameSplit = gns.GetNameSplit()
    window = QtWidgets.QWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.resize(650,300)
    layout = QtWidgets.QVBoxLayout(window)
    
    widget = QtWidgets.QPlainTextEdit(window)
    
    for sel in sels:
        shape = pm.listRelatives(sel, c = True)
        if shape[0].nodeType() == 'mesh':
            skinCluster = pm.listConnections( shape[0] + '.inMesh', d=False, s=True)
            if skinCluster[0].nodeType() == 'skinCluster':
                bindList = pm.listConnections( skinCluster[0] + ".matrix", d=False, s=True)
                widget.insertPlainText(getNameSplit.obj(sel) + "Bind = [\n")
                for jntList in bindList:
                    widget.insertPlainText('\t"' + jntList + '",\n')
                widget.insertPlainText('\t]\n')
                skcName = sel.replace(getNameSplit.node(sel), 'skc')
                cswName = sel.replace(getNameSplit.node(sel), 'csw')
                widget.insertPlainText('pm.skinCluster("'+ sel +'", ' + getNameSplit.obj(sel) +'Bind, n = "'+ skcName +'", tsb = True)\n')
                widget.insertPlainText('pm.copySkinWeights(ss = "'+ str(skinCluster[0]) +'", ds = "' + skcName + '", noMirror = True)\n')
                
            else :
                pm.error('Unbound or SkinCluster is not connected')
        else :
            pm.error('The selected object is not geometry')
    
    layout.addWidget(widget)

    button = QtWidgets.QPushButton('print',window)
    layout.addWidget(button)

    button.clicked.connect(main)
    
    window.show()

def main():
    sels = pm.selected()
    listBindJoints(sels)