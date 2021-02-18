import sys
import pymel.core as pm
import maya.cmds as cmds
from maya import utils

from scriptsInTools.singleRun import menu
utils.executeDeferred(menu.main)

try:
    # Open new ports
    cmds.commandPort(name=":7001", sourceType="mel", echoOutput=True)
    cmds.commandPort(name=":7002", sourceType="python", echoOutput=True)
except RuntimeError:
    pass