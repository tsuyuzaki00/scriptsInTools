import json
import maya.mel as mel
import pymel.core as pm
from scriptsInTools.MayaLibrary import getNameSplits as gns

class SelctJson():
    def __init__(self, fileName = '', workSpacePath = ''):
        self.sels = pm.selected()
        self.fileName = fileName
        self.workSpacePath = workSpacePath

    def selectJsonExport(self):
        mel.eval('setProject "%s";' % self.workSpacePath)
        filePass = pm.workspace(q=True,rootDirectory=1)+'data/'
        jsonName = filePass + self.fileName + '.json'

        lists = []
        for sel in self.sels:
            s =  {'name' : str(sel), 'pos' : gns.pos(sel), 'node': gns.node(sel), 'num': gns.num(sel)}
            lists.append(s)

        with open(jsonName, 'w') as f:
            json.dump(lists, f, indent = 4, ensure_ascii =False)

    def jointLabelling(self, side = 0, type = 18):
        for sel in self.sels:
            pm.setAttr(sel + '.side', side) # 0 = Center 1 = Left 2 = Right 3 = None
            pm.setAttr(sel + '.type' , type) # 18 = Other
            pm.setAttr(sel + '.otherType', str(sel), type = 'string')