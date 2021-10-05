## CROWD notas ##   

[CgWiki sobre Crowds](https://www.tokeru.com/cgwiki/index.php?title=HoudiniCrowd)   
[Few notes on Crowd Sim](https://tosinakinwoye.com/2018/10/25/a-few-notes-on-houdini-crowd-simulations/)   
[SIDEFX Intro to crowds 2020](https://www.sidefx.com/tutorials/intro-to-crowds/)   
[SIDEFX crowds example with bats 2019](https://www.sidefx.com/tutorials/crowd-workshop/)   

### INTRODUCCION ###
El elemento esencial de los crowds son los "packed agents". Es parecido a una "packed primitive", ya que es un punto que incluye toda la información sobre la geometria, clips de animación, metadata y otros elementos.   

En los "intrinsics" del "packed agent" está la información necesaria para procesar el "agent".


### NOTAS ###   
- Si la particula tienen velocidad inicial ("v"), entonces ignora el parametro "heading".   
- Aumentar los "sub-steps" en el DOP hace que mejore el comportamiento en giros y obstaculos ("espasmos" en los agentes).   


### "Intrinsics" interesantes:
- agentclipnames : name of current clip
- agentcliptimes : contiene el "time" en el que se encuentra el clip. Se puede manipular directamente. Por ejemplo:
```C++
float t[];
t[0] = @startoffset + @Time/@pscale*2;
setagentcliptimes(0,@primnum,t);
```

steer forces are normalised, so playing with the weights is key

Nodos interesantes en DOP:

**POP Steer wander** : Incorpora aleatoriedad al movimiento (parecido a turbulencia)   

**POP Steer separate** : Aplica fuerzas para mover a los agentes/particulas entre ellos. Steer Separate is a more subtle effect, and allows agents to speed up or brake to avoid collisions. Not as much as I'd like though. It also includes a sense of FOV for each agent to determine how aware they are.   

**POP Steer avoid** : Aplica fuerzas de ANTICIPACION para evitar potenciales colisiones futuras entre agentes/particulas. Steer Avoid is a repulsion, like a pop interact, or another way to think of it is agent personal space. Turn it up too high and it behaves like pop grains; agents separate too quickly and too uniform, it loses the natural chaos of a crowd. It's required of course, but at small values.   

**POP Steer SOLVER** : Used internally in the crowd solver to integrate steering forces. Se pone al final de las fuerzas "steer", para que haga los calculos. Si se utiliza, parece que las fuerzas funcionan mejor para separar las particulas y los obstaculos.   


## CROWD WORKFLOW   

- Agent : Nodo basico para importar el "agente" (el modelo fbx/rig/etc). Se puede poner el modelo en T-pose y luego incorporar animaciones. Crea un "packed agent"
- Agent Clip: Selecciona que clip animado utilizamos con este "agent"
- Agent Prep: Permite a los pies quedarse quietos cuando pisan el suelo. Para que no patine. Pone una cadena de IK junto con un CHOP para fijar las piernas.

**Agent Terrain Adaptation**: Hace que los agentes se desplacen por una superficie irregular.

- In palce animation
  - Setup
- SetUp AGENTS
- SIMULATION


## CROWD RENDERING


