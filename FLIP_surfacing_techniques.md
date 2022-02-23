## FLIP SURFACING NOTES
Técnicas para mejorar la creación de un "mesh" despues da haber simulado las particulas (y volumentes) del FLIP.



### NODOS:   
**FLUID COMPRESS**   
Comprime particulas y volumen.
- Generalmente merece la pena hacer "cache" justo después de este nodo.
- En "Keep Attributes" suele merecer la pena dejar solo "v pscale id" y poco más. Lo demás ocupa sitio y no se suele usar.

**PARTICLE FLUID SURFACE**   
Genera la superficie para hacer render y precios   
OPTIMIZACIONES:
- "Transfer attributes": merece la pena desactivarlo para ir más rápido e iterar. Activarlo para hacer render y que transfiera velocidad y demás.
- En "Region-->Bounding Box" desactivar "Closed Boundaries". Solo hará surfacing de la superficie del FLIP.



**Check animation**   
- Deactivate ""brain"" to avoid simulations   
- uncheck ""integer frames values"" in animation preferences   
- Scrub timeline with substeps to check animation behaving"   

