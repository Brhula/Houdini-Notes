### Houdini VEX  Snippets

Colección de "snippets" (trozos de código) para realizar funciones concretas. Se aplica a "wranglers" (nodos específicos de Houdini para albergar código VEX), o bien a otros nodos.

**Eliminar primer y ultimo punto de una primitiva (típicamente curvas)**
```C#
//set a wrangle to run over primitives
int primpts[] = primpoints(0,@primnum);
removepoint(0,primpts[0]);
removepoint(0,primpts[-1]);
```

**Borrar puntos de forma aleatoria según una tolerancia**
__This snippet will delete random points based on the threshold slider__
```C#
//set a wrangle to run over points
if ( rand(@ptnum) > ch('threshold') ) {
   removepoint(0,@ptnum);
}
```
