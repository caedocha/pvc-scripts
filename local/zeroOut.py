from maya.cmds import listRelatives, ls, getAttr, setAttr, objExists,group,parent,nodeType


def zeroOut(objs):
	zero_outs = list()
	for o in objs:
		if(isTransformNode(o)):
			group_name = "grp_" + o
			obj_parent = listRelatives(o, p=True)
			if objExists(group_name):
				group_name = group_name + "1"
			group_obj = group(em=True,w=True, n=group_name)
			if obj_parent is not None:
				parent(group_obj, obj_parent)
			setReceiverWithSender(o, group_obj)
			parent(o, group_obj)
			setAttrToValue(o,"r")
			setAttrToValue(o,"t")
			zero_outs.append(group_name)
	return zero_outs

def isTransformNode(obj):
	"""
	Checks if the obj is a transform node
	"""
	return (nodeType(obj) == "transform")

def setReceiverWithSender(sender, receiver):
	"""
	Sets the attrs of the receiver with the values of the sender obj.
	"""
	rotate_attrs = getAttr(sender + ".r")[0]
	translate_attrs = getAttr(sender + ".t")[0]
	setAttr(receiver+".r", rotate_attrs[0], rotate_attrs[1], rotate_attrs[2], type="double3")
	setAttr(receiver+".t", translate_attrs[0], translate_attrs[1],translate_attrs[2], type="double3")

def setAttrToValue(obj, attr, value=0):
	"""
	Sets a complex attr, like translation or rotation, to a value.
	Value's default is 0
	"""
	setAttr(obj+"."+attr, 0, 0, 0, type="double3")
