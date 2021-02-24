import maya.cmds as cmds

objs = cmds.ls(sl=True)

def auto_side(obj,dist=0):
    get_transX = cmds.xform(obj,q=True,t=True,ws=True)[0]
    get_transX = round(get_transX,3)
    if get_transX > dist:
        left_objs.append(obj)
    elif get_transX < -dist:
        right_objs.append(obj)
    else:
        center_objs.append(obj)
        
def is_side(obj,side):
    if side in obj:
        return obj
    else:
        auto_side(obj)

center_objs = []
right_objs = []
left_objs = []

for obj in objs:
    if is_side(obj,"C"):
        center_objs.append(obj)
    elif is_side(obj,"R"):
        right_objs.append(obj)
    elif is_side(obj,"L"):
        left_objs.append(obj)

print('center',set(center_objs))
print('left',set(left_objs))
print('right',set(right_objs))