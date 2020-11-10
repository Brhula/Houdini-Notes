## PYRO FX NOTES

   

### COLISIONES con PYRO:   
**Utilzar VDB para el calculo de colisiones**   
- utilizar "VDB convert to polygon" SOP.   
- En DOPs, usar nodo "static object", y:   
   - Poner en "SOP Path" el VDB de SOP
   - "Collision detection" en "Use volume collision"
   - y en "Volume"-->"Mode"  poner "Volume sample"
   - en "Proxy volume" hacer que apunte tambien al VDB del SOP.
- Conectar el "static object" al "merge" despues del Pyro Solver.   

El Pyro ahora deberia colisionar con el objeto SOP.

**Si el humo pasa a traves del objeto de colision**   

Esto no siempre es necesario. Solo si atraviesa. En general deberia funcionar bien.   
Bajar el "Time Scale" (a 0.5 o 0.25) para que detecte mejor las colisiones.   
Subir los sub-steps del DOP no parece funcionar muy bien.   
Luego, para hacer la cache, poner un TimeWarp para recuperar velocidad original.   

 
