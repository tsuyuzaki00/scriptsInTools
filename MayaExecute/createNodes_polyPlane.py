from scriptsInTools.MayaLibrary import createNodes as cn

def main():
    createNode = cn.CreateNode(name = 'model')
    createNode.polyPlaneNode()