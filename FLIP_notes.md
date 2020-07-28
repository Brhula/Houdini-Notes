## FLIP NOTES

### BEFORE START SIMULATION:   
**Check collision geometry**   
Uncheck "Display geometry" and check "Collision Guide" to see the shape of the objext.. Allways check size and shape of colliders, default values are usually terrible

**Check animation**   
- Deactivate ""brain"" to avoid simulations   
- uncheck ""integer frames values"" in animation preferences   
- Scrub timeline with substeps to check animation behaving"   

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
