### CROWD notas ###   

[CgWiki sobre Crowds](https://www.tokeru.com/cgwiki/index.php?title=HoudiniCrowd)   

Los agentes son particulas con informacion adicional en los "intrinsics".   


Nodos interesantes:

**Agent**: 

**Agent Prep**: Permite a los pies quedarse quietos cuando pisan el suelo. Para que no patine. Pone una cadena de IK junto con un CHOP para fijar las piernas.

**Agent Terrain Adaptation**: Hace que los agentes se desplacen por una superficie irregular.

Nodos interesantes en DOP:

**POP Steer wander** : Incorpora aleatoriedad al movimiento (parecido a turbulencia)   
**POP Steer separate** : Aplica fuerzas para mover a los agentes/particulas entre ellos.   
**POP Steer avoid** : Aplica fuerzas de ANTICIPACION para evitar potenciales colisiones futuras entre agentes/particulas. Steer Avoid is a repulsion, like a pop interact, or another way to think of it is agent personal space. Turn it up too high and it behaves like pop grains; agents separate too quickly and too uniform, it loses the natural chaos of a crowd. It's required of course, but at small values.   
**POP Steer SOLVER** : Used internally in the crowd solver to integrate steering forces. Se pone al final de las fuerzas "steer", para que haga los calculos. Si se utiliza, parece que las fuerzas funcionan mejor para separar las particulas y los obstaculos.   


