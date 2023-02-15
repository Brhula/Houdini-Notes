
### Declaración de atributos

Al declarar atributos se pueden inicializar con una constante:
```C++
float @mass = 1;
vector @up = {0, 1, 0};
```
Esto es util por dos motivos:
- Damos un valor por defecto al atributo: si el atributo existe (por ejemplo, @mass), la asignación se ignora. Si no existe, se inicializa.
- Al especificar el tipo de atributo así, Vex ya entiende que tipo es. despues se puede utilizar simplemente @up en vez de v@up.

Al declarar atributos, a la derecha del `=` no puede haber calculos, solo constantes o literales:
```C++
float @mass = 1 / area;  // Error
vector @up = set(0, 1, 0);  // Error
```

hijack from http://mrkunz.com/blog/08_22_2018_VEX_Wrangle_Cheat_Sheet.html   
       new link https://wiki.johnkunz.com/index.php?title=VEX_Attribute_Glossary   

### Common Geometry Attributes

**Global Variables // A list of variables available in wrangles.**    
```C++
// Available in all SOP wrangles
f@Frame     //The current floating frame number, equivalent to the $FF Hscript variable
f@Time      //The current time in seconds, equivalent to the $T Hscript variable
i@SimFrame  //The integer simulation timestep number ($SF), only present in DOP contexts.
f@SimTime   //The simulation time in seconds ($ST), only present in DOP contexts.
f@TimeInc   //The timestep currently being used for simulation or playback.

// Available in Attribute Wrangle
v@P         //The position of the current element.
i@ptnum     //The point number attached to the currently processed element.
i@vtxnum    //The linear number of the currently processed vertex.
i@primnum   //The primitive number attached to the currently processed element.
i@elemnum   //The index number of the currently processed element.
i@numpt     //The total number of points in the geometry.
i@numvtx    //The number of vertices in the primitive of the currently processed element.
i@numprim   //The total number of primitives in the geometry.
i@numelem   //The total number of elements being processed.

// Available in Volume Wrangle
v@P                     //The position of the current voxel.
f@density               //The value of the density field at the current voxel location.
v@center                //The center of the current volume.
v@dPdx, v@dPdy, v@dPdz  //These vectors store the change in P that occurs in the x, y, and z voxel indices.
i@ix, i@iy, i@iz        //Voxel indices. For dense volumes (non-VDB) these range from 0 to resolution-1.
i@resx, i@resy, i@resz  //The resolution of the current volume.
```

**Frequently used attributes. Houdini knows to cast these to the appropriate VEX datatype.**
```C++
// Int
@id         // A unique number that remains the same throughout a simulation.

// Float
@pscale     // Particle radius size.  Uniform scale.  Set display particles as 'Discs' to visualize.
@width      // Thickness of curves.  Enable 'Shade Open Curves In Viewport' on the object node to visualize.
@Alpha      // Alpha transparency override.  The viewport uses this to set the alpha of OpenGL geometry.
@Pw         // Spline weight.

// Vector3
@P          // Point position.  Used this to lay out points in 3D space.
@Cd         // Diffuse color override.  The viewport uses this to color OpenGL geometry.
@N          // Surface or curve normal.  Houdini will compute the normal if this attribute does not exist.
@scale      // Vector scale.  Allows directional scaling or stretching (in one direction).
@rest       // Used by procedural patterns and textures to stick on deforming and animated surfaces.
@up         // Up vector.  The up direction for local space, typically (0, 1, 0).
@uv         // UV texture coordinates for this point/vertex.
@v          // Point velocity.  The direction and speed of movement in units per second.

// Vector4
@orient     // The local orientation of the point (represented as a quaternion).
@rot        // Additional rotation to be applied after orient, N, and up attributes.

// String
@name       // A unique name identifying which primitives belong to which piece.  Also used to label volumes.
@instance   // Path of an object node to be instanced at render time.
```
