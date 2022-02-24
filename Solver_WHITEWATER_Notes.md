## WHITEWATER Solver  

Este solver se crea sobre (on top) de la simulacion FLIP. Por ello suele hacerse una cache del FLIP, y luego, usando los datos de la cache, se simula el "whiteweater"

### Attributes:   

Depth : positivo, encima de la superficie del agua. Negativo, sumergido. CUIDADO! La superficie tambien puede ser el lado del fip que toca un colisionador! Se puede meter en le shader para re-mapear color.


Hay que desactivar en la pestaña "main" el check  “Report Errors/Warnings to the ROP Node” del nodo "RS ROP". De lo contrario el render se para en cuanto la licencia falla.

### Instancias (copy to points y similares):   

Hay que activar en la pestaña "Instancing" en las opciones de Redshift del objeto la opción "instancing using --> Redshift Point Clouds". De lo contrario el render va muy lento.   

### CROWDS:   

Actualmente hace falta hacer "agent unpack" para que Redshift pille bien los agentes del crowd, por lo que es bastante poco eficiente. Se pasa mucho tiempo preparando la escena antes de empezar el render.   
