
### ALEMBIC exports to Maya

https://medium.com/@jessicabeckenbach/exporting-alembic-files-from-houdini-using-the-path-attribute-ac9f34f5ab1

![Alt Text](https://i.pinimg.com/originals/bc/f9/2c/bcf92cbfaa5610387a6a9dd92f37de9b.gif)
![Alt Text](https://3.bp.blogspot.com/-dOwQHkdXIm8/W0wmWYkkW2I/AAAAAAABsHg/_Oh6UYu6vVAgb_a-91eFa5XKOUO7oBBpwCLcBGAs/s1600/Houdini%2BEngine%2Bfor%2BAutodesk%2BMaya%2Band%2B3ds%2BMax.png)
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
