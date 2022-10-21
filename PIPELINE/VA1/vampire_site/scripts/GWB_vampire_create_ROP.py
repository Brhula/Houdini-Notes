'''
GW Barcelona // Proyecto Vampire
Crear nodos ROP para Mantra / Arnold / Redshift con los settings basicos preparados
'''
import hou
from PySide2 import QtCore, QtUiTools, QtWidgets

''' USER INTERFACE from QT Designer'''
class GeoCreator(QtWidgets.QWidget):
    def __init__(self):
        super(GeoCreator,self).__init__()
        ui_file = hou.getenv("VAMPIRE_PACKAGE")+"/scripts/GWB_vampire_create_ROP.ui"
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)

        self.ui.ArnoldButton.clicked.connect(self.clickArnold)
        self.ui.MantraButton.clicked.connect(self.clickMantra)
        self.ui.RedshiftButton.clicked.connect(self.clickRedshift)
        self.ui.DeadlineButton.clicked.connect(self.clickDeadline)
    def clickArnold(self): 
        print("Arnold!")
        out = hou.node("/out").createNode("arnold")
        out.setParms({"ar_picture": "$JOB/renders/fx/$HIPNAME/$HIPNAME:r.$OS.$F4.exr"})
        out.setParms({"trange" : 1 })
    def clickMantra(self):
        print("Mantra!")
        node = hou.node("/out")
        out = node.createNode("ifd")
        out.setParms({"vm_renderengine": "pbrraytrace", "override_camerares": True})
        out.setParms({"vm_picture": "$JOB/renders/fx/$HIPNAME/$HIPNAME.$OS.$F4.exr"})
        out.setParms({"trange" : 1 })
    def clickRedshift(self):
        print("Redshift!")
        node = hou.node("/out")
        out = node.createNode("Redshift_ROP", "RS_render")
        out.setParms({"RS_overrideCameraRes": True})
        out.setParms({"RS_outputFileNamePrefix": "$JOB/renders/fx/$HIPNAME/$HIPNAME.$OS.$F.bgeo.sc"})
        out.setParms({"trange" : 1 })
    def clickDeadline(self):
        print("Deadline!")
        node = hou.node("/out")
        out = node.createNode("deadline", "Deadline")
        out.setParms({"dl_department": "Vampire Academy"})        

win = GeoCreator()
win.show()
