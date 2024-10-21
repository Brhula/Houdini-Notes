## SHOTGRID Melt notas    


### Incorporar un nuevo software a ShotGrid, como por ejemplo Houdini 20.5
- Añadir el software en la aplicacion WEB en el apartado "software" que hay en la parte derecha arriba, en el icono de la "persona" (administrador). Alli se puede incorporar el nuevo software y la ruta local para el ejecutable.
- Para incorporar una nueva version de Houdini, vigilar que haya una carpeta con la version de Python que utilice H en `classic_startup`,tipicamente en `\\sloth\jobs\copa_america_24016\000_pipeline\copa_america_24016_SGT\install\github\gwbcn\tk-houdini\v1.8.6\classic_startup`. Esto es, en el proyecto en cuestion que utilia este software.



Actualizar el Houdini existente a otra vesrion cambiando ficheros python: https://community.shotgridsoftware.com/t/tk-houdini-engine-for-houdini-20/18082


Toolkit de Houdini para ShotGrid :  https://github.com/shotgunsoftware/tk-houdini
Toolkit para Maya :  https://github.com/shotgunsoftware/tk-maya

### Para actualizar el `tk-houdini` (por ejemplo de la version v1.8.6 a la v.9.3 que permite arrancar Houdini 20.5):

- descargamos la version de `tk-houdini` correspondiente.
- La descomprimimos en el proyecto donde toca en el proyecto, por ejemplo `...\000_pipeline\pipeline_test_7777_SGT\install\github\gwbcn\tk-houdini` en la carpeta `v1.9.3`
- Actualizar el fichero `engine_locations.yml` que esta en `.../000_pipeline\pipeline_test_7777_SGT\config\env\includes` (ejemplo de proyecto). Aqui cambiamos la version que apunta a houdini (por ejemplo v1.8.6 la pasamos a v1.9.3).
- Cache de shotgrid en Windows (ejemplo): `C:\Users\marco\AppData\Roaming\Shotgun` . Se necesita borrar esta cache a veces cuando Houdini no arranca porque busca la version antigua del toolkit.
