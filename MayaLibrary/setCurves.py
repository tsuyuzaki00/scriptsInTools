import pymel.core as pm
from scriptsInTools.MayaLibrary import getNameSplits as gns
class SetCurve():
    def __init__(self, name):
        self.name = name

    def renameTemplate(self, sel):
        getNameSplit = gns.GetNameSplit()
        scene = getNameSplit.scene()
        num = '1'.zfill(2)
        node = getNameSplit.node(sel)
        pos = getNameSplit.pos(sel)
        rename = '_'.join([pos, self.name, node, scene, num])
        return rename

    def trsSetting(self, ctrl):
        createNull = pm.createNode('transform')
        renameNull = self.renameTemplate(sel = createNull)
        trs = pm.rename(createNull, renameNull)
        pm.parent(ctrl, trs)
        return trs

    def selectPosition(self, sel, trs):
        pm.parent(trs, sel)
        pm.move(0, 0, 0 ,ls=True)
        pm.rotate(0, 0, 0 , os=True)
        pm.parent(trs ,w = True)

    def curveAntenna(self):
        a1 = (0,0,0)
        a2 = (0,3,0)
        a3 = (0,5,0)
        bxf =(1,4,0)
        bxb =(-1,4,0)
        bzf =(0,4,1)
        bzb =(0,4,-1)

        curve = pm.curve( d=1,p=[a1,a3,bxf,a2,bxb,a3,bzf,a2,bzb,a3,bxf,bxb,bzf,bzb,bxf,bzf,bzb,bxb])
        renameCurve = self.renameTemplate(sel = curve)
        antenna = pm.rename(curve, renameCurve)
        return antenna

    def curveArrow1(self):
        a00 = (0, -1, 0)
        a01 = (0,0,1)
        a02 = (0,0,0.5)
        a03 = (0,1,0.5)
        a04 = (0,1,-0.5)
        a05 = (0,0,-0.5)
        a06 = (0,0,-1)

        curve = pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a00])
        renameCurve = self.renameTemplate(sel = curve)
        arrow1 = pm.rename(curve, renameCurve)
        return arrow1

    def curveArrow2(self):
        a00 = (10, 0, 0)
        a01 = (4,0,6)
        a02 = (4,0,2)
        a03 = (2,0,2)
        a04 = (0,0,2)
        a05 = (-2,0,2)
        a06 = (-4,0,2)
        a07 = (-4,0,6)
        a08 = (-10,0,0)
        a09 = (-4,0,-6)
        a10 = (-4,0,-2)
        a11 = (-2,0,-2)
        a12 = (0,0,-2)
        a13 = (2,0,-2)
        a14 = (4,0,-2)
        a15 = (4,0,-6)

        curve = pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00])
        renameCurve = self.renameTemplate(sel = curve)
        arrow2 = pm.rename(curve, renameCurve)
        return arrow2

    def curveArrow4(self):
        a00 = (0,-1,-1)
        a01 = (0,-3,-1)
        a02 = (0,-3,-2)
        a03 = (0,-5,0)
        a04 = (0,-3,2)
        a05 = (0,-3,1)
        a06 = (0,-1,1)
        a07 = (0,-1,3)
        a08 = (0,-2,3)
        a09 = (0,0,5)
        a10 = (0,2,3)
        a11 = (0,1,3)
        a12 = (0,1,1)
        a13 = (0,3,1)
        a14 = (0,3,2)
        a15 = (0,5,0)
        a16 = (0,3,-2)
        a17 = (0,3,-1)
        a18 = (0,1,-1)
        a19 = (0,1,-3)
        a20 = (0,2,-3)
        a21 = (0,0,-5)
        a22 = (0,-2,-3)
        a23 = (0,-1,-3)
        a24 = (0,-1,-1)

        curve = pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a00])
        renameCurve = self.renameTemplate(sel = curve)
        arrow4 = pm.rename(curve, renameCurve)
        return arrow4

    def curveCircle(self):
        curve = pm.circle( nr = (1, 0, 0), c = (0, 0, 0), sw = 360, r = 2, ch = False)
        renameCurve = self.renameTemplate(sel = curve)
        circle = pm.rename(curve, renameCurve)
        return circle

    def curveCube(self):
        a1 = (10,10,10)
        a2 = (10,10,-10)
        a3 = (-10,10,-10)
        a4 = (-10,10,10)
        b1 = (10,-10,10)
        b2 = (10,-10,-10)
        b3 = (-10,-10,-10)
        b4 = (-10,-10,10)

        curve = pm.curve( d=1,p=[a1,a2,a3,a4,a1,b1,b2,a2,b2,b3,a3,b3,b4,a4,b4,b1])
        renameCurve = self.renameTemplate(sel = curve)
        cube = pm.rename(curve, renameCurve)
        return cube

    def curveHexagon(self):
        height = 2
        a1 = (0,-1,0)
        a2 = (0,-0.5,0.87)
        a3 = (0,0.5,0.87)
        a4 = (0,1,0)
        a5 = (0,0.5,-0.87)
        a6 = (0,-0.5,-0.87)
        b1 = (height,-1,0)
        b2 = (height,-0.5,0.87)
        b3 = (height,0.5,0.87)
        b4 = (height,1,0)
        b5 = (height,0.5,-0.87)
        b6 = (height,-0.5,-0.87)

        curve = pm.curve( d=1,p=[a1,a2,a3,a4,a5,a6,a1,b1,b2,a2,b2,b3,a3,b3,b4,a4,b4,b5,a5,b5,b6,a6,b6,b1])
        renameCurve = self.renameTemplate(sel = curve)
        hexagon = pm.rename(curve, renameCurve)
        return hexagon

    def curvePyramid(self):
        a00 = (0, 2, 0)
        a01 = (0, 0, 1)
        a02 = (1, 0, 0)
        a03 = (0, 0, -1)
        a04 = (-1, 0, 0)

        curve = pm.curve( d=1,p=[a00,a01,a02,a03,a04,a01,a00,a02,a00,a03,a00,a04,a00])
        renameCurve = self.renameTemplate(sel = curve)
        pyramid = pm.rename(curve, renameCurve)
        return pyramid

    def curveSquare(self):
        curve = pm.curve( d=1,p=[(1,0,1),(-1,0,1),(-1,0,-1),(1,0,-1),(1,0,1)])
        renameCurve = self.renameTemplate(sel = curve)
        square = pm.rename(curve, renameCurve)
        return square

    def curveTwist(self):
        a00 = (0, -1, 0)
        a01 = (0,-0.5,0.2)
        a02 = (0,-0.7,0.7)
        a03 = (0,-0.2,0.5)
        a04 = (0,0,1)
        a05 = (0,0.2,0.5)
        a06 = (0,0.7,0.7)
        a07 = (0,0.5,0.2)
        a08 = (0,1.5,0)
        a09 = (0,0.5,-0.2)
        a10 = (0,0.7,-0.7)
        a11 = (0,0.2,-0.5)
        a12 = (0,0,-1)
        a13 = (0,-0.2,-0.5)
        a14 = (0,-0.7,-0.7)
        a15 = (0,-0.5,-0.2)

        curve = pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00])
        renameCurve = self.renameTemplate(sel = curve)
        twist = pm.rename(curve, renameCurve)
        return twist

    def curveVectorIK(self):
        height = 1.4
        xu = (height,0,0)
        xd = (-height, 0, 0)
        yu = (0,height,0)
        yd = (0,-height,0)
        zu = (0, 0, height)
        zd = (0,0,-height)
        
        curve = pm.curve( d=1,p=[xu,zd,xd,zu,xu,yu,xd,yd,xu,zd,yu,zu,yd,zd])
        renameCurve = self.renameTemplate(sel = curve)
        vectorIK = pm.rename(curve, renameCurve)
        return vectorIK

    