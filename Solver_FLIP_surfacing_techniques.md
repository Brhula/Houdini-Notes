## FLIP SURFACING NOTES
Técnicas para mejorar la creación de un "mesh" despues da haber simulado las particulas (y volumentes) del FLIP.



### NODOS:   
**FLUID COMPRESS**   
Comprime particulas y volumen.
- Generalmente merece la pena hacer "cache" justo después de este nodo.
- En "Keep Attributes" suele merecer la pena dejar solo "v pscale id" y poco más. Lo demás ocupa sitio y no se suele usar.

**PARTICLE FLUID SURFACE**   
Genera la superficie para hacer render. NODO LENTO! Mejor hacer "fine tuning" antes de lanzar la cache.   

OPTIMIZACIONES para PREVIEW:
- "Transfer attributes": merece la pena desactivarlo para ir más rápido e iterar. Activarlo para hacer render y que transfiera velocidad y demás.
- En "Region-->Bounding Box" desactivar "Closed Boundaries". Solo hará surfacing de la superficie del FLIP.
- Utilizar un "bounding box" más pequeño que toda la extensión de ka simulación (conectado a un cubo, o a mano)   

PARAMETROS ÚTILES:  
Dependiendo de donde está la camara, con el "motion blur" y demás, nos interesara más o menos detalle y tamaño.
- Particle Separation: distancia entre puntos. Mejor desligarlo de la simulación. Se puede  reconstruir a partir del "pscale" de la cache.    
- Voxel Scale: impacta en la fidelidad del "mesh" resultante. Bajarlo mejora la calidad. CUIDADO MEMORIA!! Además ralentiza notablemente el proceso.
- Droplet scale: multiplicador del "pscale".    
- 
Ejemplo típico: Voxel Scale (0.45) / Influence Scale (2) / Droplet Scale (0.5)    

- Union Compressed Fluid Surface: Junta las particulas con el volumen bajo el agua. Hay que dejarlo ON generalmente.
- Collisions--> Substrackt Collision Volumes: En el "plug" de en medio del nodo podemos conectar geometría (generalmente la que colisiona). Puede ser VDB o la geometria en sí. Mejor VDB para mejores resultados. ES MUY LENTO!. No usarlo hasta hacer el cakculo final.

**Check animation**   
- Deactivate ""brain"" to avoid simulations   
- uncheck ""integer frames values"" in animation preferences   
- Scrub timeline with substeps to check animation behaving"   


### VEX:   
**Minimizar flicker y particulas sueltas**   
Comprobamos cuantas particulas hay alrededor, y multiplicamos el numero encontrado por el "pscale". De esta forma "pscale" es mayor cuantas más particulas hay alrededor, y mas pequeño si está aislado.
```C++
// Get near points with a distance. With Maximum numbre of points
int gatheNearPoints[] = nearpoints(0,@P,chf("maxDistance", chi("maxPoints")); 
// How many points are close to our point?
float pscaleMult = len(gatheNearPoints); 
// Compute new "pscale", with an additional global multiply.
@pscale *= pscaleMult * chf("additional_scale_multiply");
```
