
### Cambiar de forma ciclica el fondo del *"viewport"*    
Poner el sigueinte codigo en un *"tool"* del Shelf, y asignarle alguna tecla en el hotkey editor (con ponerlo en el contexto *"general"* es suficiente).    
alt+B para que sea como Maya, pero con CTRL+ALT+B no hay tanto conflicto     

```python
import sys
import toolutils

bg = None

try:
    # cycle next bg
    if kwargs['ctrlclick']: raise
    bgs = hou.session.bg[:]
    bgs = bgs[1:]+bgs[:1]
    if kwargs['shiftclick']: bgs = ['bw', 'light', 'wb']
    bg = bgs[0]
    hou.session.bg = bgs
except:
    # set up default bg vars
    hou.session.bg = ['wb', 'bw', 'light']
    bg = hou.session.bg[0]

bgs = { 'wb':'dark', 'bw':'grey', 'light':'light' }

hou.hscript("viewdisplay -B %s *" % bg)
hou.ui.setStatusMessage("Cycled background to %s" % bgs[bg].upper() )
```

