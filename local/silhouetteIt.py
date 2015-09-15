import maya.cmds as cmds

silhouette_flag = False
object_sgs = {}
background_color = list()

def shaderNodeExists(shader):
	"""
	Checks if a shader exists, only for readability reasons.
	"""
	return cmds.objExists(shader)

def createSurfaceShader(shader_name, shader_group_name):
	"""
	Creates the shader used by the influence spheres of the slave objects.
	"""
	shader = cmds.shadingNode("surfaceShader", asShader=True, name=shader_name)
	cmds.setAttr(shader+".outColor",0,0,0, type="double3" )
	cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shader_group_name)
	cmds.connectAttr(shader+".outColor", shader_group_name+".surfaceShader")

def connectSGToObj(shader_group,obj):
	cmds.sets(obj, edit=True, forceElement=shader_group)

def silhouetteIt():
	global background_color,silhouette_flag,object_sgs
	print silhouette_flag
	print object_sgs
	print background_color
	shapes = cmds.ls(g=True,v=True)
	filtered_shapes = filter(lambda o: (cmds.nodeType(o)=="mesh"), shapes)
	for s in filtered_shapes:
		if(silhouette_flag):
			shape_sg = object_sgs[s]
			connectSGToObj(shape_sg,s)
		else:
			obj_sg = cmds.listConnections(s, type="shadingEngine")[0]
			object_sgs[s] = obj_sg
			if(not shaderNodeExists("silhouetteShader")):
				createSurfaceShader("silhouetteShader","silhouetteShaderSG")
			connectSGToObj("silhouetteShaderSG",s)

	if(silhouette_flag):
		cmds.displayRGBColor("background",background_color[0],background_color[1],background_color[2])
		silhouette_flag=False
	else:
		background_color = cmds.displayRGBColor("background",q=True)
		cmds.displayRGBColor("background",1,1,1)
		silhouette_flag=True
	print silhouette_flag

silhouetteIt()
