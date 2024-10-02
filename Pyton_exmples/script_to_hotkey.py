'''
PLace this script on a Shelf and assign a keyboard shortcut to execute
Will build a node called "OUT" attached to selected node
'''
import hou


# Get selected nodes
nodes = hou.selectedNodes()

# Start undo group
with hou.undos.group("Make OUT null"):
    
    # Check that at least one node selected
    if( len(nodes) > 0 ):
        
        # Make new node
        for n in nodes:
            oldPos = n.position()
            parent = n.parent()
            newNode = parent.createNode("null")
            newNode.setPosition(hou.Vector2([oldPos[0], oldPos[1]-1]))
            newNode.setInput( 0, n, 0 )
            newNode.setName("OUT",unique_name=True)