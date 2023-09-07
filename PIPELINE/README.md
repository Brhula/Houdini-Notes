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

- [Houdini packages doc](https://www.sidefx.com/docs/houdini/ref/plugins.html)   
- [Toadstorm basic explanation of packages](https://www.toadstorm.com/blog/?p=722)   
