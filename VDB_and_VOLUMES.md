### VDB 

- Tiene voxels activos e inactivos. Los inactivos no se calculan (es esparso), por eso es mas rapido de calculo.


### NODES:

**VDB ACTIVATE** : 
- Permite activar voxeles que no estan activos, para poder hacer calculos en ellos. Por ejemplo aumentar los voxeles para poder meterles ruido y que el VDB pueda expandirse.


**Rename a volume** : 
  - use de `name` node to rename the primitive volumes
  - deactivate `Number of Namigns`
  - and activate `Number  of Renames`, and change the name, for example from "density" to "surface". 
