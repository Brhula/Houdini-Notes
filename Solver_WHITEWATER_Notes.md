## WHITEWATER Solver  

Este solver se crea sobre (on top) de la simulacion FLIP. Por ello suele hacerse una cache del FLIP, y luego, usando los datos de la cache, se simula el "whiteweater"

### Attributes:   

Depth : positivo, encima de la superficie del agua. Negativo, sumergido. CUIDADO! La superficie tambien puede ser el lado del fip que toca un colisionador! Se puede meter en le shader para re-mapear color.
