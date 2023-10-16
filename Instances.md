###  ATRIBUTOS para Copy e Instance

Al copiar e instanciar, Houdini comprueba la existencia de los siguientes  atributos asociados a los puntos.

```C++
p@orient                    // Orientacion (Quaternion).
f@pscale                    // Escala uniforme.
v@scale                     // Escala.
v@N                         // Normal (eje +Z en la copia si no hay p@orient).
v@up                        // Vector Up (eje +Y en la copia si no hay p@orient).
v@v                         // Velocidad (motion blur), Utiliza el eje +Z si no hay  p@orient o v@N.
p@rot                       // Rotacion adicional (aplicada despues de la rotacion anterior).
v@P                         // Posicion en el espacio de la copia.
v@trans                     // Translacion adicional a v@P.
v@pivot                     // Local pivot point.
3@transform or 4@transform  // Transform matrix overriding everything except v@P, v@pivot, and v@trans.
s@shop_materialpath         // The instanced object uses this material.
s@material_override         // A serialized Python dictionary mapping material parameter names to values.
s@instance                  // Objeto (SOP node) dentro de la escene a instanciar
s@instancefile              // File path indicando la geometria a instanciar.
s@instancepath              // Geometria a instanciar. "Path" a fichero o un "op: path" a la escena.
```

### EJEMPLOS de instancias y "copy" de objetos

Copiar instancias a puntos de objetos en memoria (SOP node):
```C++
s@instance = sprintf("/obj/SOP_node");
```
Funciona también en sub-networs de nodos.   
Un ejemplo de asignación aleatoria de nodos dentro de una sub-network que se llama "TREES_subnet", en donde los nodos se llaman "Tree_01", "Tree_02", ...,"Tree_16".   

```C++
i@frame = floor(rand(@ptnum+1579)*10+1);
if (@frame < 10) {
    s@instance = sprintf("/obj/TREES_subnet/Tree_0%d", @frame);
    }
else {
    s@instance = sprintf("/obj/TREES_subnet/Tree_%d", @frame);
}

```
### ORIENTACION

Con "quaternions". En este caso, manual, excepto "yaw" que es automatica en 360 grados (2 * PI radianes)

```C++
@orient = quaternion(maketransform(normalize(-@P),{0,1,0}));

vector4 pitch = quaternion({1,0,0}*ch('pitch'));
vector4 yaw   = quaternion({0,1,0}*(rand(@ptnum) * 3.14 * 2.0));
// vector4 yaw   = quaternion({0,1,0}*ch('yaw'));
vector4 roll  = quaternion({0,0,1}*ch('roll'));

@orient = qmultiply(@orient, pitch);
@orient = qmultiply(@orient, yaw);
@orient = qmultiply(@orient, roll);

```
Receta general con "quaternions"
```C++
float angle = rand(@ptnum) * 360; // Angulo random
angle = radians(angle); // convertimos a radianes

// vector axis = @N; // axis orientada a la normal a la superficie: 
vector axis = {0,1,0}; // axis es el eje de las Y.
matrix3 m = ident(); // Matriz identidad
 
rotate(m, angle, axis); // Calcula la matriz de rotacion al rotar "angle" respecto al eje "axis".
 
@orient = quaternion(m);

```
Orientamos todos los puntos hacia el {0,0,0}
```C++
// matrix3  maketransform(vector zaxis, vector yaxis)
@orient = quaternion(maketransform(normalize(-@P),{0,1,0}));
```

### Documentación adicional

[Point Instance procedural](https://www.sidefx.com/docs/houdini/nodes/vop/ptinstance.html)   
[Optimize copies - stamping or not](https://forums.odforce.net/topic/25971-optimize-copies-stamping-or-not-solved/?page=2&tab=comments#comment-151013)   
