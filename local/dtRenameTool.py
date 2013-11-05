'''
from maya.cmds import window, ls, button, showWindow, nameField, columnLayout

windowName = window(t="Rename Tool")
columnLayout(adj=1)
selected = ls(sl=True)
for s in selected:
	nameField(o=s)
close_command = "deleteUI -window " + windowName
button(l="Close", c=close_command)
showWindow(windowName)
'''
