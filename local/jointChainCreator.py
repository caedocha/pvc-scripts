from maya.cmds import spaceLocator, joint, parentConstraint, parent, duplicate, delete, select, rename, ls

def getConstraintNodes(node):
	"""
	Gets the constraint nodes of the specified node.
	"""
	return listRelatives(node, type="constraint")


def createJointsFromLocators(locators):
	""" 
	Creates a joint chain using the locators as a template		
	"""
	select(cl=True)
	joints = list()
	for loc in locators:
		j = joint()
		parent_constraint = parentConstraint(loc, j)
		delete(parent_constraint)		
		joints.append(j)
	return joints

def createLimbChains(locators, chains):
	"""
	Creates the specified chains of joints in the location specified by the locators
	The purpose of this script is to create the limb chains(ik, fk, bind) automaticlly. 
	"""
	for chain in chains:
		joints = createJointsFromLocators(locators)
		for i,j in enumerate(joints):
			rename(j, chain[i])
			 

locators = ls(sl=True)
#locators = ["loc1", "loc2", "loc3"]
ik_chain = ["ik_shoulder","ik_elbow", "ik_wrist"]
fk_chain = ["fk_shoulder","fk_elbow", "fk_wrist"]
bind_chain = ["bn_shoulder","bn_elbow", "bn_wrist"]
chains= [ik_chain, fk_chain, bind_chain]
if locators >0 :
	createLimbChains(locators, chains)
else:
	print "You must select the desired locators to create the joint chains."
