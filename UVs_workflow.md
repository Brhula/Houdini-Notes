
SOPS:

- SPLIT UV SEAMS: separa las UVs para que no tenga problemas al procesarlo despues (con un nodo "remesh" poir ejemplo)

### WORKFLOW TÍPICO (manual)   

1) `UV flatten` : nodo para seleccionar los edges, y trocear las UVs. Trocear modelo hasta conseguir una distribución del grid de UVs sin demasiadas distorsiones
2) `UV Layout` : reorganiza las islas de UVs sin solaparse y rellenando el espacio.
3) `UV QuickShade` : Simplemente para comprobar que todo está funcionando



