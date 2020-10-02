
### ALEMBIC exports to Maya

Alembic "need to know" things:   
- Pack Geometry for every group of primitives before exporting. Every paked geo will appear as a Maya "shape" node.   
- Name of last node in Houdini before "ROP Alembic" node will appear as the root transform in Maya.

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
