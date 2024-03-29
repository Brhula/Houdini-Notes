## FLIP SOP solver notes and workflow

`rgb(9, 105, 218)`

Notas sobre el flujo de trabajo (workflow) para el FLIP SOP solver y demás componentes (como espuma, surfacing, etc.).

Típicamente:
- Hacer una simulación "Flip" (partículas) de las partes que chocan, emergen, se deslizan, etc... Todo lo que tenga movimiento.
- "Meshing" o "surfacing" es convertir los puntitos en una superficie poligonal (típicamnete)
- Calculo del "white water" para poner encima del "mesh", es decir, una simulación de particulas que genera la espuma, burbujas y demás componentes del efecto.
- Oceano, si hace falta, se mezcla con un oceano para integrarlo en aguas abiertas. Esto no es simulación.

### LINKs INTERESANTES:   


[Añadir espuma (white water)](https://www.youtube.com/watch?v=L-o0SEijZ7U)


### FLUJO CLASICO PARA TRABAJAR:   

- nodo `Flip Container` o "Flip Tank": preparamos la "caja contenedora" o "domain" donde se calcula el FLIP. Aquí indocamos también la RESOLUCIÓN del FLIP.
- nodo `Flip Collide`: Aquí metemos todos los objetos con los que choca el FLIP. Pueden estar animados.
- nodo `Flip Solver`: Pues eso, donde se hacen los cálculos.
- nodo `Fluid Compress` : Suele utilizarse para comprimir la info del `Flip Solver` y suele seguirse de una caché para grabar en disco.
- nodo `White water Source`: donde se prepara un VDB desde donde se emitirá la espuma, burbujas, porquería flotante...
- nodo `White Water Solver` : Aquí se hace el cálculo de espuma, burbujas y demás.
- nodo `White water postprocess` : Preparamos particulas de espuma para hace render. Como puntos, VDB o mesh. También puede "chafar" las particulas fuera del area de "interes".

### PREPARAR LOS ELEMENTOS PARA SIMULAR:   

#### `NODO // FLIP TANK`   

Este nodo indica el "domain" del fluido, el espacio donde se simula.   

- "particle separation": indican cuantas particulas por unidad de Houdini indicandolo por la distancia entre ellas. Las simulaciones varian según el numero de particulas que tienen, no es lo mismo una simulación con un `paricle separation` de 0.1 que de 0.04. Las físicas se comportan distinto. Pôr eso es importante:    
  - Que fijemos un `particle separation` que funcione bien desde el principio.
  - Si la simulación es muy lenta, mejor ponemos un "domain" que solo pille un trozo y así vemos que tal el comportamiento básico. Al poner luego el "domain" completo no tendremos sorpresas en cuanto al comportamiento.   
- Vigilar que tenga activado "vorticity" si queremos hacer espuma (white water)
- Si le enchufamos un objeto, el "domain" no será un cubo, si no tendrá la forma del objeto. Se puede animar (baquitos moviendose, por ejemplo)

#### `NODO // FLIP COLLIDE`   

Colisiones (animadas también) con el fluido. Recipientes, rocas, etc.  Parámetros:
- Velocity scale: si lo ponemos a mas de 1 los objetos "empujan" con más fuerza el liquido al moverse. En objetos que "emergen" le da un poco más de espectacularidad.
- Desactivando el "Surface Collider" la SIM va mucho más rápida. Algunos "gurus" dicen que tambíen funciona mejor. La SIM cambia un poco, mirar que va mejor.

### `NODO // PARTICLE FLUID SURFACE` (crear un `mesh` de la simulación)   

Parametros:
- Influence scale : maxima distancia a la que las particulas interaccionan, es mutiplicador del "particle separation". Valor de habitual tipo 2. MAyor numero, mesh más suave y con menos detalles. Valor manor, mesh más definida y con más detalle.
- Droplet Scale: Tamaño de las gotita. Típico 0.75 (gotitas más finas)

### BEFORE START SIMULATION:   
**Check collision geometry**   
Uncheck "Display geometry" and check "Collision Guide" to see the shape of the objext.. Allways check size and shape of colliders, default values are usually terrible

**Check animation**   
- Deactivate ""brain"" to avoid simulations   
- uncheck ""integer frames values"" in animation preferences   
- Scrub timeline with substeps to check animation behaving"   

**Check "FLIP Object"**   
En "GUIDES" activar "Collision" y comprobar que tiene suficiente resolución. Si no, activar "Collision separation" y bajar el valor para que tenga el colisionador más resolución   
