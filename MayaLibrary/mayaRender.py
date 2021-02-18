import maya.cmds as cmds
import maya.mel as mel

def createPhotographSet(name = 'camera', trs = (0, 0, 5), rot = (0,0,0)):
    cam = cmds.camera(name = 'shotCam_' + name)
    litShape = cmds.spotLight()
    litParent = cmds.listRelatives(litShape, p = True)
    lit = cmds.rename(litParent, 'shotLit_' + name)
    cmds.setAttr(cam[0] + '.translate', trs[0], trs[1], trs[2], type = 'double3')
    cmds.setAttr(cam[0] + '.rotate', rot[0], rot[1], rot[2], type = 'double3')
    cmds.setAttr(lit + '.translate', trs[0], trs[1], trs[2], type = 'double3')
    cmds.setAttr(lit + '.rotate', rot[0], rot[1], rot[2], type = 'double3')
    cmds.parent(lit, cam[0])
    return cam

def shotImages(cameraShape = [], fileName = '', width = 1920, height = 1080, imageFormat = 32, isRenderer = 'mayaHardware2', workSpacePath = ''):
    mel.eval("setProject '%s';" % workSpacePath)
    cmds.setAttr('perspShape' + '.renderable', 0)
    cmds.setAttr('defaultRenderGlobals.animation', 0)
    cmds.setAttr('defaultRenderGlobals.currentRenderer', isRenderer, type = 'string')
    cmds.setAttr('defaultRenderGlobals.imageFilePrefix', fileName, type = 'string')
    cmds.setAttr('defaultResolution.width', width)
    cmds.setAttr('defaultResolution.height', height)
    cmds.setAttr('defaultRenderGlobals.imageFormat', imageFormat)
    cmds.setAttr(cameraShape[1] + '.renderable', 1)
    cmds.render(b = True, rep = True)
    cmds.delete(cameraShape[0])

def secenece(cameraShape = [], fileName = '', width = 1920, height = 1080, imageFormat = 32, isRenderer = 'mayaHardware2', workSpacePath = '', startFrame = 0, endFrame = 1):
    mel.eval("setProject '%s';" % workSpacePath)
    cmds.setAttr('perspShape' + '.renderable', 0)
    cmds.setAttr('defaultRenderGlobals.currentRenderer', isRenderer, type = 'string')
    cmds.setAttr('defaultRenderGlobals.imageFilePrefix', fileName, type = 'string')
    cmds.setAttr('defaultResolution.width', width)
    cmds.setAttr('defaultResolution.height', height)
    cmds.setAttr('defaultRenderGlobals.imageFormat', imageFormat)
    cmds.setAttr(cameraShape[1] + '.renderable', 1)
    cmds.setAttr('defaultRenderGlobals.outFormatControl', 0)
    cmds.setAttr('defaultRenderGlobals.animation', 1)
    cmds.setAttr('defaultRenderGlobals.animationRange', 0)
    cmds.setAttr('defaultRenderGlobals.extensionPadding', 3)
    cmds.setAttr('defaultRenderGlobals.startFrame', startFrame)
    cmds.setAttr('defaultRenderGlobals.endFrame', endFrame)
    cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
    cmds.setAttr('defaultRenderGlobals.periodInExt', 2)
    cmds.render(b = True, rep = True)

def runPlayblast(cam = '', fileName = '', width = 1920, height = 1080, workSpacePath = '', startFrame = 0, endFrame = 3):
    mel.eval('setProject "%s";' % workSpacePath)
    path = cmds.workspace(q=True,rootDirectory=1)+'movies/'
    cmds.lookThru(cam)
    cmds.playblast(st = startFrame, et = endFrame, fo = True, w = width, h = height, v = False, c = 'h264', orn = True, fmt = 'qt', p = 100, f = path + fileName)

def wireFrameImage(cameraShape = [], fileName = '', width = 1920, height = 1080, imageFormat = 32, isRenderer = 'mayaHardware2', workSpacePath = ''):
    mel.eval("setProject '%s';" % workSpacePath)