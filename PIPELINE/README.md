## PIPELINE STUFF   

***INTERESTING LINKS***   

- Python hacks and stuff in [HouPy Wiki](https://www.houpywiki.com)

***ENVIROMENT VARIABLES***   

Variables típicamente en *HOUDINI.ENV*.   
(Ahora es ejor utilizar `packages`, explicados mas abajo.)
- `HOUDINI_PATH` : Este es el path a los directorios donde Houdini busca los ficheros de configuración [Más info en SideFx](https://www.sidefx.com/docs/houdini/basics/houdinipath.html).
- `PATH` : Este es el "system path" para que encuentre ejecutables.

***$HSITE***   

- Variable que permite buscar packages en red. Houdini ya busca por version del software.     
- `$HSITE/houdini‹major›.‹minor›/packages` (for example, $HSITE/houdini18.0/packages) IMPORTANTE SEGUIR ESTA NOMENCLATURA!   
- Se puede poner $HSITE apuntando a algun sitio en la red (por ejemplo en `Y:\houdini`) y con sub-directorios tipo houdini20.0, houdini20.5, etc. para que escanee segun la version cuales son los packages disponibles.   

***COMMAND LINE TOOLS***   
   
[Quicktip hconfig utility](https://houdinitricks.tumblr.com/post/122304825634/quicktip-hconfig-utility)   
Abre un shell que sirve para ver las variables y configuración.    
Lo arrancamos buscando "command line tools" en el buscador de Windows   

`hconfig -a` para que vuelque todas las variables en la consola.   
`hconfig -H HOUDINI_USER_PREF_DIR` para ayuda en una variable en particular   
`hconfig -ap` muestra el orden en el que busca los packages, coandos, path, etc.

***VARIABLES en el File Browser***   
Se deben añadir al fichero "jump.pref" que suele estar en la raíz de las preferencias.   
También se puede añadir en la raíiz de un "package".
Por ejemplo incorporar variables varias:   

```C#
$GWASSETS
$GWSHOTS
$GWJOB
$GWRENDER
$GWCACHE
$GWVDB
//sloth/3d_share/houdini/MOPS-master/examples/
//sloth/jobs/
```   

***STARTUP SCRIPTS***    
Houdini busca en los directorios de $HOUDINI_PATH los siguientes ficheros (si hay mas de uno en el path, ejecuta el primero que encuentra):   
- python2.7libs/pythonrc.py : Se ejecutan al arrancar Houdini   
- scripts/123.py : Se ejecuta con escenas vacias. Interesante para configurar antes cargar escenas.
- scripts/456.py : Se ejecuta al cargar una escena.   


***PACKAGES***   

En "packages" la entrada __"hpath"__ se refiere en realidad a __"$HOUDINI_PATH"__.   
Para referirse a __"$PATH"__ se utiliza __"PATH"__.

Estructura de directorios de los "Packages" (directorio // descripción):   
- desktop //  Desktops:  Contains .desk file(s).   
- otls // Digital assets: Contains HDA files along with OPlibraries files.
- python2.7libs python3.7libs // Python modules: Contains .py files. You are responsible to provide the python modules in the right platform folder. The system python path will be updated with the folder path.
- python_panels // Python panels: Contains .pypanel file(s).
- toolbar // Shelf tools: Contains .shelf file(s). The shelf tools are loaded but not active in a shelf set.
- viewer_states // Viewer states: Contains python states implementation files.
- viewer_handles // Viewer handles: Contains python handles implementation files.
  
Links interesantes sobre "packages":   
- [Houdini packages doc](https://www.sidefx.com/docs/houdini/ref/plugins.html)   
- [Toadstorm basic explanation of packages](https://www.toadstorm.com/blog/?p=722)   

Ejemplos:   
Buscar en el *path* de los packages un "pakage" en concreto, y cargarlo SOLO una vez (por si está repetido).   
```json
{
  "load_package_once": true,
  "path": "$HOUDINI_PACKAGE_PATH/nombre-del-paquete"
}
```
Ejemplo del package de GW:   
```json
{
	"path" : "$GW_TOOLS",
	"load_package_once": true,
	"enable" : true,
	"env" : [
		{"HOUDINI_OTLSCAN_PATH" :"$GW_TOOLS/otls/glassworks;$GW_TOOLS/otls/external;$GW_TOOLS/otls/experimental;@/otls"},
		{"GW_TOOLS" : "$HSITE/packages/gw_tools"}	
	]
}
```

***PYTHON***   

- Cambiar o crear una variable dentro de la escena (se puede ver y modificar en "EDIT-->ALIASES AND VARIABLES"):   
```python
import hou
# creamos una variable $CACHE visible en edit-->Variables
hou.hscript("set -g CACHE=//path/a/algun/sitio")
```   
- Recuperar una variable:   
```python
import hou
# recuperamos la variable $CACHE visible en edit-->Variables
variable_from_houdini=hou.getenv("CACHE")
```   


***MENUS***   

- La variable `HOUDINI_MENU_PATH` se lee de derecha a izquierda (!!).


***VS CODE // EDITOR EXTERNO***   
   
Para hacer que el editor de VS CODE entienda la libreria `"hou"`, editar "settings.json" en VScode (`">open settings.json"`) y anyadir (cambiando el path):   

```json
"python.analysis.extraPaths": [
	"C:\\Program Files\\Side Effects Software\\Houdini 19.5.303\\houdini\\python3.9libs",
	"C:\\Program Files\\Side Effects Software\\Houdini 19.5.303\\python39\\lib\\site-packages-forced"
]
```   
De esta fora no da error en el "package" "hou".
