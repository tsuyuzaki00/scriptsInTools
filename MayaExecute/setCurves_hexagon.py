import pymel.core as pm
from scriptsInTools.MayaLibrary import setCurves as sc

def main():
    sels = pm.selected()
    setCurve = sc.SetCurve(name = 'curve')
    if sels == []:
        curve = setCurve.curveHexagon()
    else :
        for sel in sels:
            curve = setCurve.curveHexagon()
            trs = setCurve.trsSetting(ctrl = curve)
            setCurve.selectPosition(sel = sel, trs = trs)
        
