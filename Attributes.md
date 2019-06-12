Al declarar atributos, a la derecha del `=` no puede haber calculos, solo constantes o literales.

hijack from http://mrkunz.com/blog/08_22_2018_VEX_Wrangle_Cheat_Sheet.html

### Common Geometry Attributes

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
