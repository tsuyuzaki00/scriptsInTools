import pymel.core as pm

sels = pm.selected()

for sel in sels:
    shape = pm.listRelatives(sel, c = True)
    if shape[0].nodeType() == 'mesh':
        skinCluster = pm.listConnections( shape[0] + '.inMesh', d=False, s=True)
        if skinCluster[0].nodeType() == 'skinCluster':
            fix_name = sel.replace("_Geo","_Skc")
            pm.rename(skinCluster[0],fix_name)