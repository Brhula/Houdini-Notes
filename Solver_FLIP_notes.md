## FLIP NOTES

### LINKs INTERESANTES:   

http://www.cgchannel.com/2020/03/10-expert-tips-for-better-houdini-flip-fluid-simulations/

Si estamos emitiendo fluido, el fotograma inicial de la simulación debe tener geometria desde la que emitir. De lo contrario el solver se quejará.   

En la simulación FLIP se utilizan " volumes" y "grid", por ello las colisiones funcionan mejor con "volumes".   

### BEFORE START SIMULATION:   
**Check collision geometry**   
Uncheck "Display geometry" and check "Collision Guide" to see the shape of the objext.. Allways check size and shape of colliders, default values are usually terrible

**Check animation**   
- Deactivate ""brain"" to avoid simulations   
- uncheck ""integer frames values"" in animation preferences   
- Scrub timeline with substeps to check animation behaving"   

**Check "FLIP Object"**   
En "GUIDES" activar "Collision" y comprobar que tiene suficiente resolución. Si no, activar "Collision separation" y bajar el valor para que tenga el colisionador más resolución   

**Objetos cerrados o con grosor**   
Los objetos de colisión deben tener volumen, para generar la supeficie correctamente (es volumetrica). Vale la pena visualizar el volumen para asegurarse que sigue razonablemente la superficie.

**Flip fluid Object**   
Usually Density is 2 or 3 times bigger than Viscosity (Viscosity = 1000 => Density = 3000)

**PARTICLE SEPARATION**   
Comprobar la "particle separation" con respecto al tamaño de la simulación, para ver si es mucho o poco (todo está en unidades de H)

### on FLIP NODE
**Solver "Splashy VS Swirly Kernel"**
"Splashy (default): tipico de simulaciones con alta energía, como oceanos, rios.   
Swirly: para simulaciones con alta vorticidad, donde hay que reducir el ruido de superficie al maximo. Como simulacione de pequeña escala o lava.Los fluidos viscosos utilizan el ""swilry"""   

**Reseeding (Crear o borrar particulas)**   
Comprueba la cantidad de particulas que hay dentro del voxel, y añade más cuando es demasiado pequeño, y elimina cuando el numero es demasiado grande. Se utiliza para intentar mantener el volumen constante (evitar agujeros de "aire"). Puede ser necesario desactivarlo para objetos con un volumen constante (como un objeto fundiendose)

**Particle Separation (Resolución)**   
"Separación de las particulas, en unidades H. Cuanto más pequeño, más particulas (y más lento), equivale a la resolución del liquido.
La masa (particle mass) se recalcula al cambiar este parametro. Utilizar fuerzas con""ignore mass"" o poner mass=1 para que no cambie el comportamineto del fluido

La escala o sensación del liquido se dirige por el ""particle separation"". Si la separación es demasiado grande, puede parecer una miniatura."

**Particle Radius Scale**   
Escala del radio de la particula. A mayor tamaño, más volumen ocupa la particula pero tiene menos detalle   

**Grid Scale**   
Factor de escalado del volumen que se utiliza para hacer el calculo de la velocidad de las particulas. Puede hacer que el efecto mas "fino" (thinner) o mas "basto". Reducirlo lo hace más fino   

### HOW TO / TIPS AND TRICKS   

**// crear un INITIAL STATE**   
- (1) Dentro de la "DOP network" poner al final un nodo de "file" en modo "write" que apunte a un fichero que utilizaremos como "initial state". 
- (2) Ir hasta un fotograma que nos interese/guste (tipico posición de reposo del fluid)
- (3) Cambiar el nodo de "write" a "read".
- (4) conectar a un "switch" el "Flip Fluid Object" (primero) y en nodo "file" con el "initial state" (segundo) con la expresión `$SF==1`. El "simulation frame" == a 1 impica que el nodo "file" solo se leerá en el primer fotograma de la simulación, luego va por el "flip fluid object"

**// Kill FLIP particle at some age (VEX)**   
- Activate ""life"" at ""Source Volume"" 
- Activate ""Age Particles"" at ""FLIP Solver""
- Create a pop Wrangler with code:   
    `if (@dead==1) removepoint(0,@ptnum);`

**// H17 use SOP volume fields**   
- create vector **velocity** on points (Geometry)
- Use ""Volume rasterize attribute"" to create ""v"" volume
- On DOP, use ""volume source"" DOP to convert ""v"" source volume to ""vel""

**// Improve smoothness of surface on small scale liquids**   
Increase number of particles via reseeding
FLIP SOLVER --> Particle Motion--> Reseedin:
  - Increment ""surface oversampling"" (from 1.5 to 10 - 48)
  - Rise ""Oversamblipng Bandwith""  (like 1.5)
  
**// Que el fluido "resbale" por la superficie aunque tenga viscosidad**   
Añadir un field ""slip"" en SOP. Importar field ""slip"" en DOPs con ""sopScalarField"". 
slip = 0, no resbala. slip=1 resbala a tope    

