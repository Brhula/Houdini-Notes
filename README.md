
// DELETE first & last point of primitives
//set a wrangle to run over primitives
int primpts[] = primpoints(0,@primnum);
removepoint(0,primpts[0]); // delete FIRST point of prim
removepoint(0,primpts[-1]);// delete LAST point of prim
