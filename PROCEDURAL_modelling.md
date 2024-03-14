### PROCEDURAL MODELLING   


## Notas importantes
- Cuando las normales se queden "feas" hay que poner un nodo `normal` preferentemente con la opción "weighting method" en "By Face Area". Eso las recoloca bien.
- Si queremos recortar una forma con su misma forma más pequeña, en vez de usar un escalado se puede probar a usar un `peak` para que mantenga más las proporciones al "inflarse" respecto a las normales.
- `Boolean` con "shatter" y luego un `poly Bevel` del resultado (grupo "abseam") permite "escarvar" detalles en la superficie.




Bounding Box expression: $YMIN, $YMAX, ...

