## HOW TO ##

### IMPORT ILLUSTRATOR FILES ###  
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

### CONVERTIR HIP FILES ###     
Para saltar limitacion. Utilizamos el Textport (Windows > Hscript Textport).

Cargamos escena de origen, escribir en el Textport algo parecido para grabar fichero con la escena en texto:   
```C++
opscript -G -r / > $TEMP/temp.cmd
```
Salimos de H y arrancamos la aplicacion de nuevo.
Hacemos una escena nueva, con los mismos FPS de la de origen (y copiando el $JOB u otras variables).    
Despues tambien en Textport, cargamos el fichero generado anteriormente con:   
```C++
cmdread $TEMP/temp.cmd
```
Comprobar los nodos que dependen de $JOB y $HIP, ya que habra que ajustar para que vuelva a funcionar todo.     
Tambien hay que comprobar que los nodos de simulacion esten correctamente transpasados.

