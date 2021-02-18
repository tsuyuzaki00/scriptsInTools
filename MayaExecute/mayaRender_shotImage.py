from scriptsInTools.MayaLibrary import mayaRender as mr

def main():
    cam1 = mr.createPhotographSet(name = 'front', trs = (2.883, 76.78, 335.096), rot = (0.0, 0.0, 0.0))
    cam2 = mr.createPhotographSet(name = 'side', trs = (342.247, 78.456, 1.291), rot = (0.0, 90.0, 0.0))
    cam3 = mr.createPhotographSet(name = 'persp', trs = (213.072, 216.63, 205.637,), rot = (-25.01, 44.044, -0.0))
    cams = [cam1, cam2, cam3]
    for cam in cams:
        mr.shotImages(cameraShape = cam, imageName = cam[0], workSpacePath="D:/Maya")