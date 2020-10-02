
### ALEMBIC

Alembic "need to know" things:   
- Pack Geometry before exporting to send a Maya Shape node   
- Last node in Houdini befor 

### MAYA MEL scripts to help   

**Change all objects selected for a new one inside Maya**   
This helps 
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
