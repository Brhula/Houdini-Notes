### Manipular nombre en el campo "file"   
padzero: para añadir ceros al numero de frame   

Looping (de 0  a 250):   
```C++
$HIP/maps/my_map.`padzero(4,$F%251)`.exr
```
Looping (de 1  a 250):   
```C++
$HIP/maps/my_map.`padzero(4,($F-1)%250+1)`.exr
```
Offset:   
```C++
$HIP/maps/my_map.`padzero(4,$F +10)`.exr
```
Hold:   
```C++
$HIP/maps/my_map.`padzero(4, min($F , 250))`.exr // last
$HIP/maps/my_map.`padzero(4, max($F , 1))`.exr // first
$HIP/maps/my_map.`padzero(4, clamp($F,1,250))`.exr // both
```
