### Houdini VEX  Snippets

Colección de "snippets" (trozos de código) para realizar funciones concretas. Se aplica a "wranglers" (nodos específicos de Houdini para albergar código VEX), o bien a otros nodos.   

**LINKS a otras paginas con "wranglers" interesantes:**    
- [lex.ikoon](http://lex.ikoon.cz/vex-snippets/) // Snippets    
- [TOSIN AKINWOYE](https://tosinakinwoye.com/2017/01/23/houdini-vex-snippets/) // Snippets   
- [Kiryha](https://github.com/kiryha/Houdini/wiki/vex-snippets) // Snippets, data types, expressions, ...    


**OBTENER INFORMACION INTERESANTE PARA PROCESAR** 
```C#
vector dir = normalize(v@v);    // direccion del vector de velocidad
float speed = length(v@v);      // Magnitud de la velocidad
```   
Distancia desde el centro del objeto:
```C#
vector center = getbbox_center(0);
@dist = distance(@P, center);
```   

**DETAIL // MOSTRAR SOLO "WIREFRAME" en el VIEWPORT** 
```C#
// wrangler run over DETAIL (once)
i@gl_wireframe = 1;
```
**PRIMITIVE // MOSTRAR en ROJO N-GONGS** 
```C#
// wrangler run over PRIMITIVE (once)
if (primvertexcount(0, @primnum) > 4) // Si se quieren motrar triangulos poner "<"
{@Cd = set(1, 0, 0);}
```
**OBJETO // Centrar el pivot y mover al origen de coordenadas** 
```C#
//  Center Pivot and Move to Origin
// set a wrangle to run over points
vector centroid = getbbox_center(0);
vector dist = centroid - 0;
v@P -= dist;
```
**OBJETO // Aplicar una vibración (noise) en el eje de las Y** 
```C#
// Noise on Y // set a wrangle to run over points
@P += set(0,(noise(@Time*10)-0.5), 0);
```
**PRIMITIVA // Crear un punto en el centroide de cada primitiva** 
```C#
// Create points on centroid of primitive // set a wrangle to run over primitives
int prim_points[];
vector accum_pos, pos;
accum_pos = {0, 0, 0};

for (int i = 0; i < primvertexcount(geoself(), @primnum); i++)
{
    int vtx_index = vertexindex(geoself(), @primnum, i);
    int vtx_point = vertexpoint(geoself(), vtx_index); 
    prim_points[i] = vtx_point;
    getattribute(@OpInput1, pos, "point", "P", vtx_point, 0);
    accum_pos += pos;
}

addpoint(geoself(), accum_pos / len(prim_points));
removeprim(geoself(), @primnum, 1);
```
versión simplificada:   
```C#
// RUN over  primitives
addpoint(0, @P); // add point to "centroid" of primitive
removeprim(0, @primnum, 1); // delete primitive (optional)
```
**PUNTOS // BLENSHAPE entre dos inputs mediante un atributo "mask"** 
```C#
// Blenshape utilizando "@mask" para selecciona input // set a wrangle to run over points
@P = lerp(@P,point(1,"P", @ptnum),@mask);
```
**PUNTOS // Borrar puntos de forma aleatoria según una tolerancia** 
```C#
// This snippet will delete random points based on the threshold slider // set a wrangle to run over points
if ( rand(@ptnum) > ch('threshold') ) {
   removepoint(0,@ptnum);
}
```
**PUNTOS // Desplazar puntos en la dirección de la normal a la superficie**   
```C#   
@P += @N * chf('dist');
```   
**PUNTOS // Borrar puntos fuera de la vista de la CAMARA (con una tolerancia)** 
```C#
// Clip points from camera
vector _ndc = toNDC("/obj/cam1", @P);

float _errorx = ch("errorx");
float _errory = ch("errory");
float _errorz = ch("errorz");

// if ((_ndc[0] < 0 - _errorx) || (_ndc[0] > 1 + _errorx))   removepoint(geoself(), @ptnum,1); // Borrar tambien primitivas asociadas
if ((_ndc[0] < 0 - _errorx) || (_ndc[0] > 1 + _errorx))   removepoint(geoself(), @ptnum);
if ((_ndc[1] < 0 - _errory) || (_ndc[1] > 1 + _errory))   removepoint(geoself(), @ptnum);
if ((_ndc[2] > 0 + _errorz))   removepoint(geoself(), @ptnum);
```
**PUNTOS // Proyectar los puntos del objeto sobre la superficie del otro objeto (Como el SOP RAY)** 
```C#
// Project point to minimum distance like RAY Sop // set a wrangle to run over points
@P=minpos(1,@P);
```
**PUNTOS // Normales aleatorias en los puntos** 
```C#
// Random normals // set a wrangle to run over points
v@N=set(fit01(rand(@ptnum),-1,1),fit01(rand(@ptnum+1),-1,1),fit01(rand(@ptnum+2),-1,1));
```
**PUNTOS // Tamaño aleatorio de los puntos, dando maximo, minimo, semilla y RAMPA de distribucion** 
```C#
// SOP Random pscale with Ramp, Seed, Min and Max // change @ptnum for @id in POPs
// set a wrangle to run over points
@pscale = fit01(chramp("Width", rand(@ptnum  + ch("Seed"))), ch("Min"), ch("Max"));
```
**PUNTOS // Rotación de puntos (para instancias y copias). De euler a quaternion** 
```C#
// Random rotation of points (instances)
float angle = fit01(rand(@ptnum),0,360);
p@orient = eulertoquaternion(radians(set(0, angle, 0)), 0);
```
**PUNTOS // Rotación aleatoria en puntos, ajustada mediante una rampa.**
Borrar v@up en caso que ya exista.
```C#
// SOP Random Rotation Wrangle
// if v@up exists, delete first line // set a wrangle to run over points
v@up = {0.0, 1.0, 0.0};
float angle = ch("rot_amount");
float rand = fit01(random(@ptnum+311),0,angle);
p@rot = quaternion(radians(rand), v@up);
```
**PUNTOS // Rotación en ejes locales con QUATERNIONS**
```C#
// Si ya hay atributo @orient eliminar la linea de abajo
@orient = quaternion(maketransform(normalize(-@P),{0,1,0}));

vector4 pitch = quaternion({1,0,0}*ch('pitch'));
vector4 yaw   = quaternion({0,1,0}*ch('yaw'));
vector4 roll  = quaternion({0,0,1}*ch('roll'));

@orient = qmultiply(@orient, pitch);
@orient = qmultiply(@orient, yaw);
@orient = qmultiply(@orient, roll);
```
**PUNTOS // RAMPA de color en un eje segun Bounding Box**
```C#
vector min, max;
getbbox(0, min, max);
@Cd = vector(chramp("reMap",fit(@P.y, min.y, max.y, 0,1)));
```
Otra version parecida:
```C#
// Create attribute ramp based on the relative position in one axis
f@density = 0;
vector test = relpointbbox(0, @P);
@density = chramp('ramp', test.y);
```

**PUNTOS // Transfer de color (y P, posición) desde el segundo input.**
```C#
// Attribute transfer COLOR (and P) from other inputs // set a wrangle to run over points
int handle = pcopen(@OpInput2, "P", @P, chf("search_radius"), chi("num_of_Points"));
vector lookup_P = pcfilter(handle, "P"); //Average P from second input
vector lookup_Cd = pcfilter(handle, "Cd"); //Average Cd from second input
i@many = pcnumfound(handle);
if(i@many>0){
     @Cd = lookup_Cd;
     v@P = lerp(v@P, lookup_P, chf("Position_mix"));
}
```
**PUNTOS // orientar objeto a un punto ("look at"). Deforma el objeto**
```C#
// set a wrangle to run over points
vector pp = point(1,"P",0);//point to look at (2ond input)
matrix3 mm = lookat(@P,pp);
@P*=mm;
```
**PUNTOS // Normal en la bitangent (al estilo polyFrame pero más estable)**
```C#
// set a wrangle to run over points
int prim_points[];
vector pos_A, pos_B, dir;

addattrib(geoself(), "point", "N", {0, 0, 0});
prim_points = primpoints(geoself(), @primnum);
for ( int i = 0; i < len(prim_points); i++ ){
    getattribute(@OpInput1, pos_A, "point", "P", prim_points[i], 0);
    if ( i == 0) {
        getattribute(@OpInput1, pos_B, "point", "P", prim_points[1], 0);
        dir = normalize(pos_B - pos_A);
    }
    else {
        getattribute(@OpInput1, pos_B, "point", "P", prim_points[i - 1], 0);
        dir = normalize(pos_A - pos_B);
    }
    setattrib(geoself(), "point", "N", prim_points[i], 0, dir, "set");
}
```
**PUNTOS // Empujar un objeto contra otro**
```C#
vector dir = -@N;
vector hit_pos, hit_uv; //for fetching into the intersect function below
int ray_intersect = intersect(1, @P, dir, hit_pos, hit_uv);
float hit_dist = distance(@P, hit_pos);
@P += @N*hit_dist*-1*chf("intensity"); //you can multiply a custom float to adjust the intensity
// INPUT 0: objeto a empujar / INPUT 1 : Objeto que empuja
// Al objeto que empuja se le puede convertir en VDB y hacer un "reshape" para "engordarlo"
// El resultado, si se hace un "smooth", queda más fino
```

**POINTCLOUD // Eliminar puntos aislados con una tolerancia.**
```C#
// POINTCLOUD: remove isolated point giving a thresold
int pts[] = nearpoints(0, @P, chf(""radius""),2);
if (len(pts)==1){
    removepoint(0,@ptnum);
}
```

**CURVAS // Grosor de curva mediante rampa**
```C#
// Custom Width Along Curve // set a wrangle to run over points
// 
// needs uvtexture node set to "rows and columns" or "spline"
// running over points before it

float blend = chramp("blend",@uv[0]);
float width = chf("width");
@pscale=blend*width;
```
**CURVAS // Eliminar primer y ultimo punto de una primitiva (típicamente curvas)**
```C#
// Delete first and last curve points //set a wrangle to run over primitives
int primpts[] = primpoints(0,@primnum);
removepoint(0,primpts[0]);  // First point
removepoint(0,primpts[-1]); // Last point
```
**CURVAS // MULTI CARVE: hacer un carve animado en el que las curvas no acaban todas al mismo tiempo**
```C#
// MULTI CARVE. Needs a "mesure" SOP node with computed @perimeter for prims //set a wrangle to run over primitives
#include <groom.h>

float turbulence = rand(@primnum); // get a random number
int start_effect = 1;
int end_effect   = 100;
int shif_in_frames = 50; // decalaje del efecto en frames.

f@dist = fit(@Frame - turbulence*shif_in_frames, start_effect, end_effect, 0.0, 1.0);
// void adjustPrimLength(const int geo, prim; const float currentlength, targetlength)
adjustPrimLength(0, @primnum, @perimeter, @perimeter * @dist);
```


