## CROWD notas ##   

[CgWiki sobre Crowds](http://tokeru.com/cgwiki/HoudiniCrowd.html)   
[Few notes on Crowd Sim](https://tosinakinwoye.com/2018/10/25/a-few-notes-on-houdini-crowd-simulations/)   
[SIDEFX Intro to crowds 2020](https://www.sidefx.com/tutorials/intro-to-crowds/)   
[SIDEFX crowds example with bats 2019](https://www.sidefx.com/tutorials/crowd-workshop/)   
https://crowdsinhoudini.notion.site

SIDEFX nuevo sistema más sencillo en SOP para crowds simples de [Houdini 20](https://www.youtube.com/watch?v=z8Z5PsnWFto)

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



## FBX PREPARATION

- en el "AGENT" se pone el personaje en T-pose y SIN animación.   
- En el "AGENT  CLIP" se ponen las animaciones de los joints (sin necesidad de tener "skin"). ATENCION MIXAMO!!!! El esqueleto de animacion en el `AGENT CLIP` y el del rig del `AGENT` deben tener el mismo nombre, para que los huesos encajen!
- En los clips que vienen `take_001` es la pose de modelado y `mixamo.com` es la animacion (o pose) que hay pegada de Mixamo.   
- Los clips de animación deben tener un loop perfecto para que no haya saltos. NO hay que tenerlos en T-pose al principio   
- Para poder poner shaders separados a diferentes partes del "agent" (cara, camisa, zapatos, etc.), debe haber un "Maya mesh" distinto en cada uno de ellos. De esta manera en el "style sheet" se puede poner un "sub-target" apuntando a ese "Maya mesh" y asignarle un nuevo shader/textura
- IMPORTANTE: 
  - La estructura de los joints debe ser la misma en el RIG que en los clips de animación. De lo contrario se hace un lio en Houdini.   
  - El NOMBRE de los joints debe coincidir (CUIDADO CON MIXAMO!!! A VECES EL NOMBRE/NAMESPACE CAMBIA!!! Comprobar que el RIG y la ANIMACION tienen el mismo nombre!)
  - Asegurarse que el esqueleto animado está exactamente en el plano XZ con los pies en el suelo. Si no, flota.
  - Al exportar animación, vigilar que solo se exporte la parte del clip animada. Si no, el clip se para.
  - WARNING!!!! Si utilizamos "convert units" los `PROPS` para poner en el `agent layer` deberan ser escalados (x100 normalmente). Si se puede, pillar FBX que esten ya en la escala de Houdini. Todo se simplifica.

## FBX MIXAMO PREPARATION

- Las escalas vienen mal (son x100) y muchas veces el `namespace` es distinto. ~~Por ello es IMPORTANTE pasar tanto el RIG como las ANIMACIONES por Maya~~ (mirar el punto siguiente), eliminar el `namespace` y exportar en METROS (no centimetros, que es lo que viene por defecto). Asi en Houdini tenemos la escala correcta, y eliminamos problemas con los nombres.
- Si grabamos los ficheros en FBX ASCII entonces con un editor de texto podemos cabiar el "namespace", por ejemplo de `mixamorig9:` a `mixamorig:` de forma que pueda hacer el "mapping" de los joints sin problemas.
- Si no tenemos Maya, exportamos en ASCII FBX desde Mixamo y con un editor de texto hacemos `replace` del texto del `namespace`, por ejemplo "mixamorig:" por ""   
- Si pegamos un esqueleto de un personaje a otro, probablemente tengamos (por la diferencia de estructura) un resultado "raruno" con estiramientos y demas. Segun sea el crowd, puede ser suficiente. Si estan muy cerca entonces se va a notar.    

# To add "mixasmorig:" namespace run Rig Att. Wrangler:
```C++
// ADD mixamo NameSpace // RUN on points
@name = "mixamorig:"+@name;
```

# To remove Mixamo namespace:
```C++

// RUN on points
// STRIP mixamo??: namespace
string  mixamo[];
mixamo =  split(@name, ":", 1);
if (len(mixamo)>1) {
    @name = mixamo[1];
    }
```

## CROWD WORKFLOW   

- `Agent` : Nodo basico para importar el "agente" (el modelo fbx/rig/etc). Se puede poner el modelo en T-pose y luego incorporar animaciones. Crea un "packed agent"
- `Agent Clip`: Selecciona que clip animado utilizamos con este "agent"
- `Agent Layer`: Permite poner "props" en el "agent", como sombreros, armas, utensilios... 
- `Agent Prep`: Permite que Houidini utilice algunos de los joints para saber como utilizar el agent. Por ejemplo permite a los pies quedarse quietos cuando pisan el suelo. Para que no patine. Pone una cadena de IK junto con un CHOP para fijar las piernas.

**Agent Terrain Adaptation**: Hace que los agentes se desplacen por una superficie irregular.

- In palce animation
  - Setup
- SetUp AGENTS
- SIMULATION


## CROWD HOW TO   

- SABER QUE NOMBRES HAY EN @agenshapename PARA ASIGNARLOS A STYLESHEET: utilizar un nodo "unpack" o "agent unpack" y mirar en las primitivas. En la columna "agentshapename" deben aparecer los nombres. Además deberian coincidir con los "mesh names" de la jerarquía Maya y el equivalente en C4D. 


