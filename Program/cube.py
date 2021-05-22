#Program to create a cube using OpenGL and Python

# Import part:
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


# Vertices touple:
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

# Edges touple: used to join vertices.
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

# Surface touple: used to create faces.
surfaces = (
	(0, 1, 2, 3),
	(0, 3, 4, 5),
	(0, 1, 6, 5),
	(1, 2, 7, 6),
	(2, 3, 4, 7),
	(4, 5, 6, 7)
	)

#color combination used in program
colors = (
	(1, 0, 0),
	(0, 1, 0),
	(0, 0, 1),
	(1, 1, 0),
	(0, 1, 1),
	(1, 0, 1),
	)

# function to draw cube
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


# screen setup part:
def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


	gluPerspective(45, (display[0] / display[1]), 0.1,  50.0)

	glTranslatef(0.0, 0.0, -10)

	glRotatef(0, 0, 0, 0)

# pygame event part used to follow user command. 
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
