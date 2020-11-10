## PYRO FX NOTES

   

### COLISIONES con PYRO:   
**Utilzar VDB para el calculo de colisiones**   
- utilizar "VDB convert to polygon" SOP.   
- En DOPs, usar nodo "static object", y:   
   - Poner en "SOP Path" el VDB de SOP
   - "Collision detection" en "Use volume collision"
   - y en "Volume"-->"Mode"  poner "Volume sample"
- Conectar el "static object" al "merge" despues del Pyro Solver.

**Check animation**   
- Deactivate ""brain"" to avoid simulations   
- uncheck ""integer frames values"" in animation preferences   
- Scrub timeline with substeps to check animation behaving"   

**Check "FLIP Object"**   
En "GUIDES" activar "Collision" y comprobar que tiene suficiente resolución. Si no, activar "Collision separation" y bajar el valor para que tenga el colisionador más resolución   
