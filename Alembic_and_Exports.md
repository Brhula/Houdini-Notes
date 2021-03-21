
### ALEMBIC exports to Maya

https://medium.com/@jessicabeckenbach/exporting-alembic-files-from-houdini-using-the-path-attribute-ac9f34f5ab1

Alembic "need to know" things:   
- Pack Geometry for every group of primitives before exporting. Every paked geo will appear as a Maya "shape" node.   
- Name of last node in Houdini before "ROP Alembic" node will appear as the root transform in Maya.

### Exportar GEO con cambios de topologia a Maya   

Como por ejemplo exportar GEO con numero de puntos y caras animado como ALEMBIC (tipo boolenas animadas) o meshes FLIP.
El metodo es hacer un "stitch" fde la secuancia de alembics de salida:
- Generar secuencia de Alembics (tipo name.$F4.abc)
- Importar la secuencia  alembics de nuevo en Houdini
- Hacer un "unpack" y "attribute delete" (de lo no necesario)
- Grabar un nuevo alembic con el resultado en un solo fichero (stitch)


### MAYA MEL scripts to help   

**Change all objects selected for a new one inside Maya**   
   
```C++
// Substitute obects 

string $instance ="pCube13"; // Maya object to use as instance.

string $selection[] = `ls -sl`;
for ($each in $selection)
 {
    select -r $instance;
    $instance_copy = `instance`;
    pickWalk -d down;
    select -add $each;
    parent -r -s;
 }
```
