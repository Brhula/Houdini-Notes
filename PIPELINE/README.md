**PIPELINE STUFF**   

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

***PACKAGES***   

En "packages" la entrada "hpath" se refiere en realidad a "$HOUDINI_PATH". Para referirse a "$PATH" se utiliza "PATH".

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
