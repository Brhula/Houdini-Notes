import hou

# Create Camera - 1080
def create_camera():
  node = hou.node("/obj").createNode("cam", "camera")
  node.setParms({"resx": 4096, "resy": 2160})
  node.setDisplayFlag(False)

# Create Mantra - PBR driver
def mantra_driver():
  node = hou.node("/out")
  out = node.createNode("ifd")
  out.setParms({"vm_renderengine": "pbrraytrace", "override_camerares": True, "camera": "/obj/cam_1080"})

def main():
  create_camera()
  mantra_driver()


# set scene frame start, end and fps 
start = 1000
end = 1100
fps = 24.0

hou.setFps(fps)
# send to HSCRIPT
hou.hscript( "tset " + str((start-1)/fps) + " " + str((end)/fps) )
hou.playbar.setPlaybackRange(start,end)
hou.playbar.setFrameRange(start,end)
hou.setFrame(start)
main()