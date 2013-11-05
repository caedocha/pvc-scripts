import maya.cmds as cmds

sel = cmds.ls(sl=True,flatten=True)
for s in sel:
    loc = cmds.spaceLocator()
    cls = cmds.cluster(s)
    const = cmds.pointConstraint(cls,loc)
    cmds.delete(const, cls)