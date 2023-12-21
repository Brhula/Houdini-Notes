## FLIP SOP solver notes and workflow

`rgb(9, 105, 218)`

Notas sobre el flujo de trabajo (workflow) para el FLIP SOP solver y demás componentes (como espuma, surfacing, etc.)

### LINKs INTERESANTES:   


[Añadir espuma (white water)](https://www.youtube.com/watch?v=L-o0SEijZ7U)


### PREPARAR LOS ELEMENTOS PARA SIMULAR:   

#### `NODO // FLIP TANK`   

Este nodo indica el "domain" del fluido, el espacio donde se simula.   

"particle separation": indican cuantas particulas por unidad de Houdini indicandolo por la distancia entre ellas. Las simulaciones varian según el numero de particulas que tienen, no es lo mismo una simulación con un `paricle separation` de 0.1 que de 0.04. Las físicas se comportan distinto. Pôr eso es importante:    
- Que fijemos un `particle separation` que funcione bien desde el principio.
- Si la simulación es muy lenta, mejor ponemos un "domain" que solo pille un trozo y así vemos que tal el comportamiento básico. Al poner luego el "domain" completo no tendremos sorpresas en cuanto al comportamiento.   


### SURFACING (crear un `mesh` de la simulación)   



### BEFORE START SIMULATION:   
**Check collision geometry**   
Uncheck "Display geometry" and check "Collision Guide" to see the shape of the objext.. Allways check size and shape of colliders, default values are usually terrible

**Check animation**   
- Deactivate ""brain"" to avoid simulations   
- uncheck ""integer frames values"" in animation preferences   
- Scrub timeline with substeps to check animation behaving"   

**Check "FLIP Object"**   
En "GUIDES" activar "Collision" y comprobar que tiene suficiente resolución. Si no, activar "Collision separation" y bajar el valor para que tenga el colisionador más resolución   
