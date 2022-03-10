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
# variables locales a la sesion de Houdini ($JOB,  $HIP, etc)
hou.text.expandString('$HIP')
```
