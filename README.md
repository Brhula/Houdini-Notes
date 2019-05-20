### Houdini VEX  Snippets

Colección de "snippets" (trozos de código) para realizar funciones concretas

#### Eliminar primer y ultimo punto de una primitiva (típicamente curvas)
```C++
//set a wrangle to run over primitives
int primpts[] = primpoints(0,@primnum);
removepoint(0,primpts[0]);
removepoint(0,primpts[-1]);
```

Salida
