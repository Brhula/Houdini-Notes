### CROWD notas ###   




Nodos interesantes:

**Agent**: 

**Agent Prep**: Permite a los pies quedarse quietos cuando pisan el suelo. Para que no patine. Pone una cadena de IK junto con un CHOP para fijar las piernas.

**Agent Terrain Adaptation**: Hace que los agentes se desplacen por una superficie irregular.

Nodos interesantes en DOP:

**POP Steer wander** : Incorpora aleatoriedad al movimiento (parecido a turbulencia)   
**POP Steer separate** : Aplica fuerzas para mover a los agentes/particulas entre ellos.   
**POP Steer avoid** : Aplica fuerzas de ANTICIPACION para evitar potenciales colisiones futuras entre agentes/particulas.   
**POP Steer SOLVER** : Used internally in the crowd solver to integrate steering forces. Si se utiliza, parece que las fuerzas funcionan mejor para separar las particulas y los obstaculos.   


