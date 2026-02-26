# RBD BULLET SOLVER en HOUDINI

### // ATTRIBUTES    

```C#
// Attributes


s@name : nombre de las piezas a colisionar
i@active : 0 (static) 1 (active) // 0 si el objeto es "attrezzo" para colisionar
i@animated is 1, Bullet will read the intrinsic transform attribute from each packed primitive in SOPs, and update the transform in DOPs to match.

//
```

### // NAME Attribute   

- es el mas importante, todo lo que tenga el mismo nombre es una misma pieza para "bullet".
- Si mezclamos objetos y en algunas piezas los nombres son los mismos, el resultado sera chungo.
- Para hacer "convex hull" por pieza, que haya varias piezas que separadas tengan el mismo nombre.

### // USAR PROXY GEOMETRY para ghacer los calculos (version simplificada de la geometria principal)   
