***HOW TO***

*IMPORT ILLUSTRATOR FILES*  
Lo más sencillo es importar en Maya el fichero illustrator (en versión 8, lo carga mejor), y alli pasarlo a FBX. De esta manera no sepierden puntos ni hace cosas raras en las curvas.

Si no es posible, exportamos el "illustrator" a versión 8, e importamos con un "file node". Con el comando "ends" podemos hacer que las curvas queden abiertas.  

***MODELLING***   

Edge Loops   
  A Key and left mouse button   
  SHIFT then A to add more loops   
 

**Acciones comunes**

- Borrar todo excepto los puntos: Utilizar nodo "ADD" con opcion "Delete Geometry but Keep Points"   
- Separa polygonos (SEPARATE en Maya) : utilizar nodo "FACET" con la opcion "Unique points"   
- Cerrar una curva: utilizar nodo "ENDS"   
- poner una expresion para desplazar un objeto respecto al bounding box: **bbox("../Base_line", D_YMAX)**
- pintar la dirección de las normales: nodo "COMB"
- Utilizar el nodo TRANSFORM para cambiar normales o velocidades en uno o varios puntos: poner el atributo (tipicamente v o N) en el nodo "Attributes" en vez de "*" que hay por defecto.
