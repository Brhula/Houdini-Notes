import hou
# set scene frame start, end and fps 
start = 1000
end = 1050
fps = 25.0

hou.setFps(fps)
# send to HSCRIPT
hou.hscript( "tset " + str((start-1)/fps) + " " + str((end)/fps) )
hou.playbar.setPlaybackRange(start,end)
hou.playbar.setFrameRange(start,end)
hou.setFrame(start)