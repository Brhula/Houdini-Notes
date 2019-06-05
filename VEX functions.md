### VEX common fuctions  

Para utilizar en el nodo "wrangler":  

**Funciones para hacer calculos con datos, pueden ser vectores, enteros o numeros reales.**   
Mirar documentación para comprobar variantes con otros tipos de datos.
```C#
// LERP Performs bilinear interpolation between the values.
float  lerp(float value1, float value2, float amount);
// FIT Takes the value in one range and shifts it to the corresponding value in a new range.
float  fit(float value, float omin, float omax, float nmin, float nmax);
float  fit01(float value, float nmin, float nmax) ; // de (0, 1) a nuevo rango 
// CLAMP Returns value clamped between min and max.
float  clamp(float value, float min, float max);
```
**VECTORS. Funciones con vectores**
```C#
float  distance(vector a, vector b); // DISTANCE: distancia entre dos puntos
float  length(vector v); // LENGTH: longitud (magnitud) de un vector
// RELBBOX : Returns the relative position of the point given with respect to the bounding box of the primitives in the geometry.
vector  relbbox(<geometry>geometry, vector position);

```
