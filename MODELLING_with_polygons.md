## MODELLING with POLYGONS

#### TIPs

https://www.youtube.com/watch?v=kAXUfg2FbYY


#### <ins>SELECCION INTERACTIVA</ins>

- `Edge Loop`: doble click en el *edge*. Con SHIFT y CTRL te permiten añadir o eliminar mas *loops*
- `Face loop`: manten pulsa la tecla A, al mover el cursor hace *preview* de como quedara. Boton central (MMB) selecciona el loop.
- `Face loop parcial`: Igual que antes, pero botón izquierdo (LMB)
- `SELECT ISLAND`: manten pulsa la tecla H y selecciona (LMB) en el interior del area cerrada. Si se hace con SHIFT+H se conserva la parte que ya estaba seleccionada.
- `SELECT ISLAND` : doble clic en un polygono y seleccionamos la "polygon Island". Con `control` y `shift` podemos añadir o eliminar mas cosas.
  
- `N`: selecciona todo
- `SHIFT N`: des-selecciona todo
- `SHIFT G` : expande seleccion
- `SHIFT S` : Reduce seleccion
- `CTRL I`: Invertir selección

#### <ins>CONVERTIR polys to points y demás</ins>

botón de la derecha del ratón y seleccionar `Convert selection to...`

#### <ins>HOW TO con nodos</ins>

- `Convert triangles to hexagons` : Utilizamos el nodo `divide` con la opción `compute dual`
- `BAD NORMALS` : Cuando las normales se queden "feas" hay que poner un nodo `normal` preferentemente con la opción "weighting method" en "By Face Area". Eso las recoloca bien.
- Si queremos recortar una forma con su misma forma más pequeña, en vez de usar un escalado se puede probar a usar un `peak` para que mantenga más las proporciones al "inflarse" respecto a las normales.
- `Boolean` con "shatter" y luego un `poly Bevel` del resultado (grupo "abseam") permite "escarvar" detalles en la superficie.

