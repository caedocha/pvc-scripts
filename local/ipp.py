import maya.cmds as cmds

def is_nurbs_curve(obj):
	return cmds.nodeType(obj) == "nurbsCurve"

def create_item(item_type,point):
	item = ""
	if item_type == "joint":
		item = cmds.joint()
	elif item_type == "locator":
		item = cmds.spaceLocator()[0]
	elif item_type == "cluster":
		item = cmds.cluster(point)[1]
	elif item_type == "cube":
		item = cmds.polyCube()[0]
	return item

def create_item_per_point(item_type):
	items = list()
	selection = cmds.ls(sl=True, flatten=True)
	cmds.select(cl=True)
	for point in selection:
		new_item = create_item(item_type,point)
		if is_nurbs_curve(point):
			temp_cluster = create_item("cluster", point)
			point_const = cmds.pointConstraint(temp_cluster,new_item)
			cmds.delete(temp_cluster,point_const)
		else:
			point_const = cmds.pointConstraint(point,new_item)
			cmds.delete(point_const)
		items.append(new_item)
	cmds.select(items)

def itemPerPointUI():
	ipp_window = cmds.window(w=100,h=100,title="Item Per Point",s=False,rtf=True)
	ipp_column_lay = cmds.columnLayout(p=ipp_window,w=100)
	ipp_cls_btn = cmds.iconTextButton(image="cluster.png",style="iconAndTextHorizontal",label="Cluster",p=ipp_column_lay,c="create_item_per_point('cluster')",bgc=(0.2,0.2,0.2),w=100,h=50, font="boldLabelFont")
	cmds.separator(p=ipp_column_lay)
	ipp_jnt_btn = cmds.iconTextButton(image="kinJoint.png",style="iconAndTextHorizontal",label="Joint",p=ipp_column_lay,c="create_item_per_point('joint')",bgc=(0.2,0.2,0.2),w=100,h=50, font="boldLabelFont")
	cmds.separator(p=ipp_column_lay)
	ipp_loc_btn = cmds.iconTextButton(image="locator.png",style="iconAndTextHorizontal",label="Locator",p=ipp_column_lay,c="create_item_per_point('locator')",bgc=(0.2,0.2,0.2),w=100,h=50, font="boldLabelFont")
	cmds.separator(p=ipp_column_lay)
	ipp_cube_btn = cmds.iconTextButton(image="polyCube.png",style="iconAndTextHorizontal",label="Polycube",p=ipp_column_lay,c="create_item_per_point('cube')",bgc=(0.2,0.2,0.2),w=100,h=50, font="boldLabelFont")
	cmds.showWindow(ipp_window)
