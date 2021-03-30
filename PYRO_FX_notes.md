## PYRO FX NOTES

### WORKFLOW tipico:   

(1) Particles --> (2) convert to vdb --> (3) smoke/pyro solver --> (4) add disturbance
### (1) PARTICLES: 
- Normalmente se hace un set-up con un sistema de particulas para crear el "source" del pyro/smoke.
- La velocidad (v) así como la escala (pscale) influyen despues en como se comportara el solver. Es interesante que tengan variación (randomness)
- Típicamente empezaremos con  poca velocidad y escala, y progresivamente iremos aumentando. Si es una explosión, con pocos frames deberia funcionar.
### (2) PARTICLES to VOLUMES  (convert to VDB): 


### PARAMETROS INCLUIDOS EN EL SOLVER: 
- **TEMPERATURE DIFFUSION** : Hace que el gas se expanda mmas o menos. Mayor numero, mayor difusion / expansion   
- **COOLING RATE** : Baja la temperatura.   
   - Valor alto --> Temperatura mas baja   
   - Valor bajo --> Temperatura mas alta    
- **DISSIPATION** : [0-1]como de rapido desaparece es gas. Numeros mas altos hacen desaparecer mas rapido.   
- **DISTURBANCE** : Anyade ruido blanco a la simulcaion, para romper uniformidad. Sirve para romper "mushrooms". Demasiado y sera muy evidente.   

### MICROSOLVERS:   
- **DISTURBANCE (v2.0)** : Agrega detalles finos a una simulación de humo aplicando fuerzas de "perturbación" a la velocidad. Recomendado para romper "mushrooms". Es buena idea aplicar varios con diferentes parametros  (tipicamente "block-size").   
   - Strength : fuerza del efecto   
   - Threshold range : toma el input (densidad tipicamente) y lo remapea como 0-1 para multiplicarlo por "disturbance" (strength). Cualquier valor por encima de 0.05 no se vera afectado (valores con mayor densidad), cuanto más cerca de 0  más se vera afectado. Basicamente lo que hace es potenciar el efecto en los bordes del humo para conseguir más detalle.   
   
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
- **ELIMINAR "MUSHROMS"**: Utilizar el micro-solver de "disturbance" para romper las bolas tipo "champiñon" (mushrooms).
   -  Se pueden incorporar varios micro-solvers de "disturbance" con diferente "block-size" (que indican el tamaño del efecto, en unidade Houdini) para romper los "mushrooms" a diferentes tanaños. Un caso tipico seria poner 3 micro-solvers con un block-size de (0.3 , 0.1 y 0.033).   
   -  Si se necesita un efecto mas local, se puede hacer un "field" de mascara para limitarlo.   
   -  Tambien es interesante/posible animar el efecto para dar impulso al principio, y luego poner su influencia a cero para dejar que la simulación continue sin añadir velocidad adicional.
- **QUE UNA FUERZA/MICROSOLVER AFECTE SOLO A UNA ZONA:**   
   - Crear un objeto (SOP) y convertirlo a fog VDB y ponerle un nombre. Se utilizara el nombre como "mascara" para confinar el efecto.
   - En DOP (simulación) creamos un nodo "volume source" que apunte al objeto creado (de SOP), y como parametro "source volume" ponemos el nombre del fog VDB, y como "target" el nombre del nuevo campo que queramos utilizar (tipicamente el mismo). Se conecta a PYRO en la entrada SOURCING
   - En el micro-solver se pone el nombre del campo en el apartado "control field". Esto limitara el microsolver a la mascara.   
- **SIMULAR EL VIENTO SUAVE QUE MUEVE EL HUMO:**   
   - Incluir un nodo (o mas de uno) de "turbulence", con settings suaves para que mueva un poco el humo.   
   - Incorporar un nodo de "DRAG FORCE" a la simulacion, para que vaya frenando progresivamente las fuerzas que impulsaron originariamente el humo (un escape, explosion, etc.). Eso le da realismo al frenar el humo, y el "turbulence" se encarga de que no se quede completamente parado.
