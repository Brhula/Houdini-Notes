## POP FLUID NOTES

Solver interesante para fluidos a pequenya escala (gotas y demas). 

En la simulación FLIP se utilizan " volumes" y "grid", por ello las colisiones funcionan mejor con "volumes".   

### BEFORE START SIMULATION:   
**Particle separation**: para hacer mas o menos detallado el fluido   

**Constraint iterations**: Iteraciones para mantener el "particle separation".   
El valor por defecto (5) funciona para el solver de "white water". Valores bajos hacen mas "tendrils", valore altos juntan ma el liquido.   
Lo tipico es empezar a partir de 20 e ir subiendo, para que el liquido tenga mas consistencia.   
Indica el numero de particulas de grosor ("number of particles that is the larges thickness of the fluid") que tendra el liquido    

**Constraint stiffness**: "Fuerza de cohesion", para obligar a las particulas a estar juntas. Poner numero alto aqui (100, 200, 400, ...)   

**Viscosiy**: El valor inicial es muy bajo. Probar a partir de 0.1.    

**Tensile Strenght**: Para intentar mantener mas los "sheets" de agua. El valor original (0.001) es muy bajo. Probar con 0.005 0 0.01. Es un valor sensible.    
