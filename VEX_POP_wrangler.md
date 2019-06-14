### POP Wrangler  

Para utilizar en el nodo "POP Wrangler" dentro de simulaciones de particulas/fluidos.   

**POP WRANGLER // Point gravity**   
Crear una fuerza que atrae hacia un punto en el espacio.   
Se puede utilizar para hacer el efecto "gravedad planetaria".
```C#
// Velocity to attract from point position to a point (here {0,0.5,0})
@v += -normalize(@P - {0,0.5,0}) * chf("amount");
```




