### PYTHON in Houdini

## Links interesantes:   

https://www.tokeru.com/cgwiki/index.php?title=HoudiniPython   
https://github.com/kiryha/Houdini/wiki/Python-for-artists   
https://ikrima.dev/houdini/basics/hou-python/#get-houdini-environment-variable   

Para acceder a las fuciones de Houdini en python, se utiliza la libreria "HOU".
```Python
import hou
```
A partir de aquí tenemos acceso a las funciones de Houdini en Python. Ejemplos:
```Python
# que nodos hay seleccionados
hou.selectedNodes()
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
```

