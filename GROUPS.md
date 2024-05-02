#### <ins>GROUP EXPRESSION</ins>   

[Vex group expressions interesantes](https://www.artstation.com/blogs/jorgelega/7m1r/houdini-10-useful-vex-snippets-for-group-expression-node)

Group expression útiles en el nodo para seleccionar según el caso. Metemos expresiones en código VEX.   
- Crear grupo en un FOTOGRAMA en particular: `@Frame==chi("Frame")` , además hace un slider para entrar el numero arriba en el nodo.
- Primer punto de una primitiva : `vertexprimindex(0, @vtxnum)==0` poner el nodo en modo `point`.
- Primera y última primitiva: poner en un `group node` la expresión:
  ```C#
  `0  nprims("0")-1`
  ```  


#### <ins>PROMOTE GROUPs</ins>   

- Para convertir edges en primitivas, mejor utilizar VEX. Si utilizamos "group promote" se convierten también las primitivas que solo tocan un punto.
  ```C#
  // Run over primitives y seleccionando el grupo de "edges" en el campo Group
  i@group_nuevoGrupo=1;
  ```  

#### <ins>TIPS</ins>   

- Highlight de un grupo: usar `group combine` y combinar consigo mismo. Eso hace que podamos verlo en el viewport sin necesidad de ponerle un "color". Tabién se puede usar VEX en Bindings->Output Selection Group   
