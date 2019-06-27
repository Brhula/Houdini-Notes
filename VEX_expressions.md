### VEX expressions  

Para utilizar en el nodo "GROUP EXPRESSION" o en un "wrangler".   
En "GROUP EXPRESSIONS" no deben haber espacios, de lo contrario **las expresiones no funcionan**:  

**POINT**
```C#
// "t" is the name of the group
f@group_t = @P.x<0; // group "t" with all points/primitives where X coordinate is less than 0

f@group_r = rand(@ptnum) < 0.5; // new group "r" with 50% of the points/primitives
f@group_end = neighbourcount(0,@ptnum)==1; // new group "end" with all points with ONLy one edge (end points)
```
