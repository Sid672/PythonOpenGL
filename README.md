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
- Upto this we have completed the basic diagram requirement. We can create cube using these data but to make it more intresting we use colours on surface. For this we require two more touples: one for colors and one for surfaces.

```Python
surfaces = (
	(0, 1, 2, 3), #This means 4 points create a face of cube.
	(0, 3, 4, 5), #Example - We are connecting point no. 0, 3, 4, 5 for creating a face.
	(0, 1, 6, 5),
	(1, 2, 7, 6),
	(2, 3, 4, 7),
	(4, 5, 6, 7)
	)

colors = (
	(1, 0, 0),   #Color of face no. 0;
	(0, 1, 0),   #Six faces six colors.
	(0, 0, 1),
	(1, 1, 0),
	(0, 1, 1),
	(1, 0, 1),
	)
```
- Now we are ready to make our cube. To do this we create a function. 

```Python 
def cube:
    //body of function.
```

- In OpenGL every drawing statement should be written between `glBegin()` and `glEnd()`.

```python
def cube():

	glBegin(GL_QUADS)
	for surface in surfaces:
		x = 0
		for vertex in surface:
			x += 1
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])

	glEnd()

	glBegin(GL_LINES)
	glColor3fv((0, 1, 0))
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
```
- In the above program one should understand some functions used in the program.
- `glColor3fv()` function is used for coloring the surfaces(face of cube).
- `gl` stands for graphics library, `Color` stands for operation, `3fv` means function will take three arguments that are floating point value.
- Similarly, `glVertex3fv()` has its own meaning. It is used to draw vertex.
- One can observe that two new words are also used in the above program that are `GL_QUADS` and `GL_LINES`. These both are called constants.
- Constants are always written in capatial letters. The role of constant is to perform a task. For example - `GL_QUADS` is used to draw a polygon and `GL_LINES` are used to draw line segements.



