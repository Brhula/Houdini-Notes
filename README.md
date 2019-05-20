### Houdini VEX  Snippets

Colección de "snippets" (trozos de código) para realizar funciones concretas. Se aplica a "wranglers" (nodos específicos de Houdini para albergar código VEX), o bien a otros nodos.

**Eliminar primer y ultimo punto de una primitiva (típicamente curvas)**
```C#
// Delete first and last curve points
//set a wrangle to run over primitives
int primpts[] = primpoints(0,@primnum);
removepoint(0,primpts[0]);
removepoint(0,primpts[-1]);
```
**Borrar puntos de forma aleatoria según una tolerancia** 
```C#
// This snippet will delete random points based on the threshold slider
// set a wrangle to run over points
if ( rand(@ptnum) > ch('threshold') ) {
   removepoint(0,@ptnum);
}
```
**Centrar el pivot y mover al origen de coordenadas** 
```C#
//  Center Pivot and Move to Origin
// set a wrangle to run over points
vector centroid = getbbox_center(0);
vector dist = centroid - 0;
v@P -= dist;
```
**Normales aleatorias en los puntos** 
```C#
// Random normals
// set a wrangle to run over points
v@N=set(fit01(rand(@ptnum),-1,1),fit01(rand(@ptnum+1),-1,1),fit01(rand(@ptnum+2),-1,1));
```
**Tamaño aleatorio de los puntos, dando maximo, minimo y semilla** 
```C#
// SOP Random pscale with Ramp, Seed, Min and Max
// change @ptnum for @id in POPs
// set a wrangle to run over points
@pscale = fit01(chramp("Width", rand(@ptnum  + ch("Seed"))), ch("Min"), ch("Max"));
```
**Rotación aleatoria en puntos, ajustada mediante una rampa.**
Borrar v@up en caso que ya exista.
```C#
// SOP Random Rotation Wrangle
// if v@up exists, delete first line
// set a wrangle to run over points
v@up = {0.0, 1.0, 0.0};
float angle = ch("rot_amount");
float rand = fit01(random(@ptnum+311),0,angle);
p@rot = quaternion(radians(rand), v@up);
```
