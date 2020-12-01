## POP FLUID NOTES

PBD Fluid solver (Position Based Dynamics). Solver interesante para fluidos a pequenya escala (gotas y demas). Bastante rapido y estable (!).

En la simulación FLIP se utilizan " volumes" y "grid", por ello las colisiones funcionan mejor con "volumes".   

### BEFORE START SIMULATION:   
<ins>**Particle separation**</ins>: para hacer mas o menos detallado el fluido   

<ins>**Constraint iterations**</ins>: Iteraciones para mantener el "particle separation", cuanto mayor, mejor se conserva el "particle separation".   
El valor por defecto (5) funciona para el solver de "white water". Valores bajos hacen mas "tendrils", valore altos juntan mas el liquido.   
Lo tipico es empezar a partir de 20 e ir subiendo, para que el liquido tenga mas consistencia.   
Indica el numero de particulas de grosor ("number of particles that is the larges thickness of the fluid") que tendra el liquido    

<ins>**Constraint stiffness**</ins>: "Fuerza de cohesion", para obligar a las particulas a estar juntas. Poner numero alto aqui (100, 200, 400, ...). Cuento mayor el numero, menor la tolerancia a desviaciones del "goal", pero si es alto <ins>puede introducir inestabilidad</ins>.   

<ins>**Viscosiy**</ins>: El valor inicial es muy bajo. Probar a partir de 0.1 hast el 1 (tambien puede superar el 1 segun como). Al aumentar la viscosidad, deben aparecer menos "grupos" de particulas.    

<ins>**Tensile Strenght**</ins>: Fuerza para intentar separar mas las particulas, que no se apelotonen. Para intentar mantener mas los "sheets" de agua y "tendrils" mas largos. El valor original (0.001) es muy bajo. Probar con 0.005 o 0.01. Es un valor sensible.    
