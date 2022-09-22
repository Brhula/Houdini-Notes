### VELLUM GRAINS  

Notas sobre los "Vellum grains".  

El número de "grains" afecta a la simulación. El comportamiento es diferente según el "particle separation". Eso puede ser un problema si se intenta hacer una simulación en baja y luego replicarla en alta..   

Cuando el "particle separation" es pequeño (muchas particulas) los grains tienden a colapsar por la gravedad.

Puede ser interesante repetir la simulación con un "seed" diferente y combinarlo después (merge), para de esta forma tener más particulas con el mismo comportamiento. Cuidado porque entonce se "meten" las unas dentro de las otras.

**ATRIBUTOS/PARAMETROS.**   
- Por defecto 
- MASS: Afecta a como interaciona con las "POP forces" y como de fuertes son los "constraints". Cuanto mayor, mas "pesada" es la tela. Cuanto menor, mas "liviana" la tela. Al pesar mas o menos, también estira más el tejido.   
- DENSITY (depende de MASS): Multiplicador de la masa. Forma rápida de tocar todo el "peso" del tejido cuando Vellum calcula la masa. Admite multiplicarlo por un atributo.   
- THICKNESS: grosor del punto. Se almacana en "pscale".   
- SUB STEPS : Lo estandar es 4. Menos va mal para "grains".   

**HOW TO**   

- UTILIZAR "velocity VDB" para mover los grains: No se puede hacer un "volume source" (al estilo de "pyro"), ya que son particulas. Hay que poner un nodo "POP advect by volume" que apunte al nodo SOP y conectarlo a "force" dentro del "Vellum solver".      
- GRANOS DE TAMAÑO DIFERENTE: hay que tocar el "pscale" antes de meterlo en el solver, y en "advanced-->grain collision" desactivar "assume uniform radius".
- TOCAR PROPIEDADES o ATRIBUTOS DURANTE LA SIMULACION: Dentro del DOP utilizar el nodo "vellumconstraintproperty" para tocar parametros. Se puede conectar con VEX a otros SOP.
- COLISIONES : Funciona mucho mejor con VOLUME COLLIDERS.  Con "surface" hace tonterias.   

MEJORAR SIMULACIÓN:   
  1) probar incrementando ""sub-steps"".En cloth es conveniente comenzar con 4 o 5.   
  2) comprobar ""Thickness"", dependiendo de la escala de la escena.   
     Si son muy grandes, la escena se ralentiza (calculo de colisión), y pueden aparecer ""spikes"" y protusiones   
     (el solver se vuelve tonto).   
     Si son pequeños, tendremos más errores de simulación."   
