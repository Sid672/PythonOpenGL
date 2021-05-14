# PythonOpenGL

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/200px-Python.svg.png)
![](https://www.opengl.org/img/opengl_logo.png)

# Requirements
Python 3.6 or higher version.
  - Python libraries: pygame, opengl.
 
  To install these libraries use:
  
  `pip install pygame`
  
  `pip install PyOpenGL`
  
  
# Getting started

#### Aim: To make a cube using openGL.

- First import all necessary files.

```Python
import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
```

- Now using your art skills draw a rough diagram on paper with proper coordinates of points as given below. 

![](https://www.math.brown.edu/tbanchof/Beyond3d/Images/chapter8/image04.jpg)

- In program your vertices will be in touple which looks like

```Python
vertices = (
	(0, 0, 0), #Point 0
	(1, 0, 0), #Point 1
	(1, 1, 0), #Point 2
	(0, 1, 0), #Point 3
	(0, 1, 1), #Point 4
	(0, 0, 1), #Point 5
	(1, 0, 1), #Point 6 
	(1, 1, 1)  #Point 7
	)
```
- Next we connect vertices, for this we create a edges touple.

```Python 
edges = (
	(0, 1), #This means connect Point 0 to Point 1.
	(0, 3), #Similarly, other connections are to be made
	(0, 5), #according to the diagram of cube.
	(1, 2),
	(1, 6),
	(2, 3),
	(2, 7),
	(3, 4),
	(4, 5),
	(5, 6), 
	(6, 7), 
	(7, 4)
	)
```



