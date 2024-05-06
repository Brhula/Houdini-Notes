### VELLUM BRUSH  

Notas sobre "Vellum Brush".   

**NOTAS.**   

- REMESH (con triengulos): suele funcionar mejor con geometria aplicado un `remesh`, ya que los pliegues y otros detalles tinen menos "artifacts".
- COLISIONES: intentar hacerlo con VDBs siempre que sea posible. Si no es posible, evitar angulos duros (sharp), con un `polybevel` suele ser suficiente. Si no, la sim tendrá problemas.
- CONSTRAINT // PIN: Si los ponemos al hacer el `vellum cloth` luego no podremos moverlos.

En los parametros a tener en cuenta:   

- `Density`: indica lo "pesado" que es el tejido.
- `Stretch`: Si se comprime / expande (elasticidad).
- `Bend` : Cuanto se dobla (rigidez / flexibilidad).



**WORKFLOW**   

1) CLOTH grande // Utilizar un VELLUM SOLVER para hacer la forma inicial, y luego con `vellum brush` hacer el acabado.
2) CLOTH pequeño // Empezar directamente con el `vellum brush`
