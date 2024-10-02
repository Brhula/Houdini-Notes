### FBX en Houdini

Utilizaremos el atributo `s@path` (en las "primitivas") para construir la jerarquía y que los objetos queden organizados. 

Para ello podemos utilizar el nodo `name` poniendo en el atributo a construir `path`, o tambien con VEX (es un stributo de tipo "string").

No parece que se puedan enviar animacipones de puntos. Para eso mejor Alembic.

### Inspeccionar ALEMBIC con herramienta externas (de Houdini)

- Abrir una consola  `Command Line Tools` de Houdini
- utilizar el comando `abcinfo <fichero alembic>` para objeter info basica (fps, frame start and end)
- utilizar comando `abcecho <fichero alebic>` para obtener info detallada, inlcuyendo de donde viene el alembic, objetos que contiene y demas.

### ALEMBIC in Houdini

- El "frame rate" del Alembic y la escena deben coincidir.
- Se puede hacer "time shift" en el nodo de Alembic en el campo "frame" con la expresión $FF+offset
- Para reposicionar un "alembic archive" lo mejor es poner un nulo, y emparentarlo (como padre) al alembic (como hijo). Luego se aplican las típicas TRS para ajustar a plano.

### ALEMBIC IMPORT in Houdini

- Para saber cuando empieza y cuando acaba un alembic, pinchar "info" en el nodo SOP del alembic. Lo pone en segundos y en frames.
- El fotograma actual del alembic está en el "primitive intrinsic" abcframe. Está en segundos, no en frames.
- Los ficheros alembic soportan "sub-frame animation" al utilizar un escalar (float) como número de frame, de forma que se pueden poner a "slow motion" con facilidad.
- el intrinsic "abcframe" se puede manipular en VEX para tocar velocidad de un alembic:
```C#
// VEX running on primitive. Poner solo una de las lineas.
setprimintrinsic(0, "abcframe", @primnum, 2.0, "set"); // forzamos el segundo 2
setprimintrinsic(0, "abcframe", @primnum, 0.5, "mult"); // Velocidad a mitad
```

### ALEMBIC exports to Maya

https://medium.com/@jessicabeckenbach/exporting-alembic-files-from-houdini-using-the-path-attribute-ac9f34f5ab1   
https://ddankhazi.com/2019/07/04/houdini-to-maya-export-an-alembic-file/comment-page-1/   

Alembic "need to know" things:   
- Pack Geometry for every group of primitives before exporting. Every paked geo will appear as a Maya "shape" node.   
- Name of last node in Houdini before "ROP Alembic" node will appear as the root transform in Maya.

### Exportar GEO a Maya (Metodo 1)   
Y que en Maya aparezca con una jerarquía en el Outliner (para mejorar organizacion):
- crear un nodo CONNECTIVITY en modo PRIMITIVE. Dejar el atributo por defecto "class"
- crear un PRIMITIVE WRANGLER con el siguiente código (modificarlo según interese que aparezcan los nombres en Maya):
```C++
// Para exportar a Maya con estructura
// wireGRP : nombre del nodo "top" de la jerarquia
// wireGEO : nombre del nodo "transform" para cada elemento
// wireGEOShape : nombre del nodo "shape"

s@path = 'wireGRP/wireGEO' + itoa(i@class) + '/wireGEOShape' + itoa(i@class) ; 
```
- Utilizar un nodo ROP ALEMBIC para exportar la geometria, y activar la opción *Build Hierarchy From Attribute (path)*    

### Exportar GEO a Maya (Metodo 2)   
Y que en Maya aparezca con una jerarquía en el Outliner (para mejorar organizacion):
- para cada elemento que queramos que aparezca por separado, hacer un ""name"" attribute. Se puede utilizar el nodo ""name"" (SOP)
- En el "ROP Alembic" utilizar:
   - Partition Mode en "use attribute value" con el nombre "name". Los objetos tendrán un "shape" separado
   - "Build Hierarchy from Attribute" con el nombre del atrubute "name" para generar el path completo ransform )



### Exportar GEO con cambios de topologia a Maya   

Como por ejemplo exportar GEO con numero de puntos y caras animado como ALEMBIC (tipo boolenas animadas) o meshes FLIP.
El metodo es hacer un "stitch" fde la secuancia de alembics de salida:
- Generar secuencia de Alembics (tipo name.$F4.abc)
- Importar la secuencia  alembics de nuevo en Houdini
- Hacer un "unpack" y "attribute delete" (de lo no necesario)
- Grabar un nuevo alembic con el resultado en un solo fichero (stitch)


### MAYA MEL scripts to help   

**Change all objects selected for a new one inside Maya**   
   
```C++
// Substitute obects
// Cambiamos todos los objetos selecionados por una instancia (mismo shape)

string $instance ="pCube13"; // Maya object to use as instance.

string $selection[] = `ls -sl`;
for ($each in $selection)
 {
    select -r $instance;
    $instance_copy = `instance`;
    pickWalk -d down;
    select -add $each;
    parent -r -s;
 }
```
