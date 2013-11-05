def script_dir_to_import(dir):
	sys.path.append(os.path.join(cmds.internalVar(usd = True), dir))

def convertSel(toType):
	if(toType == "faces"):
		mel.eval("PolySelectConvert 1")
		sel = cmds.ls(sl=True)
		mel.eval("SelectFacetMask")
	elif(toType == "edges"):
		mel.eval("PolySelectConvert 2")
		sel = cmds.ls(sl=True)
		mel.eval("SelectEdgeMask")
	elif(toType == "vertices"):
		mel.eval("PolySelectConvert 3")
		sel = cmds.ls(sl=True)
		mel.eval("SelectVertexMask")
	cmds.select(sel)

print "  Importing primary modules"
import sys
import os
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
print "  Finished."
print "--" * 30
print "  Importing utils modules"
script_dir_to_import("local")
script_dir_to_import("utils")
import cameraUtils as camu
import geo_utils as geou
import ipp as ipp
import customPlayblast as custPlay
print "  Finished."
print "--" * 30

#import maya.OpenMayaUI as apiUI
#from PyQt4 import QtGui, QtCore
#from qtUtils import *
