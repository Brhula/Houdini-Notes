### INSTANCIAS de objetos

Copiar instancias a puntos de objetos en memoria (SOP node):
```C++
s@instance = sprintf("/obj/SOP_node");
```
Funciona también en sub-networs de nodos.   
Un ejemplo de asignación aleatoria de nodos dentro de una sub-network que se llama "TREES_subnet", en donde los nodos se llaman "Tree_01", "Tree_02", ...,"Tree_16".   

```C++
i@frame = floor(rand(@ptnum+1579)*10+1);
if (@frame < 10) {
    s@instance = sprintf("/obj/TREES_subnet/Tree_0%d", @frame);
    }
else {
    s@instance = sprintf("/obj/TREES_subnet/Tree_%d", @frame);
}

```
