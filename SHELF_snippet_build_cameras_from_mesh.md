### Python snippet to use as SHELF tool   

Builds a camera on every point of a mesh and aims them  towar centroid of mesh.   
Used to make renders to simulate Gaussian Spatting.

Copy code to SHELF tool and execute.


```python
import hou

# 1. Get the selected node
selected_nodes = hou.selectedNodes()

if not selected_nodes:
    hou.ui.displayMessage("Please select a Geometry node first!")
else:
    target_geo_node = selected_nodes[0]
    obj_level = hou.node('/obj')
    
    # Create a parent Null to keep the network clean
    parent_null = hou.node('/obj/cam_container')
    if not parent_null:
        parent_null = obj_level.createNode('null', 'cam_container')
    
    display_node = target_geo_node.displayNode()
    if not display_node:
        hou.ui.displayMessage("The selected node has no display flag.")
    else:
        geometry = display_node.geometry()
        
        for point in geometry.points():
            pt_num = point.number()
            pos = point.position()
            
            # Get Normal (N), default to Z-forward if missing
            has_n = geometry.findPointAttrib("N") is not None
            z_axis = hou.Vector3(point.attribValue("N")).normalized() if has_n else hou.Vector3(0, 0, 1)

            # --- BUILD MATRIX MANUALLY ---
            temp_up = hou.Vector3(0, -1, 0)
            # If the normal is pointing almost straight up or down, shift temp_up to avoid errors
            if abs(z_axis.dot(temp_up)) > 0.99:
                temp_up = hou.Vector3(1, 0, 0)

            # Correct Cross Product Order for Upright Cameras:
            # 1. Right (X) = World Up x Forward (Z)
            x_axis = temp_up.cross(z_axis).normalized()
            # 2. True Up (Y) = Forward (Z) x Right (X)
            y_axis = z_axis.cross(x_axis).normalized()

            # Create the 4x4 matrix
            # Note: Houdini cameras look down -Z
            matrix_values = (
                x_axis[0],  x_axis[1],  x_axis[2],  0,
                y_axis[0],  y_axis[1],  y_axis[2],  0,
                -z_axis[0], -z_axis[1], -z_axis[2], 0, 
                pos[0],     pos[1],     pos[2],     1
            )
            matrix = hou.Matrix4(matrix_values)

            # Create Camera
            cam_name = f"cam_{pt_num}"
            existing = hou.node(f"/obj/{cam_name}")
            if existing:
                existing.destroy()
            
            cam = obj_level.createNode('cam', cam_name)
            # Change icon size here (0.2 is usually a good size for many cameras)
            cam.parm('iconscale').set(25)
            cam.parm('focal').set(50)
            cam.parm('resx').set(4096)
            cam.parm('resy').set(4096)
            cam.setFirstInput(parent_null) # Parent to the null
            
            # Apply the transform
            cam.setWorldTransform(matrix)
        
        print(f"Successfully created {len(geometry.points())} cameras under 'cam_container'.")
    parent_null.layoutChildren()

```
