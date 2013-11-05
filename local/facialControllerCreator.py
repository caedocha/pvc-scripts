limits = {
	"fourSided":{
		"x":[-1,1],
		"y":[-1,1],
		"z":[0,0]
	},
	"twoSidedX":{
		"x":[-1,1],
		"y":[0,0],
		"z":[0,0]
	},
	"twoSidedY":{
		"x":[0,0],
		"y":[-1,1],
		"z":[0,0]
	},
	"threeSided":{
		"x":[-1,1],
		"y":[-1,0],
		"z":[0,0]
	}
}

def limitControllers(objs, limits):
	for o in objs:
		cmds.transformLimits(o, etx=(1,1), tx=(limits["x"][0], limits["x"][1]))
		cmds.transformLimits(o, ety=(1,1), ty=(limits["y"][0], limits["y"][1]))
		cmds.transformLimits(o, etz=(1,1), tz=(limits["z"][0], limits["z"][1]))

def createBoundingBox(controller_type):
	bounding_box =""
	crv = ""
	if(controller_type=="fourSided"):
		crv = mel.eval("curve -d 1 -p -1 1 0 -p 1 1 0 -p 1 -1 0 -p -1 -1 0 -p -1 1 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;")
	elif(controller_type=="twoSidedX"):
		crv = mel.eval("curve  -d 1 -p -1 1 0 -p 1 1 0 -p 1 -1 0 -p -1 -1 0 -p -1 1 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;")
		cmds.scale(1,0.1,0,crv)
	elif(controller_type=="twoSidedY"):
		crv = mel.eval("curve  -d 1 -p -1 1 0 -p 1 1 0 -p 1 -1 0 -p -1 -1 0 -p -1 1 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;")
		cmds.scale(0.1,1,0,crv)
	elif(controller_type=="threeSided"):
		crv = mel.eval("curve  -d 1 -p -1 0 0 -p 1 0 0 -p 1 -1 0 -p -1 -1 0 -p -1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;")
	print bounding_box, crv, controller_type+"BoundingBox"
	bounding_box = cmds.rename(crv, controller_type+"BoundingBox")
	cmds.makeIdentity(bounding_box,apply=True)
	cmds.setAttr(bounding_box+".overrideEnabled",1)
	cmds.setAttr(bounding_box+".overrideDisplayType",2)
	return bounding_box


def createController(controller_type):
	global limits
	controller = cmds.circle(n=controller_type,nrz=True)
	cmds.scale(0.1,0.1,0.1,controller)
	cmds.makeIdentity(controller,apply=True)
	limitControllers(controller,limits[controller_type])
	bounding_box = createBoundingBox(controller_type)
	cmds.group(controller,bounding_box,n="grp"+controller_type.title())
	
def facialControllerCreatorUI():
	win = "fccUIWin3"
	lay = "fccUILay"
	cmds.window(win,rtf=True,title="Facial Controller Creator")
	cmds.rowLayout(lay,numberOfColumns=4,p=win,w=320,h=80)
	cmds.symbolButton("fourSidedBtn",w=80,h=80,p=lay,image='fourSided.png',c="createController('fourSided')")
	cmds.symbolButton("twoSidedXBtn",w=80,h=80,p=lay,image='twoSidedX.png',c="createController('twoSidedX')")
	cmds.symbolButton("twoSidedYBtn",w=80,h=80,p=lay,image='twoSidedY.png',c="createController('twoSidedY')")
	cmds.symbolButton("threeBtn",w=80,h=80,p=lay,image='threeSided.png',c="createController('threeSided')")
	cmds.showWindow(win)

facialControllerCreatorUI()
