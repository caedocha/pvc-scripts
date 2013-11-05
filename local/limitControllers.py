"""
--------------------------------------------------------------------------------------------------------------------
limitControllers.py - Python Script
--------------------------------------------------------------------------------------------------------------------
Copyright 2012 Carlos Chacon L. All rights reserved.

DESCRIPTION:
Limit the translation of objs, useful to build UI controllers.

USAGE:
*Select objs to limit
*Run the script

AUTHOR:
Carlos Chacon L. (caedo.00 at gmail dot com)
--------------------------------------------------------------------------------------------------------------------
"""

import maya.cmds as cmds

def limitControllers(objs, limits):
	for o in objs:
		cmds.transformLimits(o, etx=(1,1), tx=(limits["x"][0], limits["x"][1]))
		cmds.transformLimits(o, ety=(1,1), ty=(limits["y"][0], limits["y"][1]))
		cmds.transformLimits(o, etz=(1,1), tz=(limits["z"][0], limits["z"][1]))

sel = cmds.ls(sl=True)
limits ={} 
limits["x"] = [-1,1]
limits["y"] = [-1,1]
limits["z"] = [0,0]
if(len(sel) > 0):
	limitControllers(sel, limits)
else:
	cmds.error("Please select at least one object.")
