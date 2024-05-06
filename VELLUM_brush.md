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
- `Sub Steps`: poner a 4, como en el `Vellum Solver`.


**WORKFLOW**   

- Poner los sub-steps a 4 y los constraint iteratios a unos 200 (si no, el tejido se simula mal)

1) CLOTH grande // Utilizar un VELLUM SOLVER para hacer la forma inicial, y luego con `vellum brush` hacer el acabado.
   
![MoCap mapping example](./images/Vellum_Brush_workflow_with_solver.jpg)

2) CLOTH pequeño // Empezar directamente con el `vellum brush`
