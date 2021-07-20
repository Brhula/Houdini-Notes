### VELLUM  

Notas de varios tipos sobre "Vellum".  

**ATRIBUTOS/PARAMETROS.**   

- MASS: Afecta a como interaciona con las "POP forces" y como de fuertes son los "constraints". Cuanto mayor, mas "pesada" es la tela. Cuanto menor, mas "liviana" la tela. Al pesar mas o menos, también estira más el tejido.   
- DENSITY (depende de MASS): Multiplicador de la masa. Forma rápida de tocar todo el "peso" del tejido cuando Vellum calcula la masa. Admite multiplicarlo por un atributo.   
- THICKNESS: grosor del punto. Se almacana en "pscale".   

**NOTAS.**   

PREPARAR para SIMULAR:   

- "Always sanity test pscale": El valor pscale ("thickness") se hereda de la geometria de entrada (input). Comprobar siempre si funciona.   
- ESCALA: es importante ya que 1 unidad Houdini es un metro. Escalar la escena para que encaje correctamente en estos parametros.   
- Intentar poner las UVs cuanto antes, para que no tengamos que rehacer cosas despues de haber simulado.   
- El nodo "remesh" es muy util para conseguir una "mesh" que tenga una subdivision triangular similar en todas partes. Evita "artifacts".

MEJORAR SIMULACIÓN:   
  1) probar incrementando ""sub-steps"".En cloth es conveniente comenzar con 4 o 5.   
  2) comprobar ""Thickness"", dependiendo de la escala de la escena.   
     Si son muy grandes, la escena se ralentiza (calculo de colisión), y pueden aparecer ""spikes"" y protusiones   
     (el solver se vuelve tonto).   
     Si son pequeños, tendremos más errores de simulación."   

ANIMACIONES:
- NO se puede animar parametros a nivel de objetos (SOP). Hay que hacerlo dentro del solver (DOP). Constraints y parámetros deben animarse dentro del sistema de dinamicas.   

CLOTH:
- Empezar con "substeps" de 4 o 5. Menos hace el comportamiento del cloth poco creible al hacerlo muy elastico.   

**CLOTH VELLUM CONSTRAINT:**   
- STIFFNESS: Cuan elastico es el tejido. Por defecto (1e+10) tiene un valor en el que no se estira o comprime. Tocandolo un poco se consiguen efectos interesantes.   
- Con "STIFFNESS-->Rest Length Scale" podemos controlar la longitud del cloth. Para hacerlo mas grande o pequenyo. Es interesante utilizar "paint attributes" para pintar una mascara que aisle partes que queremos cambiar el comportamiento.
- BEND: Cuento puede doblarse cada poligono sobre si mismo. Valores altos hacen el tejido con menos arrugas. Valores bajos permiten mas arrugas. ATENCION: la resolucion del "mesh" juega un papel importante en cuanto se puede arrugar. Pocos polygonos, pocas arrugas....

**QUE HACER PARA:**   
- **Aumentar la friccion del tejido** : En el solver (en SOPS) hay un parametro "Static Threshold" que lo controla el atributo "friction" (si no hay atributo "friction" entonces su valor 1 por defecto). Esta a 0.5, si lo subimos el tejido aumenta la friccion y resbala menos.   
- **Hacer "pin" de una parte del mesh** : para que sea independiente de la resulucion del "mesh", utilizar un "group node" con el "Keep in Bounding Regions" activado. Eso nos da un volument en que los puntos que esten dentro perteneceran al grupo.
- **Mas o menos arrugas** : Cambiar el "bend stiffness". Menos valor = más arrugas. Mas valor = menos arrugas. Si es cero, muchas arrugas...   

**PARAMETROS.**   
Thickness: "es el parametro ""pscale"", que sirve para saber la escala de los puntos iniciales.   
Se fija en el ""vellum constraint"". Al iniciar la simulación, si hay puntos que se interseccionan, vellum escalará los puntos conflictivos para que el  solver no explote.
- Debe ser lo suficientemente pequeño para que permita las arrugas."



