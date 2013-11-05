import maya.cmds as cmds
import iterUtils as itu


def camera_type(camera):
	cam_orth = cmds.camera(camera,q=True,o=True)
	if(cam_orth):
		return "orthographic"
	else:
		return "perspective"

def switch_persp_panel():
	current_model = cmds.getPanel(wf=True)
	current_camera = cmds.modelEditor(current_model,q=True,cam=True)
	persp_cameras = cmds.listCameras(p=True)
	print persp_cameras
	try:
		if(camera_type(current_camera) == "orthographic"):
			cmds.lookThru("persp")
		else:
			if(len(persp_cameras) > 1):
				for c,n in itu.pairwise(persp_cameras):
					if(current_camera == c):
						if(persp_cameras.index(c) == (len(persp_cameras)-1)):
							cmds.lookThru(persp_cameras[0])
						else:	
							print n
							cmds.lookThru(n)
	except:
		print "No persp camera, create a new persp camera!"

def cycle_panel_focus():
	"""
	TODO:Aun no se como poner en frente un panel
	"""
	current_panel = cmds.getPanel(wf=True)
	visible_panels = cmds.getPanel(vis=True)

