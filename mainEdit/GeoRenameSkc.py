import pymel.core as pm

def cluster_rename(sels,source_name="_Geo",cluster_name="_Skc"):
    for sel in sels:
        shape = pm.listRelatives(sel, c = True)
        if shape[0].nodeType() == 'mesh':
            skinCluster = pm.listConnections( shape[0] + '.inMesh', d=False, s=True)
            if skinCluster[0].nodeType() == 'skinCluster':
                fix_name = sel.replace(source_name,cluster_name)
                pm.rename(skinCluster[0],fix_name)

sels = pm.selected()
cluster_rename(sels,source_name="_Geo",cluster_name="_Skc")