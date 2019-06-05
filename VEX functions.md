### VEX common fuctions  

Para utilizar en el nodo "wrangler":  

**POINT**
```C#
// LERP Performs bilinear interpolation between the values.
float  lerp(float value1, float value2, float amount)
// FIR Takes the value in one range and shifts it to the corresponding value in a new range.
float  fit(float value, float omin, float omax, float nmin, float nmax)
// CLAMP Returns value clamped between min and max.
float  clamp(float value, float min, float max)
```
