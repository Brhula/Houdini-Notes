## WHITEWATER Solver  

Solver para simular espuma, burbujas y micro-gotas voladoras en liquidos.
Este solver se crea sobre (on top) de la simulacion FLIP. Por ello suele hacerse una cache del FLIP, y luego, usando los datos de la cache, se simula el "whiteweater"

### Componentes:   

- (1) source (SOP): aqui se define las zonas donde nace y crece el "whitewater". Tambien se puede inducir manualmente.  Es en donde la simulacion busca cuales son los emisores de las particulas de "whitewater" 
- (2) simulate (DOP) : propiamente la simulacion, que pilla el "source" para generar y calcular el "whitewater". Es donde mas parametros suelen tocarse.
- (3) import (SOP) : importamos la sim, para generar le geometria que hacer render   

### (1) SOURCE (SOP):   

- Se considera aceleracion, curvatura y vorticidad
- output es un emission VDB

### (2) SIMULATION (DOP):   

- whitewaterobject: parametros de colision
- whitewatersolver: Se encarga de emitir y matar las particulas   

Las particulas no saben su "origen", una burbuja se puede transformar en espuma, al subir a la superficie.
Las particulas envejecen mediante el solver. La esperanza de vida no esta predeterminada. Las particulas se eliminan basandose en el valor del atributo *"deathchance"*.    
Que determina la probabilidad de eliminar una particula:   
- edad y vida (age and life): Las mas viejas es mas probable que mueran.
- profundidad (depth): por valores de la tasa de envejecimiento (Aging Rates)
- density: cuando la erosion esta activada.

#### FUERZAS   
- uniform gravity:
- bouyancy: flotabilidad. Sube las burbujas.
- advection: mueve las particulas con el fluido.
- density control : previene que las particulas hagan "clusters" (se acerquen demasiado entre ellas), y permite un "surface tension" que hace que parezcan mejor un fluido.
- depth control: empuja las particulas hacia la superficie. 
- repulsion: para separar las pariculas  entre si.

#### REPELLANTS    
- Puntos "especiales" que empujan el "whitewater" afuera, dando origen a espuma de patron celular.    
- Se almacenan en el "whitewater object" como geometria con el nombre *"Repellants"*

### Attributes:   

Depth : positivo, encima de la superficie del agua. Negativo, sumergido. CUIDADO! La superficie tambien puede ser el lado del fip que toca un colisionador! Se puede meter en le shader para re-mapear color.
