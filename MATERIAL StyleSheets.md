## MATERIAL StyleSheets ##   

En una ventana (nueva o ya existente) seleccionar:   
- Inspectors > Data Tree   
- Choose a Viewer > Material Style Sheets   

Podemos añadir un "style sheet" a un objeto, o a la escena entera.

- STYLE: Contiene especificaciones para el "TARGET" y una lista de "OVERRIDES" para modificar el "TARGETED GEO"
- TARGET: A que geometria debe aplicarse las modificaciones.
- OVERRIDE: Como modificar los materiales de la geometria seleccionada.   
   
- El orden de los elementos en el stylesheet es importante. Se ejecutan de arriba hacia abajo. Los ultimos tienen preferencia sobre los primeros.   
- los objetos adicionales (sombreros, cascos, herramientas) anadidos mediante "LAYERS" se acceden en el primer grupo de sub-targets (Agent Shape)

### EJEMPLO de styleSheet con CROWDS ###   
- En el nodo "AGENT" el campo "Agent Name" va a parar al POINT ATTRIBUTE @agentname
- En el stylesheet buscamos en los "point attribute" el nombre en concreto
- Y en el "sub-target" miramos que grupo de primitivas (que en Maya es un objeto "mesh") y buscamos su nombre (con o sin wildcards).

![Alt text](images/Crowds_and_StyleSheet_01.jpg?raw=true "Title")   

[PETfactory Style Sheets](https://www.petfactory.se/notes/houdini_stylesheets/)   
