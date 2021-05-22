# PythonOpenGL

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/200px-Python.svg.png)
![](https://www.opengl.org/img/opengl_logo.png)

# Overview
![](https://media.giphy.com/media/BhAVomTAXMUYZRxB7z/giphy.gif)


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

- Now using your art skills to draw a rough diagram on paper with proper coordinates of points as shown below. 

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
- One can observe that two words are also used in the above program that are `GL_QUADS` and `GL_LINES`. These both are called constants.
- Constants are always written in capatial letters. The role of constant is to perform a task. For example - `GL_QUADS` is used to draw a polygon and `GL_LINES` are used to draw line segements.

- It's time to step up the screen for this one can use 
```Python
def main():
	pygame.init()
	display = (800, 600)                                      #screen size
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)      #For refresh rate(frame buffer)

	gluPerspective(45, (display[0] / display[1]), 0.1,  50.0) #Here 45 is angle view,
	                                                          #then aspect ratio of screen (800/600),
	                                                          #zoom in, zoom out.
```

- Final step is to make some user commands to move the cube, close the window and auto movement of cube.
- To do so one can use pygame game `pygame.event` that take input event from user like keyboard input, mouse input.
- Last part of code looks like
```python 
glTranslatef(0.0, 0.0, -10)                                #self movement of cube.
glRotatef(0, 0, 0, 0)

while True:                                                #user command input part.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:          #use arrow key to move up, down, left, right. 
			if event.key == pygame.K_LEFT:
				glTranslatef(-1, 0, 0)

			if event.key == pygame.K_RIGHT:
				glTranslatef(1, 0, 0)

			if event.key == pygame.K_UP:
				glTranslatef(0, 1, 0)

			if event.key == pygame.K_DOWN:
				glTranslatef(0, -1, 0)

	glRotatef(1, 3, 1, 1)                            #auto rotation of cube at point(1, 3, 1) with speed 1.
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	cube()
	
	pygame.display.flip()                            #update button.
	pygame.time.wait(10)


main()                                                   #function call.
```

- Overall code looks like: 
```python

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(0, 0, 0),
	(4, 0, 0),
	(4, 4, 0), 
	(0, 4, 0),
	(0, 4, 4),
	(0, 0, 4),
	(4, 0, 4), 
	(4, 4, 4)
	)

edges = (
	(0, 1),
	(0, 3), 
	(0, 5),
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

surfaces = (
	(0, 1, 2, 3),
	(0, 3, 4, 5),
	(0, 1, 6, 5),
	(1, 2, 7, 6),
	(2, 3, 4, 7),
	(4, 5, 6, 7)
	)

colors = (
	(1, 0, 0),
	(0, 1, 0),
	(0, 0, 1),
	(1, 1, 0),
	(0, 1, 1),
	(1, 0, 1),
	)

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


def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


	gluPerspective(45, (display[0] / display[1]), 0.1,  50.0)

	glTranslatef(0.0, 0.0, -10)

	glRotatef(0, 0, 0, 0)


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-1, 0, 0)

				if event.key == pygame.K_RIGHT:
					glTranslatef(1, 0, 0)

				if event.key == pygame.K_UP:
					glTranslatef(0, 1, 0)

				if event.key == pygame.K_DOWN:
					glTranslatef(0, -1, 0)

		glRotatef(1, 3, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		cube()

		pygame.display.flip()
		pygame.time.wait(10)

main()
```
### Done!
![](https://media3.giphy.com/media/obN7DdnUWxuyqz5qZS/200.webp?cid=ecf05e47xa73yjdd83bqrh0835n48zq1zpfx0xcdja4a0mgf&rid=200.webp&ct=g)

## License
### Apache-2.0
