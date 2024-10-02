### PYTHON in Houdini

Estas notas están basadas en Houdini 19 funcionando con Python3.7   

## Links interesantes:   

[Tokeru Python](https://www.tokeru.com/cgwiki/index.php?title=HoudiniPython)   
[Python for Artists](https://github.com/kiryha/Houdini/wiki/Python-for-artists)   
[Interesting Python snippets](https://github.com/kiryha/Houdini/wiki/python-snippets)   

Para acceder a las fuciones de Houdini en python, se utiliza la libreria "HOU".
```Python
import hou
```
A partir de aquí tenemos acceso a las funciones de Houdini en Python. Ejemplos:
```Python
# que nodos hay seleccionados
hou.selectedNodes()
```
Activar / desactivar un nodo (bypass)
```Python
n = hou.node('/obj/geo1/font1')
n.bypass(1)   # node is now bypassed
n.bypass(0)   # node is now active
```

```Python
# obtener variables locales a la sesion de Houdini ($JOB,  $HIP, etc)
hou.text.expandString('$HIP')
# también sirve para pillar variables declaradas en la definición "json" de un "package"
# para poder acceder, por ejemplo, a la ubicación del package y utilizar ese path para localizar cosas
hou.text.expandString('$VAMPIRE_PACKAGE')
hou.text.expandString('$VAMPIRE_PACKAGE/scripts')
```
```Python
# obtener variables de Windows validas a la sesion de Houdini (PATH, HOUDINI_PATH, etc.)
hou.getenv("HOUDINI_PATH") 
```
## INSTALAR librerias/packages  externos:   

Para instalar de forma permanente una libreria/package de Python en una versión de Houdini   
Abrimos un windows shell externo (desde Houdini podemos hacer windows-->shell).    

Cargamos PIP en houdini (lo ponemos en un directorio temporal antes de instalar)   
```console
curl https://bootstrap.pypa.io/get-pip.py -o D:/EXAMPLE/get-pip.py
hython D:/EXAMPLE/get-pip.py
```
Y ya podemos instalar el modulo por su nombre. Por ejemplo scipy
```console
- hython -m pip install XXXXXXX
```   

## UI STUFF:   
Mensaje directo simple:   
```Python
# Mostrar un mensaje en una ventana (bloquea houdini hasta que la cerramos)
hou.ui.displayMessage("run! Forrest run! ")
hou.ui.displayMessage('Hello', buttons=('OK','NO',)) 
```
Muestra texto en la barra inferior de información   
```Python
hou.ui.setStatusMessage("Working on it!")
```
Seleccionar elemento de una lista   
```Python
list = ["first","second","and third"]
hou.ui.selectFromList(list, message='Select Parms to bake key')
```
Seleccionar un fichero (abre un "browser")   
```Python
file = hou.ui.selectFile()
```
Seleccionar un nodo (abre un selector "outliner")   
```Python
hou.ui.selectNode()
hou.ui.selectNode(initial_node=hou.node('/obj/torus1')) # abre el selector con "torus1" del contexto /obj seleccionado 
```

