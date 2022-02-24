## WHITEWATER Solver  

Solver para simular espuma, burbujas y micro-gotas voladoras en liquidos.
Este solver se crea sobre (on top) de la simulacion FLIP. Por ello suele hacerse una cache del FLIP, y luego, usando los datos de la cache, se simula el "whiteweater"

### Componentes:   

- source (SOP): aqui se define las zonas donde nace y crece el "whitewater". Tambien se puede inducir manualmente.  Es en donde la simulacion busca cuales son los emisores de las particulas de "whitewater" 
- simulate (DOP) : propiamente la simulacion, que pilla el "source" para generar y calcular el "whitewater". Es donde mas parametros suelen tocarse.
- import (SOP) : importamos la sim, para generar le geometria que hacer render   

### Attributes:   

Depth : positivo, encima de la superficie del agua. Negativo, sumergido. CUIDADO! La superficie tambien puede ser el lado del fip que toca un colisionador! Se puede meter en le shader para re-mapear color.
