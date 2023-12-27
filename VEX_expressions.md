### VEX expressions  

Para utilizar en el nodo "GROUP EXPRESSION" o en un "wrangler".   
En "GROUP EXPRESSIONS" no deben haber espacios, de lo contrario **las expresiones no funcionan**.:  

**POINT**
```C#
// VEX for WRANGLER to create a GROUP
f@group_t = @P.x<0; // group "t" with all points/primitives where X coordinate is less than 0
f@group_r = rand(@ptnum) < 0.5; // new group "r" with 50% of the points/primitives
f@group_end = neighbourcount(0,@ptnum)==1; // new group "end" with all points with ONLy one edge (end points)
```

```C#
// VEX EXPRESSIONS 
@ptnum%(@numpt-1)==0; // group of first and last point
@name=="pepe"; // grupo con todos los que tienen "pepe" como valor del atributo @name
```

**SWITCH NODE**   
Expresiones interesantes para el nodo SWITCH.   

```int  haspointattrib(<geometry>geometry, string attribute_name)```   
Ejemplo: Determine if the "pscale" attribute exists.    
```C#
haspointattrib("../previous_node", "pscale");
```
