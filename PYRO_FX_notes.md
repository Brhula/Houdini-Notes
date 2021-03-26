## PYRO FX NOTES

### WORKFLOW tipico:   

Particles -> convert to vdb -> smoke solver -> add disturbance


- **TEMPERATURE DIFFUSION** : Hace que el gas se expanda mmas o menos. Mayor numero, mayor difusion / expansion   
- **COOLING RATE** : Baja la temperatura.   
   - Valor alto --> Temperatura mas baja   
   - Valor bajo --> Temperatura mas alta    
- **DISSIPATION** : [0-1]como de rapido desaparece es gas. Numeros mas altos hacen desaparecer mas rapido.   
- **DISTURBANCE** : Anyade ruido blanco a la simulcaion, para romper uniformidad. Sirve para romper "mushrooms". Demasiado y sera muy evidente.   

### MICROSOLVERS:   
- **DISTURBANCE** : 

### COLISIONES con PYRO:   
**Utilzar VDB para el calculo de colisiones**   
- utilizar "VDB from polygon" SOP con "distance VDB" y una resolucion suficiente para que no tenga agujeros.   
- En DOPs, usar nodo "static object", y:   
   - Poner en "SOP Path" el VDB de SOP
   - "Collision detection" en "Use volume collision"
   - y en "Volume"-->"Mode"  poner "Volume sample"
   - en "Proxy volume" hacer que apunte tambien al VDB del SOP.
- Conectar el "static object" al "merge" despues del Pyro Solver.   

El Pyro ahora deberia colisionar con el objeto SOP.

**Si el humo pasa a traves del objeto de colision**   

Esto no siempre es necesario. Solo si atraviesa. En general deberia funcionar bien.   
Bajar el "Time Scale" (a 0.5 o 0.25) para que detecte mejor las colisiones.   
Subir los sub-steps del DOP no parece funcionar muy bien.   
Luego, para hacer la cache, poner un TimeWarp para recuperar velocidad original.   


### QUE HACER PARA:   
- **ELIMINAR "MUSHROMS"**: Utilizar el micro-solver de "disturbance" para romper las bolas tipo "champinon" (mushrooms). Se pueden incorporar varios micro-solvers de "disturbance" con diferente "block-size" (en unidade Houdini) para romper los "mushrooms" a diferentes tanaños. Un caso tipico seria poner 3 micro-solvers con un block-size de (0.3 , 0.1 y 0.033).   
