import maya.cmds as cmds

sel = cmds.ls(sl=True,flatten=True)
for s in sel:
    cmds.cluster(s)