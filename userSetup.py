import sys
import os
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

def script_dir_to_import(scriptDir):
	scriptPath = os.path.join(cmds.internalVar(usd = True), scriptDir)
	sys.path.append(scriptPath)

script_dir_to_import("pvc_scripts/local")
script_dir_to_import("pvc_scripts/utils")

import ipp
import cameraUtils as camu
import geo_utils as geou
import customPlayblast as custPlay
