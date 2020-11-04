### VELLUM  

Notas de varios tipos sobre "Vellum".  

**NOTAS.**   

PREPARAR para SIMULAR:
- "Always sanity test pscale": El valor pscale se hereda de la geometria de entrada (input). Comprobar siempre si funciona.

MEJORAR SIMULACIÓN:   
  1) probar incrementando ""sub-steps"".   
  2) comprobar ""Thickness"", dependiendo de la escala de la escena.   
     Si son muy grandes, la escena se ralentiza (calculo de colisión), y pueden aparecer ""spikes"" y protusiones   
     (el solver se vuelve tonto).   
     Si son pequeños, tendremos más errores de simulación."   

ANIMACIONES GUIADAS:
- Para guiar animaciones se   

**QUE HACER PARA:**   
- Aumentar la friccion del tejido : En el solver (en SOPS) hay un parametro "Static Threshold" que lo controla el atributo "friction" (si no hay atributo "friction" entonces val 1 por defecto). Esta a 0.5, si lo subimos el tejido aumenta la friccion.   

**PARAMETROS.**   
Thickness: "es el parametro ""pscale"", que sirve para saber la escala de los puntos iniciales.   
Se fija en el ""vellum constraint"". Al iniciar la simulación, si hay puntos que se interseccionan, vellum escalará los puntos conflictivos para que el  solver no explote.
- Debe ser lo suficientemente pequeño para que permita las arrugas."

**Nodos.**   
Otras combinacione posibles.

