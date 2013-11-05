import maya.cmds as cmds
import os
import re

cppercentage = "cppercentage"
cpname = "cpname"
cpincremental ="cpincremental"

def custom_playblast():
	global cppercentage, cpname, cpincremental
	current_project = cmds.workspace(rd=True,q=True)
	cppercentage_value = cmds.floatSliderGrp(cppercentage,q=True,v=True)
	cpname_value = cmds.textFieldGrp(cpname,q=True,tx=True)
	cpincremental_value = cmds.checkBox(cpincremental,q=True,v=True)

	if(cpincremental_value):
		file_name = cpname_value+"_"
		files = os.listdir(current_project)
		file_inc = 0
		for f in files:
			if(re.match(cpname_value+"_\d",f)):
				file_inc += 1
		file_name = file_name + str(file_inc)
		cmds.playblast( p=cppercentage_value, f=current_project+file_name, v=False )
	else:
		cmds.playblast( p=cppercentage_value, f=current_project+cpname_value, v=False,fo=True)

def custom_playblast_UI():
	global cppercentage,cpname,cpincremental
	cpwin = cmds.window(title="Custom Playblast",rtf=True)
	cplay = cmds.columnLayout(p=cpwin, w=300, h=200,cat=("left",10),rs=10)
	cmds.floatSliderGrp(cppercentage,p=cplay,label="Quality",w=280,min=0,max=100,value=50,step=1,field=True,cal=[1,"left"])
	cmds.textFieldGrp(cpname,p=cplay,h=50,label="File name",w=280,cal=[1,"left"])
	cmds.checkBox(cpincremental,p=cplay,l="Incremental Save",w=280,enable=True)
	cpplayblastbtn = cmds.button(p=cplay,h=50,w=280,l="Custom Playblast",c="custom_playblast()")
	cmds.showWindow(cpwin)