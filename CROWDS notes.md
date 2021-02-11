### CROWD notas ###   

[CgWiki sobre Crowds](https://www.tokeru.com/cgwiki/index.php?title=HoudiniCrowd)   
[Few notes on Crowd Sim](https://tosinakinwoye.com/2018/10/25/a-few-notes-on-houdini-crowd-simulations/)   
[SIDEFX Intro to crowds 2020](https://www.sidefx.com/tutorials/intro-to-crowds/)   

Los agentes son particulas con informacion adicional en los "intrinsics":
- agentclipnames : name of current clip
Aumentar los "sub-steps" en el DOP hace que mejore el comportamiento en giros y obstaculos ("espasmos" en los agentes).

***Nodos interesantes:***

steer forces are normalised, so playing with the weights is key

**Agent**: 

**Agent Prep**: Permite a los pies quedarse quietos cuando pisan el suelo. Para que no patine. Pone una cadena de IK junto con un CHOP para fijar las piernas.

**Agent Terrain Adaptation**: Hace que los agentes se desplacen por una superficie irregular.

Nodos interesantes en DOP:

**POP Steer wander** : Incorpora aleatoriedad al movimiento (parecido a turbulencia)   

**POP Steer separate** : Aplica fuerzas para mover a los agentes/particulas entre ellos. Steer Separate is a more subtle effect, and allows agents to speed up or brake to avoid collisions. Not as much as I'd like though. It also includes a sense of FOV for each agent to determine how aware they are.   

**POP Steer avoid** : Aplica fuerzas de ANTICIPACION para evitar potenciales colisiones futuras entre agentes/particulas. Steer Avoid is a repulsion, like a pop interact, or another way to think of it is agent personal space. Turn it up too high and it behaves like pop grains; agents separate too quickly and too uniform, it loses the natural chaos of a crowd. It's required of course, but at small values.   

**POP Steer SOLVER** : Used internally in the crowd solver to integrate steering forces. Se pone al final de las fuerzas "steer", para que haga los calculos. Si se utiliza, parece que las fuerzas funcionan mejor para separar las particulas y los obstaculos.   



