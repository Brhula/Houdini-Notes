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
float floor(float n); // FLOOR: Returns the largest integer less than or equal to the argument.
float ceil(float n); // CEIL: Returns the smallest integer greater than or equal to the argument.

float  chramp(string channel, float ramppos); // Evaluates a ramp parameter and return its value.
float  chramp(string channel, float ramppos, float time)
vector  chramp(string channel, float ramppos)
vector  chramp(string channel, float ramppos, float time)

vector  getbbox_center(<geometry> geometry) // Nos da el centroide de la geometria
```
**Cambio de tipo de datos.**   
Otras combinacione posibles.
```C#
string  itoa(int number) ; // Convierte Integer a Ascii (string)
string  sprintf(string format, ...);
```
**VECTORS. Funciones con vectores**
```C#
float  distance(vector a, vector b); // DISTANCE: distancia entre dos puntos
float  length(vector v); // LENGTH: longitud (magnitud) de un vector
// RELBBOX : Returns the relative position (0-1) of the point given
// with respect to the bounding box of the primitives in the geometry.
vector  relbbox(<geometry>geometry, vector position);

```
**GEOMETRIA. Funciones con geometria**
```C#
void  getbbox(<geometry> geometry, vector &min, vector &max); // pone en "min" y "max" los valores del bounding box
```
