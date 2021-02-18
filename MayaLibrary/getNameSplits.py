import pymel.core as pm
class GetNameSplit():
    def scene(self):
        sceneName = pm.sceneName().basename()
        part = sceneName.split("_")
        if part[0].endswith('.ma') or part[0].endswith('.mb'):
            scene = part[0][:-3]
        elif part[0] == '':
            scene = 'scene'
        else:
            scene = part[0]
        return scene

    def obj(self, sel):
        part = sel.split("_")

        if part[0] == self.pos(sel):
            if part[1] == self.scene():
                obj = part[2]
                return obj
            else :
                obj = part[1]
                return obj
        elif part[0] == self.node(sel):
            obj = part[1]
            return obj
        elif part[0] == self.scene():
            obj = part[1]
            return obj     
        else :
            obj = part[0]
            return obj

    def node(self, sel):
        if sel.nodeType() == 'transform':
            if pm.listRelatives(sel, s = True) == []:
                node = 'null'
                return node
            elif pm.listRelatives(sel, c = True, type = 'mesh'):
                node = 'geo'
                # cage
                return node
            elif pm.listRelatives(sel, c = True, type = 'nurbsCurve'):
                node = 'ctl'
                return node
            elif pm.listRelatives(sel, c = True, type = 'nurbsSurface'):
                node = 'surf'
                return node
            elif pm.listRelatives(sel, c = True, type = 'camera'):
                node = 'cam'
                return node
            elif pm.listRelatives(sel, c = True, type = 'locator'):
                node = 'loc'
                return node
            elif pm.listRelatives(sel, c = True, type = 'imagePlane'):
                node = 'image'
                return node
            elif pm.listRelatives(sel, c = True, type = 'spotLight'):
                node = 'spl'
                return node
            elif pm.listRelatives(sel, c = True, type = 'ambientLight'):
                node = 'aml'
                return node
            elif pm.listRelatives(sel, c = True, type = 'pointLight'):
                node = 'pol'
                return node
            elif pm.listRelatives(sel, c = True, type = 'directionalLight'):
                node = 'drl'
                return node
            elif pm.listRelatives(sel, c = True, type = 'follicle'):
                node = 'flc'
                return node
        elif sel.nodeType() == 'joint':
            node = 'jnt'
            return node
        elif sel.nodeType() == 'parentConstraint':
            node = 'prc'
            return node
        elif sel.nodeType() == 'pointConstraint':
            node = 'pnc'
            return node
        elif sel.nodeType() == 'orientConstraint':
            node = 'orc'
            return node
        elif sel.nodeType() == 'scaleConstraint':
            node = 'slc'
            return node
        elif sel.nodeType() == 'aimConstraint':
            node = 'amc'
            return node
        elif sel.nodeType() == 'poleVectorConstraint':
            node = 'pvc'
            return node
        elif sel.nodeType() == 'ikHandle':
            node = 'ikhl'
            return node
        elif sel.nodeType() == 'ikEffector':
            node = 'ikef'
            return node
        elif sel.nodeType() == 'condition':
            node = 'cnd'
            return node
        elif sel.nodeType() == 'multiplyDivide':
            node = 'mdp'
            return node
        elif sel.nodeType() == 'plusMinusAverage':
            node = 'pma'
            return node
        elif sel.nodeType() == 'reverse':
            node = 'rvs'
            return node
        elif sel.nodeType() == 'clamp':
            node = 'clp'
            return node
        elif sel.nodeType() == 'blendColors':
            node = 'bdc'
            return node
        elif sel.nodeType() == 'multMatrix':
            node = 'mmx'
            return node
        elif sel.nodeType() == 'decomposeMatrix':
            node = 'dmx'
            return node
        elif sel.nodeType() == 'composeMatrix':
            node = 'cmx'
            return node
        elif sel.nodeType() == 'distanceBetween':
            node = 'dist'
            return node
        elif sel.nodeType() == 'curveInfo':
            node = 'info'
            return node
        elif sel.nodeType() == 'skinCluster':
            node = 'skc'
            # csw = copy skin weights
            return node
        elif sel.nodeType() == 'lambert':
            node = 'lbt'
            #test = pm.listConnections(sel + '.color', d = True)
            #print test
            #pm.rename(color,node + obj(sel) + scene())
            return node

        #elif sel.nodeType() == 'file':
            node = 'color' #baseColor
            node = 'nmp' #normalMap

    def pos(self, sel):
        pos = 'C'
        if 'joint' == self.node(sel):
            if pm.listRelatives(sel, c = True) == []:
                pos = 'CT'

        elif sel.endswith('_C') or sel.startswith('C_'):
            pos = 'C'
        elif sel.endswith('_CT') or sel.startswith('CT_'):
            pos = 'CT'
        elif sel.endswith('_L') or sel.startswith('L_'):
            pos = 'L'
        elif sel.endswith('_LT') or sel.startswith('LT_'):
            pos = 'LT'
        elif sel.endswith('_R') or sel.startswith('R_'):
            pos = 'R'
        elif sel.endswith('_RT') or sel.startswith('RT_'):
            pos = 'RT'
        elif sel.endswith('_U') or sel.startswith('U_'):
            pos = 'U'
        elif sel.endswith('_D') or sel.startswith('D_'):
            pos = 'D'
        else :
            pos = 'C'

        return pos

    def num(self, sel):
        part = sel.split("_")
        try:
            part[-1]
            part[-2]
        except IndexError:
            num = '0'.zfill(2)
            return num
        else :
            if (part[-1].startswith('0') 
                or part[-1].startswith('1')
                or part[-1].startswith('2')
                or part[-1].startswith('3')
                or part[-1].startswith('4')
                or part[-1].startswith('5')
                or part[-1].startswith('6')
                or part[-1].startswith('7')
                or part[-1].startswith('8')
                or part[-1].startswith('9')) :
                num = part[-1]
                return num   
            elif (part[-2].startswith('0') 
                or part[-2].startswith('1')
                or part[-2].startswith('2')
                or part[-2].startswith('3')
                or part[-2].startswith('4')
                or part[-2].startswith('5')
                or part[-2].startswith('6')
                or part[-2].startswith('7')
                or part[-2].startswith('8')
                or part[-2].startswith('9')) :
                num = part[-2]
                return num
            else :
                num = '0'.zfill(2)
                return num

    def sameNameCheck(self, check):
        print (check)
        if pm.objExists(check):
            check = check + '_NG'
            return check
        else :
            return check