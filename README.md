### Houdini VEX  Snippets

```C++
//set a wrangle to run over primitives
int primpts[] = primpoints(0,@primnum);
removepoint(0,primpts[0]);
removepoint(0,primpts[-1]);
```

Salida
