## MATERIAL StyleSheets ##   

En una ventana (nueva o ya existente) seleccionar:   
- Inspectors > Data Tree   
- Choose a Viewer > Material Style Sheets   

Podemos añadir un "style sheet" a un objeto, o a la escena entera.

[PETfactory Style Sheets](https://www.petfactory.se/notes/houdini_stylesheets/)   

### INTRODUCCION ###
El elemento esencial de los crowds son los "packed agents". Es parecido a una "packed primitive", ya que es un punto que incluye toda la información sobre la geometria, clips de animación, metadata y otros elementos.   


### NOTAS ###   
- Si la particula tienen velocidad inicial ("v"), entonces ignora el parametro "heading".   
- Aumentar los "sub-steps" en el DOP hace que mejore el comportamiento en giros y obstaculos ("espasmos" en los agentes).   


### "Intrinsics" interesantes:
- agentclipnames : name of current clip
- agentcliptimes : contiene el "time" en el que se encuentra el clip. Se puede manipular directamente. Por ejemplo:
```C++
float t[];
t[0] = @startoffset + @Time/@pscale*2;
setagentcliptimes(0,@primnum,t);
```

steer forces are normalised, so playing with the weights is key   

## CROWDS // MATERIAL StyleSheets ##   
