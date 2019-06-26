
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
