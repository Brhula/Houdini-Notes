## Redshift en HOUDINI   


### Render de una secuencia sin licencia (con WaterMark):   

Hay que desactivar en la pestaña "main" el check  “Report Errors/Warnings to the ROP Node” del nodo "RS ROP". De lo contrario el render se para en cuanto la licencia falla.

### Instancias (copy to points y similares):   

Hay que activar en la pestaña "Instancing" en las opciones de Redshift del objeto la opción "instancing using --> Redshift Point Clouds". De lo contrario el render va muy lento.

### NOISE (reducir ruido)   
Parámetro a tocar // Tipo de ruido al que afecta.
```C#
Unified samples         //  Motion blur and depth of field noise   
light samples           //  Shadows and direct specular noise   
Shader samples          //  Indirect specular noise   
GI samples              //  GI noise   
Volume samples (lights) //  VDBs and volumes noise 
```
### PBR Materials   
Toggle "Gamma override" check on "texture" node if dealing with gray scale images.   
Use node "Bump Blender" to combine Normal and Bump mapping.   
- Albedo/Diffuse/Base/Color : diffuse color   
- Roughness : reflexion roughness   
- Gloss / Glossiness:  connect to "reflexion roughness" and on "advanced" tab check "convert glossiness to roughness".    
- AO (if needed) : overall color / diffuse weight / or multiply by diffuse color   
- Normal : Texture node connected to a "Bump map" node with "tangent space". : Bump Input (on RS material) or Bump Map (o Redshift Material, the exit node)   
- Height / Displacement : Displacement node and to "Displacement"   
- Metal / Metalness : Reflection Metalness (change "Fresnel Type" to "Metalness" and "BRDF" to "GGX")   

![Alt text](images/RedShift_PBR.jpg?raw=true "Title")   

### VOLUME Rendering   
- Add "Volume" shader to object   
- In "volume shader", add "density" to "Channel" to create SMOKE. Its empty by default   
- In "volume shader", add 'HEAT' (or 'TEMPERATURE') to the emission -> Channel to get fire and incandescence   
- Check "Volume" light contribution (0 by default) on every light needed to lit volume   
- Increase "Samples" on the "Volume" tab in the lights, to avoid noise   
- Turn ON "Global Illumination" to let the fire "light" the volume   
- Check "advanced" tab in Volume shader to remap HEAT or TEMPERATURE and bring the numbers down (HEAT value is usually lower than TEMPERATURE). Like mapping 50 to 1 for TEMPERATURE  and 15 to 1 on HEAT
	
### VOLUME Shader   
- Absortion: (like "transparency") cuanto más alto, más denso el humo
- Scatter:  (like "diffuse") tiende a hacer más brillante el humo
- Emission: (like "incandescence") para fuego. Utilizar "head" o "Temperature" para conseguir la incandescencia del fuego.
- Shadow density: densidad de las sombras. Valores bajos para nubes más transparentes
	
### TIPS:   
- *Volumen mas o menos opaco:* incrementat tanto el "Absortion coefficient" como el "scatter coefficient" al mismo tiempo mas brillante o  más oscuro: modificar solamente "scatter coefficient"
- *Color de todo el volumen:* modificar "scatter tint". Utilizar la rampa para remapear según la densidad: Izquierda--> menos denso, derecha--> más densidad
- **OVERSCAN:** para hacer "overscan" del render (para "plates" sin distorsion, al volver a aplicarles la distorsion), utilizar "overscan mode" a pixeles en "ROP redshift".
	
### WARNINGS:   
- *Texturas:* Parece que los ficheros ".pic" de Houdini no le gustan. Hace cosas raras en el render.   
	
