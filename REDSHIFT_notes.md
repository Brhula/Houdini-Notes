## Redshift en HOUDINI   

### // Instancias (copy to points y similares):   

- Hay que activar en la pestaña "Instancing" en las opciones de Redshift del objeto la opción "instancing using --> Redshift Point Clouds". De lo contrario el render va muy lento.
- Para que los colores se propaguen por las instacias, activar en el objecto (en propiedades de RS --> Settings --> Instancing) el `Instances SOP Level Packed Primitives`
- TESSELATION : Para que subdivida correctamente las `packed primitives` hay que deconectar Tesselation --> Screen Space Adaptive.

### // CROWDS:   

Actualmente hace falta hacer "agent unpack" para que Redshift pille bien los agentes del crowd, por lo que es bastante poco eficiente. Se pasa mucho tiempo preparando la escena antes de empezar el render.   


### // NOISE (reducir ruido)   
Parámetro a tocar // Tipo de ruido al que afecta.   
```C#
Unified samples         //  Motion blur and depth of field noise   
light samples           //  Shadows and direct specular noise   
Shader samples          //  Indirect specular noise   
GI samples              //  GI noise   
Volume samples (lights) //  VDBs and volumes noise 
```
#### SSS RANDOM WALK FLICKERING   
- A veces SSS Random Walk hace flicker, para solucionarlo poner GI en Brute Force + Brute Force. Más lento pero lo elimina
- Otra solución es aumentar en el GI secundario el Irradiance Point Cloud (IPC) el parámetro `RayTrace threshold` a 3 (por ejemplo). Se supone que es más rápido que el anterior.

### // PBR Materials   
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

### // Material LAYERING  
Utilizar un nodo "Material Blender", conectando:
- "Base Color": es el primer material
- En el "Layer Color 1" el material (shader) que queramos mezclar
- En el "blend color" la máscara (textura) utilizada para mezclar los dos materiales.
    
Utilizar también un "Displacement Blender" y un "Bump blender".   

### // VOLUME Rendering   
- Add "Volume" shader to object   
- In "volume shader", add "density" to "Channel" to create SMOKE. Its empty by default   
- In "volume shader", add 'HEAT' (or 'TEMPERATURE') to the emission -> Channel to get fire and incandescence   
- Check "Volume" light contribution (0 by default) on every light needed to lit volume   
- Increase "Samples" on the "Volume" tab in the lights, to avoid noise   
- Turn ON "Global Illumination" to let the fire "light" the volume   
- Check "advanced" tab in Volume shader to remap HEAT or TEMPERATURE and bring the numbers down (HEAT value is usually lower than TEMPERATURE). Like mapping 50 to 1 for TEMPERATURE  and 15 to 1 on HEAT
	
### // VOLUME Shader   
- Absortion: (like "transparency") cuanto más alto, más denso el humo
- Scatter:  (like "diffuse") tiende a hacer más brillante el humo
- Emission: (like "incandescence") para fuego. Utilizar "head" o "Temperature" para conseguir la incandescencia del fuego.
- Shadow density: densidad de las sombras. Valores bajos para nubes más transparentes

### // STRANDS and CURVES   
- No admite color (u otros atributos) por "point", solo por cada curva. Los colores (Cd) son uno por curva. Si hay que hacer render con mas de un color hay que transformarlo a "mesh"
- Para tener strands/curvas con colores diferentes, colorear "por primitiva" y luego hacer un "attribute promote" a "points". De esta forma si pilla los colores (para cada curva completa). Entonces se puede pillar el "RS color data" en el shader.
- No le gustan los "packed objects" al hacer render como "strands". Mejor "desempaquetarlos", de lo contrario se pasa un buen rato "pensando".

### // RENDER REFRACTANDO FONDO PERO SIN VERLO   
Si ponemos un background en el HDRI (enable background + backplate) se vera el fondo. La unica manera de hacer que el fondo refracte (con cristales por ejemplo) y que no se vea, es hacer una esfera gigante y convertirla en "matte object". Hay que desactivar todos sus componentes de visibilidad excepto "primary", de lo cantrario hara sombras y demas interferencias.

### // CRYPTOMATTE   
Si quereos que el fichero d Cryptomatte no acabe coo "*.exr.cryptomatte" tenemos que poner $AOV en el OUTPUT path, tipo  `$HIP/render/$HIPNAME/$HIPNAME.$OS.$AOV.$F4.exr`.    

### // RENDER MAPS (para hacer "bake" de las texturas con la luz de la escena)   
![Alt text](images/Render_Maps.jpg?raw=true "Title")   

- (!!!) Vigilar las normales de los objetos, si no, el render sale negro.
- (!!!) UVs no deben solaparse, si no el render sale mal.
- UVs en el espacio [0-1] preferiblemente.
- En "OBJECTS" forzamos los objetos que queramos que se consideren en el render (tanto para que se renderizen como para que hagan sombras o rebotes de luz).
- En "RENDER MAPS -> Render Map Object" ponemos el objeto que queramos hacer "bake" de sus textras con la luz.

### // TIPS:   
- *Volumen mas o menos opaco:* incrementat tanto el "Absortion coefficient" como el "scatter coefficient" al mismo tiempo mas brillante o  más oscuro: modificar solamente "scatter coefficient"
- *Color de todo el volumen:* modificar "scatter tint". Utilizar la rampa para remapear según la densidad: Izquierda--> menos denso, derecha--> más densidad
- VOLUME MOTION BLUR: Parece que no hace bien el mb con VDB, hay que convertirlo a HOUDINI VOLUMES.
- **OVERSCAN:** para hacer "overscan" del render (para "plates" sin distorsion, al volver a aplicarles la distorsion), utilizar "overscan mode" a pixeles en "ROP redshift".
	
### // WARNINGS:   
- *Texturas:* Parece que los ficheros ".pic" de Houdini no le gustan. Hace cosas raras en el render.   
	
