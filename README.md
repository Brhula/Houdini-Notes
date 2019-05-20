### Houdini VEX  Snippets

Colección de "snippets" (trozos de código) para realizar funciones concretas. Se aplica a "wranglers" (nodos específicos de Houdini para albergar código VEX), o bien a otros nodos.

**Eliminar primer y ultimo punto de una primitiva (típicamente curvas)**
```C#
//set a wrangle to run over primitives
int primpts[] = primpoints(0,@primnum);
removepoint(0,primpts[0]);
removepoint(0,primpts[-1]);
```


