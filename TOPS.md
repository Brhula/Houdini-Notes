## HOUDINI TOPS    

[intro to TOPS en CGwiki](https://www.tokeru.com/cgwiki/HoudiniTops)   
[HOUDINI TOPS build-in attributes](https://www.sidefx.com/docs/houdini/tops/attributes.html#builtin)

#### ELEMENTOS BASICOS en TOPs   

- WORKITEM: unidad "atomica" de TOPS, tipicamente un fotograma, pero puede ser cualquier cosa: un frame, una secuencia, un directorio en el disco duro... Es una unidad de procesamiento    
- PARTITIONS: los WORKITEMS pueden organizarse en "partitions" de forma similar a como los puntos en SOPs se les pueden hacer "pack" y "unpack" para trabajarlos.

#### GENERATE vs COOK   

Boton derecho en el nodo:
- GENERATE: Intenta construir los `work items` sin cocinarlos. Es como generar la lista de cosas a hacer, pero sin hacerlo. Bueno para ver los elementos que hay.
- COOK: Efectivamente hace el trabajo, se pone a calcular y "cocinar" el resultado.
