## PYRO FX H18.5 and UP   
El workflow ha cambiado un poco, al incluir algunas herramientas interesantes y unos presets en "SOPS" que permiten cosas complejas sin necesidad de entrar en "DOPS"     
   
**FUEL**: combustible a quemar. Para fuegos que estan quemando siempre necesita "regenerarse" (con "injection", por ejemplo)   
**TEMPERATURE**: Temperatura. A una determinada temperatura, el fuel hace combustion y da origen al "BURN".   
**BURN**: en donde actualmente esta quemando (burning)   
**TOTAL BURN**: lor que en algun momento se ha quemado   

### Workflow para la versión 18.5 y posteriores:   

### Notas para fuego:
- Necesitamos al menos "Temperature" y "burn". "Burn" se utiliza como emisor del fuego.
- Mejor dejar "density" para que haga un poco de "smoke". Se puede controlar en el shading.
- Desactivar "expansion" para que no haga "bolas de fuego" (como en las explosiones). en H19 Tab "Shape-->Flame Expansion.   
- Para hacer el shading, convertir el volument en VDB (ConvertVDB-->VDB). Es mucho más rápido de calculo.   

## PYRO SOURCE SPREAD   
![Alt text](images/PYRO_source_spread.jpg?raw=true "Title")   
- Vigilar el parametro "Fuel-->Injection Rate". Este parametro incorpora nuevo fuel en cada iteracion. Si queremos que se queme y desaparezca, hay qe ponerlo a cero.
- **Hacer que el "BURN" siga al fuel** : Jugar con los siguentes parametros.
   - "Combustion --> Ignition Temperature" marca la sensibilidad a la que el FUEL comenzara a quemar. Cuanto mas bajo, mas facimente prende.
   - Subir en "Temnperature change" el "Search Radius"  y "Max Neighbors".
   - Si le estamos metiendo la "Temperature" blurearla tambien ayuda.
- **HACER QUE EL FUEL COMBUSTIONE MAS LENTAMENTE** : Tocar el "Combustion-->Burn Rate", cuento mas pequenyo mas lentamente se quema el fuel. Este parametro controla la velocidad basicamente   
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
- **DISTURBANCE** : Anyade ruido blanco a la simulacion, para romper uniformidad. Sirve para romper "mushrooms". Demasiado y sera muy evidente.   

### MICROSOLVERS:   
- **DISTURBANCE (v2.0)** : Agrega detalles finos a una simulación de humo aplicando fuerzas de "perturbación" a la velocidad. Recomendado para romper "mushrooms". Es buena idea aplicar varios con diferentes parametros  (tipicamente "block-size").   
   - Strength : fuerza del efecto   
   - Threshold range : toma el input (densidad tipicamente) y lo remapea como 0-1 para multiplicarlo por "disturbance" (strength). Cualquier valor por encima de 0.05 no se vera afectado (valores con mayor densidad), cuanto más cerca de 0  más se vera afectado. Basicamente lo que hace es potenciar el efecto en los bordes del humo para conseguir más detalle.   
- **GAS BLUR** : Sirve para "suavizar" (blur) el campo indicado. RECORDAR de poner en el "field" lo que queramos blurear (típicamente será "density"). Ayuda a eliminar "artifacts".   
   
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
- **BOLA DE FUEGO y luego LLAMAS** : Animar en el PyroSolver  el "shape->Flame expansion" que controla la tendencia a que el fuego se expanda. Sirve normalmente para explosiones.   
