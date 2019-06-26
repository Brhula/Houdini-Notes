### Redshift en HOUDINI   


**Render de una secuencia sin licencia**   

Hay que desactivar en la pestaña "main" el check  “Report Errors/Warnings to the ROP Node” del nodo "RS ROP". De lo contrario el render se para en cuanto la licencia falla.

   
  
**NOISE (reduce)**
```C#
Unified samples         //  Motion blur and depth of field noise   
light samples           //  Shadows and direct specular noise   
Shader samples          //  Indirect specular noise   
GI samples              //  GI noise   
Volume samples (lights) //  VDBs and volumes noise 
```

**VOLUME Rendering**   
- Add "Volume" shader to object   
- In "volume shader", add "density" to "Channel" to create SMOKE. Its empty by default   
- In "volume shader", add 'HEAT' (or 'TEMPERATURE') to the emission -> Channel to get fire and incandescence   
- Check "Volume" light contribution (0 by default) on every light needed to lit volume   
- Increase "Samples" on the "Volume" tab in the lights, to avoid noise   
- Turn ON "Global Illumination" to let the fire "light" the volume   
- Check "advanced" tab in Volume shader to remap HEAT or TEMPERATURE and bring the numbers down (HEAT value is usually lower than TEMPERATURE). Like mapping 50 to 1 for TEMPERATURE  and 15 to 1 on HEAT
	
	
**VOLUME Shader**   
- Absortion: (like "transparency") cuanto más alto, más denso el humo
- Scatter:  (like "diffuse") tiende a hacer más brillante el humo
- Emission: (like "incandescence") para fuego. Utilizar "head" o "Temperature" para conseguir la incandescencia del fuego.
- Shadow density: densidad de las sombras. Valores bajos para nubes más transparentes
	
**TIPS:**   
- *Volumen mas o menos opaco:* incrementat tanto el "Absortion coefficient" como el "scatter coefficient" al mismo tiempo mas brillante o  más oscuro: modificar solamente "scatter coefficient"
- *Color de todo el volumen:* modificar "scatter tint". Utilizar la rampa para remapear según la densidad: Izquierda--> menos denso, derecha--> más densidad
	
